# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: image.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'image.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bimage.proto\x12\x0cimageservice\"<\n\x12ImageUploadRequest\x12\x12\n\nimage_name\x18\x01 \x01(\t\x12\x12\n\nimage_data\x18\x02 \x01(\x0c\"4\n\nImageChunk\x12\x12\n\nimage_name\x18\x01 \x01(\t\x12\x12\n\nchunk_data\x18\x02 \x01(\x0c\"9\n\x13ImageUploadResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tfile_path\x18\x02 \x01(\t2\xb6\x01\n\x0cImageService\x12R\n\x0bUploadImage\x12 .imageservice.ImageUploadRequest\x1a!.imageservice.ImageUploadResponse\x12R\n\x11UploadImageStream\x12\x18.imageservice.ImageChunk\x1a!.imageservice.ImageUploadResponse(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEUPLOADREQUEST']._serialized_start=29
  _globals['_IMAGEUPLOADREQUEST']._serialized_end=89
  _globals['_IMAGECHUNK']._serialized_start=91
  _globals['_IMAGECHUNK']._serialized_end=143
  _globals['_IMAGEUPLOADRESPONSE']._serialized_start=145
  _globals['_IMAGEUPLOADRESPONSE']._serialized_end=202
  _globals['_IMAGESERVICE']._serialized_start=205
  _globals['_IMAGESERVICE']._serialized_end=387
# @@protoc_insertion_point(module_scope)
