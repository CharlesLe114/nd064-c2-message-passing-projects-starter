import os
import logging
from time import sleep
from typing import Dict, List
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, scoped_session
from consumer_models import Location
import json
from kafka import KafkaConsumer

from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry import Point

from geoalchemy2.functions import ST_AsText, ST_Point
# ====================#
# == Define db == #
# ====================#

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

# ====================#
# == Connect to db == #
# ====================#

from sqlalchemy import create_engine
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
logging.basicConfig(level=logging.WARNING)

TOPIC_NAME = 'location_data'
KAFKA_SERVER = "my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092"

class ConsumerService:
    @staticmethod
    def consume():
        # set up kafka consumer to put into database
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_SERVER,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
        for message in consumer:
            print(type(message), "Is the message type")
            location = json.loads(message.value)
            new_location = Location()
            new_location.person_id = location["person_id"]
            new_location.creation_time = datetime.fromtimestamp( location["creation_time"] )
            new_location.coordinate = ST_Point(location["latitude"], location["longitude"])    #- ST_Point undefined
            # new_location.coordinate = "010100000097FDBAD39D925EC0D00A0C59DDC64240"
            print(new_location, "is the location transmitted by kafka")
            # session.add(new_location)
            # session.commit()
            print("I'm in the consumer and here's the message!", new_location)

        # return location
        print(message, " is the most recent message!")
        return message

if __name__ == '__main__':
    consumer_serve = ConsumerService()
    while True:
        sleep(0.05)
        consumer_serve.consume()