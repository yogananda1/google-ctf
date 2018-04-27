#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aart_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aart_message.proto',
  package='',
  serialized_pb='\n\x12\x61\x61rt_message.proto\"\xbc\x01\n\x0b\x41\x41rtMessage\x12*\n\x04type\x18\x01 \x02(\x0e\x32\x1c.AArtMessage.AArtMessageType\x12\x11\n\tclient_id\x18\x02 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\t\"]\n\x0f\x41\x41rtMessageType\x12\x0b\n\x07R_HELLO\x10\x00\x12\x12\n\x0eR_CAPABILITIES\x10\x01\x12\x0f\n\x0bR_OPERATION\x10\x02\x12\x18\n\x14R_OPERATION_RESPONSE\x10\x03')



_AARTMESSAGE_AARTMESSAGETYPE = _descriptor.EnumDescriptor(
  name='AArtMessageType',
  full_name='AArtMessage.AArtMessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='R_HELLO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='R_CAPABILITIES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='R_OPERATION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='R_OPERATION_RESPONSE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=118,
  serialized_end=211,
)


_AARTMESSAGE = _descriptor.Descriptor(
  name='AArtMessage',
  full_name='AArtMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='AArtMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='AArtMessage.client_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='AArtMessage.content', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AARTMESSAGE_AARTMESSAGETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=211,
)

_AARTMESSAGE.fields_by_name['type'].enum_type = _AARTMESSAGE_AARTMESSAGETYPE
_AARTMESSAGE_AARTMESSAGETYPE.containing_type = _AARTMESSAGE;
DESCRIPTOR.message_types_by_name['AArtMessage'] = _AARTMESSAGE

class AArtMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AARTMESSAGE

  # @@protoc_insertion_point(class_scope:AArtMessage)


# @@protoc_insertion_point(module_scope)