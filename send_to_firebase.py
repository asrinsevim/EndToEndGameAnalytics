import requests
import json
import random
import time
from datetime import datetime, timedelta
import secrets
from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv()

MEASUREMENT_ID = os.getenv("MEASUREMENT_ID")
API_SECRET = os.getenv("API_SECRET")

if not MEASUREMENT_ID or not API_SECRET:
    raise ValueError("Hata: Lütfen .env dosyanızın içine MEASUREMENT_ID ve API_SECRET değerlerini ekleyin.")

# --- Configuration ---
NUM_USERS = 100 
START_DATE = datetime.now() - timedelta(days=2) 

fake = Faker()

print("Starting data generation and sending to Firebase...")

# Loop through each user to simulate their activity
for i in range(NUM_USERS):
    user_id_internal = i + 1000
    app_instance_id = secrets.token_hex(16)
    
    events_payload = []
    
    events_payload.append({
        'name': 'first_open',
        'params': {"source": random.choice(["Facebook", "Google", "Organic"])}
    })
    
    num_events = random.randint(1, 20)
    for _ in range(num_events):
        event_name = random.choices(['level_complete', 'ad_watched', 'iap_purchase', 'session_start'], weights=[0.6, 0.25, 0.05, 0.1], k=1)[0]
        params = {}
        if event_name == 'level_complete':
            params['level_number'] = random.randint(1, 15)
        elif event_name == 'iap_purchase':
            params['value_usd'] = random.choice([1.99, 5.99, 9.99])
        
        events_payload.append({
            'name': event_name,
            'params': params
        })
        
    request_body = {
        'app_instance_id': app_instance_id,
        'events': events_payload
    }

    url = f"https://www.google-analytics.com/mp/collect?measurement_id={MEASUREMENT_ID}&api_secret={API_SECRET}"
    
    try:
        response = requests.post(url, data=json.dumps(request_body), headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        print(f"Successfully sent event batch for user {user_id_internal}. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data for user {user_id_internal}: {e}")
    
    time.sleep(0.2) 

print("Script finished sending data.")
