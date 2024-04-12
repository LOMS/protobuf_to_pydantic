# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/p2p_validate.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19protos/p2p_validate.proto\x12\x0cp2p_validate\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1e\n\nOneofRules\x12\x10\n\x08optional\x18\x01 \x03(\t\"\x81\x08\n\nFieldRules\x12\x30\n\x07message\x18\x11 \x01(\x0b\x32\x1a.p2p_validate.MessageRulesH\x01\x88\x01\x01\x12)\n\x05\x66loat\x18\x01 \x01(\x0b\x32\x18.p2p_validate.FloatRulesH\x00\x12+\n\x06\x64ouble\x18\x02 \x01(\x0b\x32\x19.p2p_validate.DoubleRulesH\x00\x12)\n\x05int32\x18\x03 \x01(\x0b\x32\x18.p2p_validate.Int32RulesH\x00\x12)\n\x05int64\x18\x04 \x01(\x0b\x32\x18.p2p_validate.Int64RulesH\x00\x12+\n\x06uint32\x18\x05 \x01(\x0b\x32\x19.p2p_validate.UInt32RulesH\x00\x12+\n\x06uint64\x18\x06 \x01(\x0b\x32\x19.p2p_validate.UInt64RulesH\x00\x12+\n\x06sint32\x18\x07 \x01(\x0b\x32\x19.p2p_validate.SInt32RulesH\x00\x12+\n\x06sint64\x18\x08 \x01(\x0b\x32\x19.p2p_validate.SInt64RulesH\x00\x12-\n\x07\x66ixed32\x18\t \x01(\x0b\x32\x1a.p2p_validate.Fixed32RulesH\x00\x12-\n\x07\x66ixed64\x18\n \x01(\x0b\x32\x1a.p2p_validate.Fixed64RulesH\x00\x12/\n\x08sfixed32\x18\x0b \x01(\x0b\x32\x1b.p2p_validate.SFixed32RulesH\x00\x12/\n\x08sfixed64\x18\x0c \x01(\x0b\x32\x1b.p2p_validate.SFixed64RulesH\x00\x12\'\n\x04\x62ool\x18\r \x01(\x0b\x32\x17.p2p_validate.BoolRulesH\x00\x12+\n\x06string\x18\x0e \x01(\x0b\x32\x19.p2p_validate.StringRulesH\x00\x12)\n\x05\x62ytes\x18\x0f \x01(\x0b\x32\x18.p2p_validate.BytesRulesH\x00\x12\'\n\x04\x65num\x18\x10 \x01(\x0b\x32\x17.p2p_validate.EnumRulesH\x00\x12/\n\x08repeated\x18\x12 \x01(\x0b\x32\x1b.p2p_validate.RepeatedRulesH\x00\x12%\n\x03map\x18\x13 \x01(\x0b\x32\x16.p2p_validate.MapRulesH\x00\x12%\n\x03\x61ny\x18\x14 \x01(\x0b\x32\x16.p2p_validate.AnyRulesH\x00\x12/\n\x08\x64uration\x18\x15 \x01(\x0b\x32\x1b.p2p_validate.DurationRulesH\x00\x12\x31\n\ttimestamp\x18\x16 \x01(\x0b\x32\x1c.p2p_validate.TimestampRulesH\x00\x42\x06\n\x04typeB\n\n\x08_message\"\xf6\x04\n\nFloatRules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x02H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x02H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x02H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x02H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x02H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x02\x12\x0e\n\x06not_in\x18\x07 \x03(\x02\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf7\x04\n\x0b\x44oubleRules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x01H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x01H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x01H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x01H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x01H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x01\x12\x0e\n\x06not_in\x18\x07 \x03(\x01\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf6\x04\n\nInt32Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x05H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x05H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x05H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x05H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x05H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x05\x12\x0e\n\x06not_in\x18\x07 \x03(\x05\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf6\x04\n\nInt64Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x03H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x03H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x03H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x03H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x03H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x03\x12\x0e\n\x06not_in\x18\x07 \x03(\x03\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf7\x04\n\x0bUInt32Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\rH\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\rH\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\rH\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\rH\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\rH\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\r\x12\x0e\n\x06not_in\x18\x07 \x03(\r\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf7\x04\n\x0bUInt64Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x04H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x04H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x04H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x04H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x04H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x04\x12\x0e\n\x06not_in\x18\x07 \x03(\x04\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf7\x04\n\x0bSInt32Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x11H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x11H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x11H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x11H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x11H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x11\x12\x0e\n\x06not_in\x18\x07 \x03(\x11\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf7\x04\n\x0bSInt64Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x12H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x12H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x12H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x12H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x12H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x12\x12\x0e\n\x06not_in\x18\x07 \x03(\x12\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf8\x04\n\x0c\x46ixed32Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x07H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x07H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x07H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x07H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x07H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x07\x12\x0e\n\x06not_in\x18\x07 \x03(\x07\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf8\x04\n\x0c\x46ixed64Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x06H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x06H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x06H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x06H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x06H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x06\x12\x0e\n\x06not_in\x18\x07 \x03(\x06\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf9\x04\n\rSFixed32Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x0fH\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x0fH\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x0fH\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x0fH\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x0fH\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x0f\x12\x0e\n\x06not_in\x18\x07 \x03(\x0f\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf9\x04\n\rSFixed64Rules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x10H\x02\x88\x01\x01\x12\x0f\n\x02lt\x18\x02 \x01(\x10H\x03\x88\x01\x01\x12\x0f\n\x02le\x18\x03 \x01(\x10H\x04\x88\x01\x01\x12\x0f\n\x02gt\x18\x04 \x01(\x10H\x05\x88\x01\x01\x12\x0f\n\x02ge\x18\x05 \x01(\x10H\x06\x88\x01\x01\x12\n\n\x02in\x18\x06 \x03(\x10\x12\x0e\n\x06not_in\x18\x07 \x03(\x10\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x0e \x01(\x02H\n\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x0b\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0e\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\x96\x03\n\tBoolRules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x08H\x01\x88\x01\x01\x12\x13\n\x06\x65nable\x18\x02 \x01(\x08H\x02\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\x08H\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x14\n\x07\x65xample\x18\x07 \x01(\x08H\x05\x88\x01\x01\x12\x12\n\x05\x66ield\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x11\n\x04type\x18\t \x01(\tH\x07\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\x08\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\t\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x08\n\x06_constB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\n\n\x08_exampleB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xc8\x07\n\x0bStringRules\x12\x12\n\x05\x63onst\x18\x01 \x01(\tH\x03\x88\x01\x01\x12\x10\n\x03len\x18\x02 \x01(\x04H\x04\x88\x01\x01\x12\x17\n\nmin_length\x18\x03 \x01(\x04H\x05\x88\x01\x01\x12\x17\n\nmax_length\x18\x04 \x01(\x04H\x06\x88\x01\x01\x12\x14\n\x07pattern\x18\x05 \x01(\tH\x07\x88\x01\x01\x12\x13\n\x06prefix\x18\x06 \x01(\tH\x08\x88\x01\x01\x12\x13\n\x06suffix\x18\x07 \x01(\tH\t\x88\x01\x01\x12\x15\n\x08\x63ontains\x18\x08 \x01(\tH\n\x88\x01\x01\x12\x19\n\x0cnot_contains\x18\t \x01(\tH\x0b\x88\x01\x01\x12\n\n\x02in\x18\n \x03(\t\x12\x0e\n\x06not_in\x18\x0b \x03(\t\x12\x0f\n\x05\x65mail\x18\x0c \x01(\x08H\x00\x12\x12\n\x08hostname\x18\r \x01(\x08H\x00\x12\x0c\n\x02ip\x18\x0e \x01(\x08H\x00\x12\x0e\n\x04ipv4\x18\x0f \x01(\x08H\x00\x12\x0e\n\x04ipv6\x18\x10 \x01(\x08H\x00\x12\r\n\x03uri\x18\x11 \x01(\x08H\x00\x12\x11\n\x07uri_ref\x18\x12 \x01(\x08H\x00\x12\x11\n\x07\x61\x64\x64ress\x18\x15 \x01(\x08H\x00\x12\x0e\n\x04uuid\x18\x16 \x01(\x08H\x00\x12\x17\n\rpydantic_type\x18\x63 \x01(\tH\x00\x12\x13\n\x06\x65nable\x18\x17 \x01(\x08H\x0c\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\x18 \x01(\tH\x01\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\x19 \x01(\tH\x01\x12\x16\n\x0cmiss_default\x18\x1a \x01(\x08H\x01\x12\x12\n\x08required\x18# \x01(\x08H\x01\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18$ \x01(\tH\x01\x12\x12\n\x05\x61lias\x18\x1b \x01(\tH\r\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x1c \x01(\tH\x0e\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x1e \x01(\tH\x02\x12\x19\n\x0f\x65xample_factory\x18\x1f \x01(\tH\x02\x12\x12\n\x05\x66ield\x18  \x01(\tH\x0f\x88\x01\x01\x12\x11\n\x04type\x18! \x01(\tH\x10\x88\x01\x01\x12\x12\n\x05title\x18\" \x01(\tH\x11\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x12\x88\x01\x01\x42\x0c\n\nwell_knownB\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x06\n\x04_lenB\r\n\x0b_min_lengthB\r\n\x0b_max_lengthB\n\n\x08_patternB\t\n\x07_prefixB\t\n\x07_suffixB\x0b\n\t_containsB\x0f\n\r_not_containsB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\x86\x06\n\nBytesRules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x0cH\x03\x88\x01\x01\x12\x17\n\nmin_length\x18\x02 \x01(\x04H\x04\x88\x01\x01\x12\x17\n\nmax_length\x18\x03 \x01(\x04H\x05\x88\x01\x01\x12\x13\n\x06prefix\x18\x05 \x01(\x0cH\x06\x88\x01\x01\x12\x13\n\x06suffix\x18\x06 \x01(\x0cH\x07\x88\x01\x01\x12\x15\n\x08\x63ontains\x18\x07 \x01(\x0cH\x08\x88\x01\x01\x12\n\n\x02in\x18\x08 \x03(\x0c\x12\x0e\n\x06not_in\x18\t \x03(\x0c\x12\x13\n\x06\x65nable\x18\n \x01(\x08H\t\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\x0b \x01(\x0cH\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\x0c \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\r \x01(\x08H\x00\x12\x12\n\x08required\x18\x1a \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18$ \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0e \x01(\tH\n\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x0f \x01(\tH\x0b\x88\x01\x01\x12\x18\n\x0bmultiple_of\x18\x10 \x01(\x02H\x0c\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x11 \x01(\x0cH\x01\x12\x19\n\x0f\x65xample_factory\x18\x12 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x13 \x01(\tH\r\x88\x01\x01\x12\x11\n\x04type\x18\x14 \x01(\tH\x0e\x88\x01\x01\x12\x0c\n\x02ip\x18\x15 \x01(\x08H\x02\x12\x0e\n\x04ipv4\x18\x16 \x01(\x08H\x02\x12\x0e\n\x04ipv6\x18\x17 \x01(\x08H\x02\x12\x12\n\x05title\x18\x18 \x01(\tH\x0f\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x19 \x01(\tH\x10\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x0c\n\nwell_knownB\x08\n\x06_constB\r\n\x0b_min_lengthB\r\n\x0b_max_lengthB\t\n\x07_prefixB\t\n\x07_suffixB\x0b\n\t_containsB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x0e\n\x0c_multiple_ofB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xcf\x03\n\tEnumRules\x12\x12\n\x05\x63onst\x18\x01 \x01(\x05H\x02\x88\x01\x01\x12\n\n\x02in\x18\x03 \x03(\x05\x12\x0e\n\x06not_in\x18\x04 \x03(\x05\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x03\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x05H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\x05\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x05H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x06\x88\x01\x01\x12\x12\n\x05title\x18\x12 \x01(\tH\x07\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x08\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x08\n\x06_titleB\x08\n\x06_extra\"\xd0\x03\n\x0cMessageRules\x12\x11\n\x04skip\x18\x01 \x01(\x08H\x02\x88\x01\x01\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x03\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x02H\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x02 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\x05\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0f \x01(\x02H\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\x06\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x07\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\x08\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\t\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x07\n\x05_skipB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xb3\x04\n\rRepeatedRules\x12\x16\n\tmin_items\x18\x01 \x01(\x04H\x02\x88\x01\x01\x12\x16\n\tmax_items\x18\x02 \x01(\x04H\x03\x88\x01\x01\x12\x13\n\x06unique\x18\x03 \x01(\x08H\x04\x88\x01\x01\x12,\n\x05items\x18\x04 \x01(\x0b\x32\x18.p2p_validate.FieldRulesH\x05\x88\x01\x01\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x06\x88\x01\x01\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x07\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\x08\x88\x01\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\t\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\n\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\x0b\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0c\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x0c\n\n_min_itemsB\x0c\n\n_max_itemsB\t\n\x07_uniqueB\x08\n\x06_itemsB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xc6\x04\n\x08MapRules\x12\x16\n\tmin_pairs\x18\x01 \x01(\x04H\x02\x88\x01\x01\x12\x16\n\tmax_pairs\x18\x02 \x01(\x04H\x03\x88\x01\x01\x12+\n\x04keys\x18\x04 \x01(\x0b\x32\x18.p2p_validate.FieldRulesH\x04\x88\x01\x01\x12-\n\x06values\x18\x05 \x01(\x0b\x32\x18.p2p_validate.FieldRulesH\x05\x88\x01\x01\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x06\x88\x01\x01\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x15 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x07\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\x08\x88\x01\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\t\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\n\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\x0b\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x0c\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x0c\n\n_min_pairsB\x0c\n\n_max_pairsB\x07\n\x05_keysB\t\n\x07_valuesB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xb0\x03\n\x08\x41nyRules\x12\n\n\x02in\x18\x02 \x03(\t\x12\x0e\n\x06not_in\x18\x03 \x03(\t\x12\x13\n\x06\x65nable\x18\x08 \x01(\x08H\x02\x88\x01\x01\x12\x11\n\x07\x64\x65\x66\x61ult\x18\t \x01(\tH\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x01 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\x04\x88\x01\x01\x12\x11\n\x07\x65xample\x18\x0e \x01(\tH\x01\x12\x19\n\x0f\x65xample_factory\x18\x0f \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x10 \x01(\tH\x05\x88\x01\x01\x12\x12\n\x05title\x18\x11 \x01(\tH\x06\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\x07\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x08\n\x06_titleB\x08\n\x06_extra\"\xc2\x06\n\rDurationRules\x12-\n\x05\x63onst\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x02\x88\x01\x01\x12*\n\x02lt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationH\x03\x88\x01\x01\x12*\n\x02le\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationH\x04\x88\x01\x01\x12*\n\x02gt\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationH\x05\x88\x01\x01\x12*\n\x02ge\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationH\x06\x88\x01\x01\x12%\n\x02in\x18\x07 \x03(\x0b\x32\x19.google.protobuf.Duration\x12)\n\x06not_in\x18\x08 \x03(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x06\x65nable\x18\x0e \x01(\x08H\x07\x88\x01\x01\x12,\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\n \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\x0b \x01(\x08H\x00\x12\x12\n\x08required\x18\x01 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0c \x01(\tH\x08\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\t\x88\x01\x01\x12,\n\x07\x65xample\x18\x0f \x01(\x0b\x32\x19.google.protobuf.DurationH\x01\x12\x19\n\x0f\x65xample_factory\x18\x10 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x11 \x01(\tH\n\x88\x01\x01\x12\x11\n\x04type\x18\x12 \x01(\tH\x0b\x88\x01\x01\x12\x12\n\x05title\x18\x13 \x01(\tH\x0c\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x14 \x01(\tH\r\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra\"\xf3\x06\n\x0eTimestampRules\x12.\n\x05\x63onst\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x12+\n\x02lt\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x03\x88\x01\x01\x12+\n\x02le\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x04\x88\x01\x01\x12+\n\x02gt\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x05\x88\x01\x01\x12+\n\x02ge\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x06\x88\x01\x01\x12\x13\n\x06lt_now\x18\x07 \x01(\x08H\x07\x88\x01\x01\x12\x13\n\x06gt_now\x18\x08 \x01(\x08H\x08\x88\x01\x01\x12.\n\x06within\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationH\t\x88\x01\x01\x12\x13\n\x06\x65nable\x18\n \x01(\x08H\n\x88\x01\x01\x12-\n\x07\x64\x65\x66\x61ult\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x19\n\x0f\x64\x65\x66\x61ult_factory\x18\x0c \x01(\tH\x00\x12\x16\n\x0cmiss_default\x18\r \x01(\x08H\x00\x12\x12\n\x08required\x18\x01 \x01(\x08H\x00\x12\x1a\n\x10\x64\x65\x66\x61ult_template\x18\x16 \x01(\tH\x00\x12\x12\n\x05\x61lias\x18\x0e \x01(\tH\x0b\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x0f \x01(\tH\x0c\x88\x01\x01\x12-\n\x07\x65xample\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x12\x19\n\x0f\x65xample_factory\x18\x11 \x01(\tH\x01\x12\x12\n\x05\x66ield\x18\x12 \x01(\tH\r\x88\x01\x01\x12\x11\n\x04type\x18\x13 \x01(\tH\x0e\x88\x01\x01\x12\x12\n\x05title\x18\x14 \x01(\tH\x0f\x88\x01\x01\x12\x12\n\x05\x65xtra\x18\x15 \x01(\tH\x10\x88\x01\x01\x42\x10\n\x0e\x64\x65\x66\x61ult_configB\x10\n\x0e\x65xample_configB\x08\n\x06_constB\x05\n\x03_ltB\x05\n\x03_leB\x05\n\x03_gtB\x05\n\x03_geB\t\n\x07_lt_nowB\t\n\x07_gt_nowB\t\n\x07_withinB\t\n\x07_enableB\x08\n\x06_aliasB\x0e\n\x0c_descriptionB\x08\n\x06_fieldB\x07\n\x05_typeB\x08\n\x06_titleB\x08\n\x06_extra:4\n\x07ignored\x12\x1f.google.protobuf.MessageOptions\x18\xb1\x08 \x01(\x08\x88\x01\x01:3\n\x08required\x12\x1d.google.protobuf.OneofOptions\x18\xb1\x08 \x01(\x08\x88\x01\x01:Q\n\x0coneof_extend\x12\x1d.google.protobuf.OneofOptions\x18\xb2\x08 \x01(\x0b\x32\x18.p2p_validate.OneofRules\x88\x01\x01:J\n\x05rules\x12\x1d.google.protobuf.FieldOptions\x18\xb1\x08 \x01(\x0b\x32\x18.p2p_validate.FieldRules\x88\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.p2p_validate_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(ignored)
  google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(required)
  google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof_extend)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(rules)

  DESCRIPTOR._options = None
  _ONEOFRULES._serialized_start=142
  _ONEOFRULES._serialized_end=172
  _FIELDRULES._serialized_start=175
  _FIELDRULES._serialized_end=1200
  _FLOATRULES._serialized_start=1203
  _FLOATRULES._serialized_end=1833
  _DOUBLERULES._serialized_start=1836
  _DOUBLERULES._serialized_end=2467
  _INT32RULES._serialized_start=2470
  _INT32RULES._serialized_end=3100
  _INT64RULES._serialized_start=3103
  _INT64RULES._serialized_end=3733
  _UINT32RULES._serialized_start=3736
  _UINT32RULES._serialized_end=4367
  _UINT64RULES._serialized_start=4370
  _UINT64RULES._serialized_end=5001
  _SINT32RULES._serialized_start=5004
  _SINT32RULES._serialized_end=5635
  _SINT64RULES._serialized_start=5638
  _SINT64RULES._serialized_end=6269
  _FIXED32RULES._serialized_start=6272
  _FIXED32RULES._serialized_end=6904
  _FIXED64RULES._serialized_start=6907
  _FIXED64RULES._serialized_end=7539
  _SFIXED32RULES._serialized_start=7542
  _SFIXED32RULES._serialized_end=8175
  _SFIXED64RULES._serialized_start=8178
  _SFIXED64RULES._serialized_end=8811
  _BOOLRULES._serialized_start=8814
  _BOOLRULES._serialized_end=9220
  _STRINGRULES._serialized_start=9223
  _STRINGRULES._serialized_end=10191
  _BYTESRULES._serialized_start=10194
  _BYTESRULES._serialized_end=10968
  _ENUMRULES._serialized_start=10971
  _ENUMRULES._serialized_end=11434
  _MESSAGERULES._serialized_start=11437
  _MESSAGERULES._serialized_end=11901
  _REPEATEDRULES._serialized_start=11904
  _REPEATEDRULES._serialized_end=12467
  _MAPRULES._serialized_start=12470
  _MAPRULES._serialized_end=13052
  _ANYRULES._serialized_start=13055
  _ANYRULES._serialized_end=13487
  _DURATIONRULES._serialized_start=13490
  _DURATIONRULES._serialized_end=14324
  _TIMESTAMPRULES._serialized_start=14327
  _TIMESTAMPRULES._serialized_end=15210
# @@protoc_insertion_point(module_scope)
