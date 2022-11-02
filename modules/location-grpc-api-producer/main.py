import time
from concurrent import futures

import grpc
import locations_pb2
import locations_pb2_grpc
import json

from kafka import KafkaProducer
from datetime import datetime, timezone

TOPIC_NAME = 'location_data'
KAFKA_SERVER = "my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092"

def response_test(request_value):
    res = locations_pb2.LocationResponse(
        person_id = request_value["person_id"],
        creation_time = request_value["creation_time"],
        coordinate = locations_pb2.Point(
            latitude = request_value["latitude"],
            longitude = request_value["longitude"]
        )
    )
    return res

class LocationServicer(locations_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }

        data = json.dumps(request_value).encode('utf-8') # convert dict to string -> match with kafka requirement
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        producer.send(TOPIC_NAME, value=data)
        producer.flush()

        print(data)
        return locations_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)