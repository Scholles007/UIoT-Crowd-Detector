import json
import base64
from kafka import KafkaProducer

# TODO: change to host ip
kafka_broker = "192.168.68.121:9093"
topic_name = "crowd_image"

producer = KafkaProducer(bootstrap_servers=kafka_broker, value_serializer=lambda v: json.dumps(v).encode('utf-8'))


with open("..\crowdetect\crowd.jpg.ext", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read())
    # Sending image to Kafka
    producer.send(topic_name, {'image': encoded_image})




