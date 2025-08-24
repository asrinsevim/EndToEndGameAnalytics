-- Step 1: Unnest the event_params array and extract the key and value for each parameter.
WITH unnested_params AS (
  SELECT
    PARSE_DATE('%Y%m%d', CAST(event_date AS STRING)) AS event_date,
    user_pseudo_id,
    event_name,
    -- Extract the parameter's key 
    JSON_VALUE(param, '$.key') as param_key,
    -- Extract the parameter's value as a JSON object string 
    JSON_QUERY(param, '$.value') as param_value
  FROM
    `my-game-analytics-v2.game_data_manual.events`
    CROSS JOIN
    -- This unnests the JSON string from the event_params column
    UNNEST(JSON_QUERY_ARRAY(event_params)) AS param
),

-- Step 2: Create a clean table with separate columns for each parameter we care about.
parsed_events AS (
  SELECT
    event_date,
    user_pseudo_id,
    event_name,
    -- If the parameter key is 'value_usd', extract the double_value from its value object.
    CASE
      WHEN param_key = 'value_usd' THEN SAFE_CAST(JSON_VALUE(param_value, '$.double_value') AS FLOAT64)
      ELSE NULL
    END AS purchase_revenue,
    -- If the parameter key is 'level_number', extract the int_value from its value object.
    CASE
      WHEN param_key = 'level_number' THEN SAFE_CAST(JSON_VALUE(param_value, '$.int_value') AS INT64)
      ELSE NULL
    END AS level_number
  FROM
    unnested_params
)

-- Step 3: Now that we have a clean, flat table, we can easily aggregate to get our final KPIs.
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) AS daily_active_users,
  COUNTIF(event_name = 'session_start') AS session_starts,
  SUM(purchase_revenue) AS total_revenue,
  COUNTIF(event_name = 'iap_purchase') AS purchase_count,
  SAFE_DIVIDE(SUM(purchase_revenue), COUNT(DISTINCT user_pseudo_id)) AS arpu,
  COUNT(level_number) AS levels_completed
FROM
  parsed_events
GROUP BY
  event_date
ORDER BY
  event_date ASC;
