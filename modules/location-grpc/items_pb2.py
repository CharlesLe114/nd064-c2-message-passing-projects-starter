# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: items.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bitems.proto\"l\n\x0fLocationMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\x05\x12\x10\n\x08latitude\x18\x04 \x01(\x05\x12\x15\n\rcreation_time\x18\x05 \x01(\x03\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"X\n\x10LocationResponse\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x15\n\rcreation_time\x18\x02 \x01(\x03\x12\x1a\n\ncoordinate\x18\x03 \x01(\x0b\x32\x06.Point2@\n\x0fLocationService\x12-\n\x06\x43reate\x12\x10.LocationMessage\x1a\x11.LocationResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'items_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCATIONMESSAGE._serialized_start=15
  _LOCATIONMESSAGE._serialized_end=123
  _POINT._serialized_start=125
  _POINT._serialized_end=169
  _LOCATIONRESPONSE._serialized_start=171
  _LOCATIONRESPONSE._serialized_end=259
  _LOCATIONSERVICE._serialized_start=261
  _LOCATIONSERVICE._serialized_end=325
# @@protoc_insertion_point(module_scope)
