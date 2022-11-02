from kafka import KafkaProducer
import json


TOPIC_NAME = 'items'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

request_value = {
    "person_id": 2,
    "longitude": 1.23,
    "latitude": 3.43,
    "creation_time": 1667295256
}

data = json.dumps(request_value)
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
producer.send(TOPIC_NAME, value=data)
producer.flush()