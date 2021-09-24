# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: level.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='level.proto',
  package='COD.Level',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0blevel.proto\x12\tCOD.Level\x1a\x0btypes.proto\"\xae\x01\n\x05Level\x12\x15\n\rformatVersion\x18\x01 \x01(\r\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08\x63reators\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\ncomplexity\x18\x05 \x01(\r\x12\x1a\n\x12maxCheckpointCount\x18\x07 \x01(\r\x12(\n\nlevelNodes\x18\x06 \x03(\x0b\x32\x14.COD.Types.LevelNodeb\x06proto3'
  ,
  dependencies=[types__pb2.DESCRIPTOR,])




_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='COD.Level.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='formatVersion', full_name='COD.Level.Level.formatVersion', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='COD.Level.Level.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creators', full_name='COD.Level.Level.creators', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='COD.Level.Level.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='complexity', full_name='COD.Level.Level.complexity', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxCheckpointCount', full_name='COD.Level.Level.maxCheckpointCount', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='levelNodes', full_name='COD.Level.Level.levelNodes', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=40,
  serialized_end=214,
)

_LEVEL.fields_by_name['levelNodes'].message_type = types__pb2._LEVELNODE
DESCRIPTOR.message_types_by_name['Level'] = _LEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Level = _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), {
  'DESCRIPTOR' : _LEVEL,
  '__module__' : 'level_pb2'
  # @@protoc_insertion_point(class_scope:COD.Level.Level)
  })
_sym_db.RegisterMessage(Level)


# @@protoc_insertion_point(module_scope)