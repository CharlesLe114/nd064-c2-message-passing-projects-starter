import time
from concurrent import futures

import grpc
import items_pb2
import items_pb2_grpc

def response_test(request_value):
    res = items__pb2.LocationResponse(
        person_id = request_value["person_id"],
        creation_time = request_value["creation_time"],
        coordinate = items__pb2.Point(
            latitude = request_value["latitude"],
            longitude = request_value["longitude"]
        )
    )
    return res

class LocationServicer(items_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        return_value = response_test(request_value)
        return return_value


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
items_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)