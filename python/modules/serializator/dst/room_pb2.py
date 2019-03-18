# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: room.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='room.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nroom.proto\"f\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x10\n\x08rotation\x18\x05 \x03(\x02\x12\x11\n\tdirection\x18\x06 \x03(\x05\"l\n\x04Room\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x07persons\x18\x02 \x03(\x0b\x32\x07.Person\x12\x0b\n\x03seq\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x10\n\x08rotation\x18\x05 \x01(\x02\x12\x11\n\tdirection\x18\x06 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Person.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age', full_name='Person.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='Person.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='Person.rotation', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='Person.direction', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=116,
)


_ROOM = _descriptor.Descriptor(
  name='Room',
  full_name='Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Room.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='persons', full_name='Room.persons', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq', full_name='Room.seq', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Room.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='Room.rotation', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='Room.direction', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=226,
)

_ROOM.fields_by_name['persons'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['Room'] = _ROOM

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'room_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)

Room = _reflection.GeneratedProtocolMessageType('Room', (_message.Message,), dict(
  DESCRIPTOR = _ROOM,
  __module__ = 'room_pb2'
  # @@protoc_insertion_point(class_scope:Room)
  ))
_sym_db.RegisterMessage(Room)


# @@protoc_insertion_point(module_scope)
