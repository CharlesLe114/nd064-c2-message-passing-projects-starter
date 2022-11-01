import grpc
import items_pb2
import items_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = items_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = items_pb2.LocationMessage(
    id=1,
    person_id=2,
    longitude=1234,
    latitude=1234,
    creation_time=1667295256
)


response = stub.Create(location)

print(response)