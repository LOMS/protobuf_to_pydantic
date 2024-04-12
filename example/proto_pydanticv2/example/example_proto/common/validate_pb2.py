# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/example_proto/common/validate.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+example/example_proto/common/validate.proto\x12\x08validate\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x98\x07\n\nFieldRules\x12\'\n\x07message\x18\x11 \x01(\x0b\x32\x16.validate.MessageRules\x12%\n\x05\x66loat\x18\x01 \x01(\x0b\x32\x14.validate.FloatRulesH\x00\x12\'\n\x06\x64ouble\x18\x02 \x01(\x0b\x32\x15.validate.DoubleRulesH\x00\x12%\n\x05int32\x18\x03 \x01(\x0b\x32\x14.validate.Int32RulesH\x00\x12%\n\x05int64\x18\x04 \x01(\x0b\x32\x14.validate.Int64RulesH\x00\x12\'\n\x06uint32\x18\x05 \x01(\x0b\x32\x15.validate.UInt32RulesH\x00\x12\'\n\x06uint64\x18\x06 \x01(\x0b\x32\x15.validate.UInt64RulesH\x00\x12\'\n\x06sint32\x18\x07 \x01(\x0b\x32\x15.validate.SInt32RulesH\x00\x12\'\n\x06sint64\x18\x08 \x01(\x0b\x32\x15.validate.SInt64RulesH\x00\x12)\n\x07\x66ixed32\x18\t \x01(\x0b\x32\x16.validate.Fixed32RulesH\x00\x12)\n\x07\x66ixed64\x18\n \x01(\x0b\x32\x16.validate.Fixed64RulesH\x00\x12+\n\x08sfixed32\x18\x0b \x01(\x0b\x32\x17.validate.SFixed32RulesH\x00\x12+\n\x08sfixed64\x18\x0c \x01(\x0b\x32\x17.validate.SFixed64RulesH\x00\x12#\n\x04\x62ool\x18\r \x01(\x0b\x32\x13.validate.BoolRulesH\x00\x12\'\n\x06string\x18\x0e \x01(\x0b\x32\x15.validate.StringRulesH\x00\x12%\n\x05\x62ytes\x18\x0f \x01(\x0b\x32\x14.validate.BytesRulesH\x00\x12#\n\x04\x65num\x18\x10 \x01(\x0b\x32\x13.validate.EnumRulesH\x00\x12+\n\x08repeated\x18\x12 \x01(\x0b\x32\x17.validate.RepeatedRulesH\x00\x12!\n\x03map\x18\x13 \x01(\x0b\x32\x12.validate.MapRulesH\x00\x12!\n\x03\x61ny\x18\x14 \x01(\x0b\x32\x12.validate.AnyRulesH\x00\x12+\n\x08\x64uration\x18\x15 \x01(\x0b\x32\x17.validate.DurationRulesH\x00\x12-\n\ttimestamp\x18\x16 \x01(\x0b\x32\x18.validate.TimestampRulesH\x00\x42\x06\n\x04type\"\x7f\n\nFloatRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x02\x12\n\n\x02lt\x18\x02 \x01(\x02\x12\x0b\n\x03lte\x18\x03 \x01(\x02\x12\n\n\x02gt\x18\x04 \x01(\x02\x12\x0b\n\x03gte\x18\x05 \x01(\x02\x12\n\n\x02in\x18\x06 \x03(\x02\x12\x0e\n\x06not_in\x18\x07 \x03(\x02\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x80\x01\n\x0b\x44oubleRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x01\x12\n\n\x02lt\x18\x02 \x01(\x01\x12\x0b\n\x03lte\x18\x03 \x01(\x01\x12\n\n\x02gt\x18\x04 \x01(\x01\x12\x0b\n\x03gte\x18\x05 \x01(\x01\x12\n\n\x02in\x18\x06 \x03(\x01\x12\x0e\n\x06not_in\x18\x07 \x03(\x01\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x7f\n\nInt32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x05\x12\n\n\x02lt\x18\x02 \x01(\x05\x12\x0b\n\x03lte\x18\x03 \x01(\x05\x12\n\n\x02gt\x18\x04 \x01(\x05\x12\x0b\n\x03gte\x18\x05 \x01(\x05\x12\n\n\x02in\x18\x06 \x03(\x05\x12\x0e\n\x06not_in\x18\x07 \x03(\x05\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x7f\n\nInt64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x03\x12\n\n\x02lt\x18\x02 \x01(\x03\x12\x0b\n\x03lte\x18\x03 \x01(\x03\x12\n\n\x02gt\x18\x04 \x01(\x03\x12\x0b\n\x03gte\x18\x05 \x01(\x03\x12\n\n\x02in\x18\x06 \x03(\x03\x12\x0e\n\x06not_in\x18\x07 \x03(\x03\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x80\x01\n\x0bUInt32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\r\x12\n\n\x02lt\x18\x02 \x01(\r\x12\x0b\n\x03lte\x18\x03 \x01(\r\x12\n\n\x02gt\x18\x04 \x01(\r\x12\x0b\n\x03gte\x18\x05 \x01(\r\x12\n\n\x02in\x18\x06 \x03(\r\x12\x0e\n\x06not_in\x18\x07 \x03(\r\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x80\x01\n\x0bUInt64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x04\x12\n\n\x02lt\x18\x02 \x01(\x04\x12\x0b\n\x03lte\x18\x03 \x01(\x04\x12\n\n\x02gt\x18\x04 \x01(\x04\x12\x0b\n\x03gte\x18\x05 \x01(\x04\x12\n\n\x02in\x18\x06 \x03(\x04\x12\x0e\n\x06not_in\x18\x07 \x03(\x04\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x80\x01\n\x0bSInt32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x11\x12\n\n\x02lt\x18\x02 \x01(\x11\x12\x0b\n\x03lte\x18\x03 \x01(\x11\x12\n\n\x02gt\x18\x04 \x01(\x11\x12\x0b\n\x03gte\x18\x05 \x01(\x11\x12\n\n\x02in\x18\x06 \x03(\x11\x12\x0e\n\x06not_in\x18\x07 \x03(\x11\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x80\x01\n\x0bSInt64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x12\x12\n\n\x02lt\x18\x02 \x01(\x12\x12\x0b\n\x03lte\x18\x03 \x01(\x12\x12\n\n\x02gt\x18\x04 \x01(\x12\x12\x0b\n\x03gte\x18\x05 \x01(\x12\x12\n\n\x02in\x18\x06 \x03(\x12\x12\x0e\n\x06not_in\x18\x07 \x03(\x12\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x81\x01\n\x0c\x46ixed32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x07\x12\n\n\x02lt\x18\x02 \x01(\x07\x12\x0b\n\x03lte\x18\x03 \x01(\x07\x12\n\n\x02gt\x18\x04 \x01(\x07\x12\x0b\n\x03gte\x18\x05 \x01(\x07\x12\n\n\x02in\x18\x06 \x03(\x07\x12\x0e\n\x06not_in\x18\x07 \x03(\x07\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x81\x01\n\x0c\x46ixed64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x06\x12\n\n\x02lt\x18\x02 \x01(\x06\x12\x0b\n\x03lte\x18\x03 \x01(\x06\x12\n\n\x02gt\x18\x04 \x01(\x06\x12\x0b\n\x03gte\x18\x05 \x01(\x06\x12\n\n\x02in\x18\x06 \x03(\x06\x12\x0e\n\x06not_in\x18\x07 \x03(\x06\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x82\x01\n\rSFixed32Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x0f\x12\n\n\x02lt\x18\x02 \x01(\x0f\x12\x0b\n\x03lte\x18\x03 \x01(\x0f\x12\n\n\x02gt\x18\x04 \x01(\x0f\x12\x0b\n\x03gte\x18\x05 \x01(\x0f\x12\n\n\x02in\x18\x06 \x03(\x0f\x12\x0e\n\x06not_in\x18\x07 \x03(\x0f\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x82\x01\n\rSFixed64Rules\x12\r\n\x05\x63onst\x18\x01 \x01(\x10\x12\n\n\x02lt\x18\x02 \x01(\x10\x12\x0b\n\x03lte\x18\x03 \x01(\x10\x12\n\n\x02gt\x18\x04 \x01(\x10\x12\x0b\n\x03gte\x18\x05 \x01(\x10\x12\n\n\x02in\x18\x06 \x03(\x10\x12\x0e\n\x06not_in\x18\x07 \x03(\x10\x12\x14\n\x0cignore_empty\x18\x08 \x01(\x08\"\x1a\n\tBoolRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x08\"\xfd\x03\n\x0bStringRules\x12\r\n\x05\x63onst\x18\x01 \x01(\t\x12\x0b\n\x03len\x18\x13 \x01(\x04\x12\x0f\n\x07min_len\x18\x02 \x01(\x04\x12\x0f\n\x07max_len\x18\x03 \x01(\x04\x12\x11\n\tlen_bytes\x18\x14 \x01(\x04\x12\x11\n\tmin_bytes\x18\x04 \x01(\x04\x12\x11\n\tmax_bytes\x18\x05 \x01(\x04\x12\x0f\n\x07pattern\x18\x06 \x01(\t\x12\x0e\n\x06prefix\x18\x07 \x01(\t\x12\x0e\n\x06suffix\x18\x08 \x01(\t\x12\x10\n\x08\x63ontains\x18\t \x01(\t\x12\x14\n\x0cnot_contains\x18\x17 \x01(\t\x12\n\n\x02in\x18\n \x03(\t\x12\x0e\n\x06not_in\x18\x0b \x03(\t\x12\x0f\n\x05\x65mail\x18\x0c \x01(\x08H\x00\x12\x12\n\x08hostname\x18\r \x01(\x08H\x00\x12\x0c\n\x02ip\x18\x0e \x01(\x08H\x00\x12\x0e\n\x04ipv4\x18\x0f \x01(\x08H\x00\x12\x0e\n\x04ipv6\x18\x10 \x01(\x08H\x00\x12\r\n\x03uri\x18\x11 \x01(\x08H\x00\x12\x11\n\x07uri_ref\x18\x12 \x01(\x08H\x00\x12\x11\n\x07\x61\x64\x64ress\x18\x15 \x01(\x08H\x00\x12\x0e\n\x04uuid\x18\x16 \x01(\x08H\x00\x12\x30\n\x10well_known_regex\x18\x18 \x01(\x0e\x32\x14.validate.KnownRegexH\x00\x12\x14\n\x06strict\x18\x19 \x01(\x08:\x04true\x12\x14\n\x0cignore_empty\x18\x1a \x01(\x08\x42\x0c\n\nwell_known\"\xfb\x01\n\nBytesRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x0c\x12\x0b\n\x03len\x18\r \x01(\x04\x12\x0f\n\x07min_len\x18\x02 \x01(\x04\x12\x0f\n\x07max_len\x18\x03 \x01(\x04\x12\x0f\n\x07pattern\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\x0c\x12\x0e\n\x06suffix\x18\x06 \x01(\x0c\x12\x10\n\x08\x63ontains\x18\x07 \x01(\x0c\x12\n\n\x02in\x18\x08 \x03(\x0c\x12\x0e\n\x06not_in\x18\t \x03(\x0c\x12\x0c\n\x02ip\x18\n \x01(\x08H\x00\x12\x0e\n\x04ipv4\x18\x0b \x01(\x08H\x00\x12\x0e\n\x04ipv6\x18\x0c \x01(\x08H\x00\x12\x14\n\x0cignore_empty\x18\x0e \x01(\x08\x42\x0c\n\nwell_known\"L\n\tEnumRules\x12\r\n\x05\x63onst\x18\x01 \x01(\x05\x12\x14\n\x0c\x64\x65\x66ined_only\x18\x02 \x01(\x08\x12\n\n\x02in\x18\x03 \x03(\x05\x12\x0e\n\x06not_in\x18\x04 \x03(\x05\".\n\x0cMessageRules\x12\x0c\n\x04skip\x18\x01 \x01(\x08\x12\x10\n\x08required\x18\x02 \x01(\x08\"\x80\x01\n\rRepeatedRules\x12\x11\n\tmin_items\x18\x01 \x01(\x04\x12\x11\n\tmax_items\x18\x02 \x01(\x04\x12\x0e\n\x06unique\x18\x03 \x01(\x08\x12#\n\x05items\x18\x04 \x01(\x0b\x32\x14.validate.FieldRules\x12\x14\n\x0cignore_empty\x18\x05 \x01(\x08\"\xa3\x01\n\x08MapRules\x12\x11\n\tmin_pairs\x18\x01 \x01(\x04\x12\x11\n\tmax_pairs\x18\x02 \x01(\x04\x12\x11\n\tno_sparse\x18\x03 \x01(\x08\x12\"\n\x04keys\x18\x04 \x01(\x0b\x32\x14.validate.FieldRules\x12$\n\x06values\x18\x05 \x01(\x0b\x32\x14.validate.FieldRules\x12\x14\n\x0cignore_empty\x18\x06 \x01(\x08\"8\n\x08\x41nyRules\x12\x10\n\x08required\x18\x01 \x01(\x08\x12\n\n\x02in\x18\x02 \x03(\t\x12\x0e\n\x06not_in\x18\x03 \x03(\t\"\xbb\x02\n\rDurationRules\x12\x10\n\x08required\x18\x01 \x01(\x08\x12(\n\x05\x63onst\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x02lt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12&\n\x03lte\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x02gt\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12&\n\x03gte\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12%\n\x02in\x18\x07 \x03(\x0b\x32\x19.google.protobuf.Duration\x12)\n\x06not_in\x18\x08 \x03(\x0b\x32\x19.google.protobuf.Duration\"\xba\x02\n\x0eTimestampRules\x12\x10\n\x08required\x18\x01 \x01(\x08\x12)\n\x05\x63onst\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02lt\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03lte\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02gt\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03gte\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06lt_now\x18\x07 \x01(\x08\x12\x0e\n\x06gt_now\x18\x08 \x01(\x08\x12)\n\x06within\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration*F\n\nKnownRegex\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10HTTP_HEADER_NAME\x10\x01\x12\x15\n\x11HTTP_HEADER_VALUE\x10\x02:2\n\x08\x64isabled\x12\x1f.google.protobuf.MessageOptions\x18\xaf\x08 \x01(\x08:1\n\x07ignored\x12\x1f.google.protobuf.MessageOptions\x18\xb0\x08 \x01(\x08:0\n\x08required\x12\x1d.google.protobuf.OneofOptions\x18\xaf\x08 \x01(\x08:C\n\x05rules\x12\x1d.google.protobuf.FieldOptions\x18\xaf\x08 \x01(\x0b\x32\x14.validate.FieldRulesBP\n\x1aio.envoyproxy.pgv.validateZ2github.com/envoyproxy/protoc-gen-validate/validate')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example.example_proto.common.validate_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(disabled)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(ignored)
  google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(required)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(rules)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032io.envoyproxy.pgv.validateZ2github.com/envoyproxy/protoc-gen-validate/validate'
  _KNOWNREGEX._serialized_start=4561
  _KNOWNREGEX._serialized_end=4631
  _FIELDRULES._serialized_start=157
  _FIELDRULES._serialized_end=1077
  _FLOATRULES._serialized_start=1079
  _FLOATRULES._serialized_end=1206
  _DOUBLERULES._serialized_start=1209
  _DOUBLERULES._serialized_end=1337
  _INT32RULES._serialized_start=1339
  _INT32RULES._serialized_end=1466
  _INT64RULES._serialized_start=1468
  _INT64RULES._serialized_end=1595
  _UINT32RULES._serialized_start=1598
  _UINT32RULES._serialized_end=1726
  _UINT64RULES._serialized_start=1729
  _UINT64RULES._serialized_end=1857
  _SINT32RULES._serialized_start=1860
  _SINT32RULES._serialized_end=1988
  _SINT64RULES._serialized_start=1991
  _SINT64RULES._serialized_end=2119
  _FIXED32RULES._serialized_start=2122
  _FIXED32RULES._serialized_end=2251
  _FIXED64RULES._serialized_start=2254
  _FIXED64RULES._serialized_end=2383
  _SFIXED32RULES._serialized_start=2386
  _SFIXED32RULES._serialized_end=2516
  _SFIXED64RULES._serialized_start=2519
  _SFIXED64RULES._serialized_end=2649
  _BOOLRULES._serialized_start=2651
  _BOOLRULES._serialized_end=2677
  _STRINGRULES._serialized_start=2680
  _STRINGRULES._serialized_end=3189
  _BYTESRULES._serialized_start=3192
  _BYTESRULES._serialized_end=3443
  _ENUMRULES._serialized_start=3445
  _ENUMRULES._serialized_end=3521
  _MESSAGERULES._serialized_start=3523
  _MESSAGERULES._serialized_end=3569
  _REPEATEDRULES._serialized_start=3572
  _REPEATEDRULES._serialized_end=3700
  _MAPRULES._serialized_start=3703
  _MAPRULES._serialized_end=3866
  _ANYRULES._serialized_start=3868
  _ANYRULES._serialized_end=3924
  _DURATIONRULES._serialized_start=3927
  _DURATIONRULES._serialized_end=4242
  _TIMESTAMPRULES._serialized_start=4245
  _TIMESTAMPRULES._serialized_end=4559
# @@protoc_insertion_point(module_scope)
