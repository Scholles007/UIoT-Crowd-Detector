import json
from kafka import KafkaConsumer

# TODO: change to host ip
kafka_broker = "192.168.68.121:9093"
topic_name = "crowd_params"

print("Starting consumer...") 
consumer = KafkaConsumer(topic_name, bootstrap_servers=kafka_broker)
print("Consumer started")
for msg in consumer:
    print(f"Received message: {msg}")
    # Load rule as json
    rules = json.loads(msg.value)
    # Aqui vai ter algo do tipo: {crowd_thld: 5, frames_total: 60} 
    # esses valores precisam ser inseridos no codigo do crowd_detector
    # for r in rules:
      # do something
