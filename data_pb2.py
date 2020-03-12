# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\ndata.proto\"/\n\nInputImage\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x13\n\x0bpart_number\x18\x02 \x01(\x05\"=\n\nImageParts\x12\x0f\n\x07ratio_x\x18\x01 \x01(\x05\x12\x0f\n\x07ratio_y\x18\x02 \x01(\x05\x12\r\n\x05parts\x18\x03 \x01(\x0c\"#\n\x0bImageResult\x12\x14\n\x0cresult_image\x18\x01 \x01(\x0c\x32\x31\n\nCroppImage\x12#\n\x05\x63ropp\x12\x0b.InputImage\x1a\x0b.ImageParts\"\x00\x32>\n\x10\x43oncatenateImage\x12*\n\x0b\x63oncatenate\x12\x0b.ImageParts\x1a\x0c.ImageResult\"\x00\x62\x06proto3'
)




_INPUTIMAGE = _descriptor.Descriptor(
  name='InputImage',
  full_name='InputImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='InputImage.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='part_number', full_name='InputImage.part_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=14,
  serialized_end=61,
)


_IMAGEPARTS = _descriptor.Descriptor(
  name='ImageParts',
  full_name='ImageParts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ratio_x', full_name='ImageParts.ratio_x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratio_y', full_name='ImageParts.ratio_y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parts', full_name='ImageParts.parts', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=63,
  serialized_end=124,
)


_IMAGERESULT = _descriptor.Descriptor(
  name='ImageResult',
  full_name='ImageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_image', full_name='ImageResult.result_image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=126,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['InputImage'] = _INPUTIMAGE
DESCRIPTOR.message_types_by_name['ImageParts'] = _IMAGEPARTS
DESCRIPTOR.message_types_by_name['ImageResult'] = _IMAGERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputImage = _reflection.GeneratedProtocolMessageType('InputImage', (_message.Message,), {
  'DESCRIPTOR' : _INPUTIMAGE,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:InputImage)
  })
_sym_db.RegisterMessage(InputImage)

ImageParts = _reflection.GeneratedProtocolMessageType('ImageParts', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPARTS,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:ImageParts)
  })
_sym_db.RegisterMessage(ImageParts)

ImageResult = _reflection.GeneratedProtocolMessageType('ImageResult', (_message.Message,), {
  'DESCRIPTOR' : _IMAGERESULT,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:ImageResult)
  })
_sym_db.RegisterMessage(ImageResult)



_CROPPIMAGE = _descriptor.ServiceDescriptor(
  name='CroppImage',
  full_name='CroppImage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=163,
  serialized_end=212,
  methods=[
  _descriptor.MethodDescriptor(
    name='cropp',
    full_name='CroppImage.cropp',
    index=0,
    containing_service=None,
    input_type=_INPUTIMAGE,
    output_type=_IMAGEPARTS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CROPPIMAGE)

DESCRIPTOR.services_by_name['CroppImage'] = _CROPPIMAGE


_CONCATENATEIMAGE = _descriptor.ServiceDescriptor(
  name='ConcatenateImage',
  full_name='ConcatenateImage',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=214,
  serialized_end=276,
  methods=[
  _descriptor.MethodDescriptor(
    name='concatenate',
    full_name='ConcatenateImage.concatenate',
    index=0,
    containing_service=None,
    input_type=_IMAGEPARTS,
    output_type=_IMAGERESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONCATENATEIMAGE)

DESCRIPTOR.services_by_name['ConcatenateImage'] = _CONCATENATEIMAGE

# @@protoc_insertion_point(module_scope)
