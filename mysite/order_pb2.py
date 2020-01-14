# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='order.proto',
  package='orders',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0border.proto\x12\x06orders\"\x1d\n\nGetRequest\x12\x0f\n\x07orderID\x18\x01 \x01(\t\"\x1a\n\x08GetReply\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\"\x1d\n\nSetRequest\x12\x0f\n\x07orderID\x18\x01 \x01(\t\"\x1a\n\x08SetReply\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t2o\n\x05Order\x12\x32\n\x08GetState\x12\x12.orders.GetRequest\x1a\x10.orders.GetReply\"\x00\x12\x32\n\x08SetState\x12\x12.orders.SetRequest\x1a\x10.orders.SetReply\"\x00\x62\x06proto3')
)




_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='orders.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderID', full_name='orders.GetRequest.orderID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=52,
)


_GETREPLY = _descriptor.Descriptor(
  name='GetReply',
  full_name='orders.GetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='orders.GetReply.answer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=80,
)


_SETREQUEST = _descriptor.Descriptor(
  name='SetRequest',
  full_name='orders.SetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderID', full_name='orders.SetRequest.orderID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=111,
)


_SETREPLY = _descriptor.Descriptor(
  name='SetReply',
  full_name='orders.SetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='orders.SetReply.answer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetReply'] = _GETREPLY
DESCRIPTOR.message_types_by_name['SetRequest'] = _SETREQUEST
DESCRIPTOR.message_types_by_name['SetReply'] = _SETREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:orders.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetReply = _reflection.GeneratedProtocolMessageType('GetReply', (_message.Message,), {
  'DESCRIPTOR' : _GETREPLY,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:orders.GetReply)
  })
_sym_db.RegisterMessage(GetReply)

SetRequest = _reflection.GeneratedProtocolMessageType('SetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:orders.SetRequest)
  })
_sym_db.RegisterMessage(SetRequest)

SetReply = _reflection.GeneratedProtocolMessageType('SetReply', (_message.Message,), {
  'DESCRIPTOR' : _SETREPLY,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:orders.SetReply)
  })
_sym_db.RegisterMessage(SetReply)



_ORDER = _descriptor.ServiceDescriptor(
  name='Order',
  full_name='orders.Order',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=141,
  serialized_end=252,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='orders.Order.GetState',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetState',
    full_name='orders.Order.SetState',
    index=1,
    containing_service=None,
    input_type=_SETREQUEST,
    output_type=_SETREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDER)

DESCRIPTOR.services_by_name['Order'] = _ORDER

# @@protoc_insertion_point(module_scope)
