from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from kafka import KafkaConsumer
import json

from datetime import datetime
from app.udaconnect.schemas import ConnectionSchema, LocationSchema

db = SQLAlchemy()

TOPIC_NAME = 'location_data'
KAFKA_SERVER = "my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092"

def process_message(message):
    value_json = message.value.json()

    new_location = Location()
    new_location.person_id = message["person_id"]
    new_location.creation_time = datetime.fromtimestamp( message["creation_time"] )
    new_location.coordinate = ST_Point(message["latitude"], message["longitude"])
    db.session.add(new_location)
    db.session.commit()

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER)
    for message in consumer:
        process_message(message)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
