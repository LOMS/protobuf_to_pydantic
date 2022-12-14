# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

import datetime
import typing

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.util import Timedelta
from pydantic import BaseModel
from pydantic.fields import FieldInfo


class FieldRules(BaseModel):

    message: "MessageRules" = FieldInfo()
    float: "FloatRules" = FieldInfo()
    double: "DoubleRules" = FieldInfo()
    int32: "Int32Rules" = FieldInfo()
    int64: "Int64Rules" = FieldInfo()
    uint32: "UInt32Rules" = FieldInfo()
    uint64: "UInt64Rules" = FieldInfo()
    sint32: "SInt32Rules" = FieldInfo()
    sint64: "SInt64Rules" = FieldInfo()
    fixed32: "Fixed32Rules" = FieldInfo()
    fixed64: "Fixed64Rules" = FieldInfo()
    sfixed32: "SFixed32Rules" = FieldInfo()
    sfixed64: "SFixed64Rules" = FieldInfo()
    bool: "BoolRules" = FieldInfo()
    string: "StringRules" = FieldInfo()
    bytes: "BytesRules" = FieldInfo()
    enum: "EnumRules" = FieldInfo()
    repeated: "RepeatedRules" = FieldInfo()
    map: "MapRules" = FieldInfo()
    any: "AnyRules" = FieldInfo()
    duration: "DurationRules" = FieldInfo()
    timestamp: "TimestampRules" = FieldInfo()


class FloatRules(BaseModel):

    const: float = FieldInfo(default=0.0)
    lt: float = FieldInfo(default=0.0)
    le: float = FieldInfo(default=0.0)
    gt: float = FieldInfo(default=0.0)
    ge: float = FieldInfo(default=0.0)
    not_in: typing.List[float] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class DoubleRules(BaseModel):

    const: float = FieldInfo(default=0.0)
    lt: float = FieldInfo(default=0.0)
    le: float = FieldInfo(default=0.0)
    gt: float = FieldInfo(default=0.0)
    ge: float = FieldInfo(default=0.0)
    not_in: typing.List[float] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class Int32Rules(BaseModel):

    const: int = FieldInfo(default=0)
    lt: int = FieldInfo(default=0)
    le: int = FieldInfo(default=0)
    gt: int = FieldInfo(default=0)
    ge: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class Int64Rules(BaseModel):

    const: int = FieldInfo(default=0)
    lt: int = FieldInfo(default=0)
    le: int = FieldInfo(default=0)
    gt: int = FieldInfo(default=0)
    ge: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class UInt32Rules(BaseModel):

    const: int = FieldInfo(default=0)
    lt: int = FieldInfo(default=0)
    le: int = FieldInfo(default=0)
    gt: int = FieldInfo(default=0)
    ge: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class UInt64Rules(BaseModel):

    const: int = FieldInfo(default=0)
    lt: int = FieldInfo(default=0)
    le: int = FieldInfo(default=0)
    gt: int = FieldInfo(default=0)
    ge: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class SInt32Rules(BaseModel):

    const: int = FieldInfo(default=0)
    lt: int = FieldInfo(default=0)
    le: int = FieldInfo(default=0)
    gt: int = FieldInfo(default=0)
    ge: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class SInt64Rules(BaseModel):

    const: int = FieldInfo(default=0)
    lt: int = FieldInfo(default=0)
    le: int = FieldInfo(default=0)
    gt: int = FieldInfo(default=0)
    ge: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class Fixed32Rules(BaseModel):

    const: float = FieldInfo(default=0.0)
    lt: float = FieldInfo(default=0.0)
    le: float = FieldInfo(default=0.0)
    gt: float = FieldInfo(default=0.0)
    ge: float = FieldInfo(default=0.0)
    not_in: typing.List[float] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class Fixed64Rules(BaseModel):

    const: float = FieldInfo(default=0.0)
    lt: float = FieldInfo(default=0.0)
    le: float = FieldInfo(default=0.0)
    gt: float = FieldInfo(default=0.0)
    ge: float = FieldInfo(default=0.0)
    not_in: typing.List[float] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class SFixed32Rules(BaseModel):

    const: float = FieldInfo(default=0.0)
    lt: float = FieldInfo(default=0.0)
    le: float = FieldInfo(default=0.0)
    gt: float = FieldInfo(default=0.0)
    ge: float = FieldInfo(default=0.0)
    not_in: typing.List[float] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class SFixed64Rules(BaseModel):

    const: float = FieldInfo(default=0.0)
    lt: float = FieldInfo(default=0.0)
    le: float = FieldInfo(default=0.0)
    gt: float = FieldInfo(default=0.0)
    ge: float = FieldInfo(default=0.0)
    not_in: typing.List[float] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class BoolRules(BaseModel):

    const: bool = FieldInfo(default=False)
    enable: bool = FieldInfo(default=False)
    default: bool = FieldInfo(default=False)
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: bool = FieldInfo(default=False)
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class StringRules(BaseModel):

    const: str = FieldInfo(default="")
    len: int = FieldInfo(default=0)
    min_length: int = FieldInfo(default=0)
    max_length: int = FieldInfo(default=0)
    pattern: str = FieldInfo(default="")
    prefix: str = FieldInfo(default="")
    suffix: str = FieldInfo(default="")
    contains: str = FieldInfo(default="")
    not_contains: str = FieldInfo(default="")
    not_in: typing.List[str] = FieldInfo(default_factory=list)
    email: bool = FieldInfo(default=False)
    hostname: bool = FieldInfo(default=False)
    ip: bool = FieldInfo(default=False)
    ipv4: bool = FieldInfo(default=False)
    ipv6: bool = FieldInfo(default=False)
    uri: bool = FieldInfo(default=False)
    uri_ref: bool = FieldInfo(default=False)
    address: bool = FieldInfo(default=False)
    uuid: bool = FieldInfo(default=False)
    pydantic_type: str = FieldInfo(default="")
    enable: bool = FieldInfo(default=False)
    default: str = FieldInfo(default="")
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: str = FieldInfo(default="")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class BytesRules(BaseModel):

    const: bytes = FieldInfo(default=b"")
    min_length: int = FieldInfo(default=0)
    max_length: int = FieldInfo(default=0)
    prefix: bytes = FieldInfo(default=b"")
    suffix: bytes = FieldInfo(default=b"")
    contains: bytes = FieldInfo(default=b"")
    not_in: typing.List[bytes] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: bytes = FieldInfo(default=b"")
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    multiple_of: float = FieldInfo(default=0.0)
    example: bytes = FieldInfo(default=b"")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    ip: bool = FieldInfo(default=False)
    ipv4: bool = FieldInfo(default=False)
    ipv6: bool = FieldInfo(default=False)
    title: str = FieldInfo(default="")


