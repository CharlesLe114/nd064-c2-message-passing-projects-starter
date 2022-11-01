from kafka import KafkaConsumer


TOPIC_NAME = 'location_data'

consumer = KafkaConsumer('location_data',bootstrap_servers='localhost:9092')
for message in consumer:
    print (message)