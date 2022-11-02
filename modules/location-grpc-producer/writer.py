import grpc
import locations_pb2
import locations_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:30005")
stub = locations_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = locations_pb2.LocationMessage(
    person_id=2,
    longitude=1.23,
    latitude=3.43,
    creation_time=1667295256
)


response = stub.Create(location)

print(response)