class EnumRules(BaseModel):

    const: int = FieldInfo(default=0)
    not_in: typing.List[int] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: int = FieldInfo(default=0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: int = FieldInfo(default=0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class MessageRules(BaseModel):

    skip: bool = FieldInfo(default=False)
    required: bool = FieldInfo(default=False)
    enable: bool = FieldInfo(default=False)
    default: float = FieldInfo(default=0.0)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: float = FieldInfo(default=0.0)
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class RepeatedRules(BaseModel):

    min_items: int = FieldInfo(default=0)
    max_items: int = FieldInfo(default=0)
    unique: bool = FieldInfo(default=False)
    items: "FieldRules" = FieldInfo()
    enable: bool = FieldInfo(default=False)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class MapRules(BaseModel):

    min_pairs: int = FieldInfo(default=0)
    max_pairs: int = FieldInfo(default=0)
    keys: "FieldRules" = FieldInfo()
    values: "FieldRules" = FieldInfo()
    enable: bool = FieldInfo(default=False)
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class AnyRules(BaseModel):

    required: bool = FieldInfo(default=False)
    not_in: typing.List[str] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: str = FieldInfo(default="")
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: str = FieldInfo(default="")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class DurationRules(BaseModel):

    const: Timedelta = FieldInfo(default_factory="Timedelta")
    lt: Timedelta = FieldInfo(default_factory="Timedelta")
    le: Timedelta = FieldInfo(default_factory="Timedelta")
    gt: Timedelta = FieldInfo(default_factory="Timedelta")
    ge: Timedelta = FieldInfo(default_factory="Timedelta")
    not_in: typing.List[Timedelta] = FieldInfo(default_factory=list)
    enable: bool = FieldInfo(default=False)
    default: Timedelta = FieldInfo(default_factory="Timedelta")
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: Timedelta = FieldInfo(default_factory="Timedelta")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")


class TimestampRules(BaseModel):

    const: datetime.datetime = FieldInfo(default_factory="now")
    lt: datetime.datetime = FieldInfo(default_factory="now")
    le: datetime.datetime = FieldInfo(default_factory="now")
    gt: datetime.datetime = FieldInfo(default_factory="now")
    ge: datetime.datetime = FieldInfo(default_factory="now")
    lt_now: bool = FieldInfo(default=False)
    gt_now: bool = FieldInfo(default=False)
    within: Timedelta = FieldInfo(default_factory="Timedelta")
    enable: bool = FieldInfo(default=False)
    default: datetime.datetime = FieldInfo(default_factory="now")
    default_factory: str = FieldInfo(default="")
    miss_default: bool = FieldInfo(default=False)
    alias: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    example: datetime.datetime = FieldInfo(default_factory="now")
    example_factory: str = FieldInfo(default="")
    field: str = FieldInfo(default="")
    type: str = FieldInfo(default="")
    title: str = FieldInfo(default="")
