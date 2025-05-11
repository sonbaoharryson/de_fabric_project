# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

!pip install requests pytz azure-servicebus

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json
import time

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def call_weather_api(api_key = "your_api_key_from_weatherstack"):
    try:
        url = f"http://api.weatherstack.com/current?access_key={api_key}"
        querystring = [
            {"query":"HaNoi;"},
            {"query":"Da Nang"},
            {"query":"Ho Chi Minh;"}
        ]
        result = []
        for city in querystring:
            response = requests.get(url, params= city)
            if response.status_code==200:
                response = response.json()
                if "success" in response:
                    continue
                result.append(response)
        return result
    except Exception as e:
        raise response.raise_for_status

def send_to_eventstream(message, connection_string="event_stream_connection_string_sas_token"):
    entity_path = None
    for param in connection_string.split(';'):
        if param.startswith('EntityPath='):
            entity_path = param.split('=')[1]
            break
    
    if not entity_path:
        raise ValueError("EntityPath is missing in the connection string. Please check you Fabric setup. Can get the connection string in EventStream after publishing a custom pipeline.")

    if isinstance(message, dict):
        message = [message]

    service_bs_client = ServiceBusClient.from_connection_string(connection_string)
    try:
        with service_bs_client.get_queue_sender(entity_path) as sender:
            batch_message = [ServiceBusMessage(json.dumps(msg)) for msg in message]
            sender.send_messages(batch_message)
            print(f"Successfully send {len(message)} records to EventStream.")
    except Exception as e:
        print(f"Error sending messages: {e}")
    finally:
        service_bs_client.close()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

while True:
    data = call_weather_api()
    send_to_eventstream(data)
    time.sleep(2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
