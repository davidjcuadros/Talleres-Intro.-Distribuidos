# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: servicio.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'servicio.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservicio.proto\"7\n\x10OperacionRequest\x12\x15\n\rtipoOperacion\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61to\x18\x02 \x01(\x05\"%\n\x10ResultadoReceive\x12\x11\n\tresultado\x18\x01 \x01(\x05\"\x06\n\x04Nulo2\x96\x01\n\x07Sistema\x12\x15\n\x05Listo\x12\x05.Nulo\x1a\x05.Nulo\x12:\n\x12SolicitudOperacion\x12\x11.OperacionRequest\x1a\x11.ResultadoReceive\x12\x38\n\x10OperacionParcial\x12\x11.OperacionRequest\x1a\x11.ResultadoReceiveb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'servicio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OPERACIONREQUEST']._serialized_start=18
  _globals['_OPERACIONREQUEST']._serialized_end=73
  _globals['_RESULTADORECEIVE']._serialized_start=75
  _globals['_RESULTADORECEIVE']._serialized_end=112
  _globals['_NULO']._serialized_start=114
  _globals['_NULO']._serialized_end=120
  _globals['_SISTEMA']._serialized_start=123
  _globals['_SISTEMA']._serialized_end=273
# @@protoc_insertion_point(module_scope)
