from kafka import KafkaConsumer


TOPIC_NAME = 'location_data'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)