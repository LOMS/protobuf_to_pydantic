from datetime import datetime, timedelta
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Type, TypeVar, Union

from annotated_types import Ge, Gt, Le, Lt, MaxLen, MinLen, MultipleOf, Predicate
from pydantic import AfterValidator
from pydantic._internal._fields import PydanticGeneralMetadata
from pydantic.types import AllowInfNan, AnyItemType, PydanticUserError, Strict
from typing_extensions import Annotated

from protobuf_to_pydantic.customer_validator import rule

__all__ = [
    "conlist",
    "conint",
    "confloat",
    "constr",
    "conbytes",
    "contimedelta",
    "contimestamp",
    "pydantic_con_dict",
    "set_ignore_param_value_tz",
    "TimedeltaType",
    "DatetimeType",
    "gt_now",
    "lt_now",
    "const",
    "in_",
    "not_in",
    "within",
    "ignore_tz_validator",
    "get_origin_code",
]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Like pydantic type ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The source code generated by the construction function of the pydantic type will be more complicated,
# and the corresponding function will be rewritten here to simplify the code generation.
def conlist(
    item_type: Type[AnyItemType],
    *,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    unique_items: Optional[bool] = None,
) -> Type[List[AnyItemType]]:
    """A wrapper around typing.List that adds validation.

    Args:
        item_type: The type of the items in the list.
        min_length: The minimum length of the list. Defaults to None.
        max_length: The maximum length of the list. Defaults to None.
        unique_items: Whether the items in the list must be unique. Defaults to None.

    Returns:
        The wrapped list type.
    """
    if unique_items is not None:
        raise PydanticUserError(
            (
                "`unique_items` is removed, use `Set` instead"
                "(this feature is discussed in https://github.com/pydantic/pydantic-core/issues/296)"
            ),
            code="removed-kwargs",
        )
    type_param = [List[item_type]]
    if min_length is not None:
        type_param.append(MinLen(min_length))
    if max_length is not None:
        type_param.append(MaxLen(max_length))
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))

    return List[item_type]


def conint(
    *,
    strict: Optional[bool] = None,
    gt: Optional[int] = None,
    ge: Optional[int] = None,
    lt: Optional[int] = None,
    le: Optional[int] = None,
    multiple_of: Optional[int] = None,
) -> Type[int]:
    """A wrapper around `int` that allows for additional constraints.

    Args:
        strict: Whether to validate the integer in strict mode. Defaults to `None`.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.

    Returns:
        The wrapped integer type.
    """
    type_param = [int]
    if strict is not None:
        type_param.append(Strict(strict))
    if gt is not None:
        type_param.append(Gt(gt))
    if ge is not None:
        type_param.append(Ge(ge))
    if lt is not None:
        type_param.append(Lt(lt))
    if le is not None:
        type_param.append(Le(le))
    if multiple_of is not None:
        type_param.append(MultipleOf(multiple_of))
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))
    return int


def confloat(
    *,
    strict: Optional[bool] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    multiple_of: Optional[float] = None,
    allow_inf_nan: Optional[bool] = None,
) -> Type[float]:
    """A wrapper around `float` that allows for additional constraints.

    Args:
        strict: Whether to validate the float in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.
        allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`.

    Returns:
        The wrapped float type.
    """
    type_param = [float]
    if strict is not None:
        type_param.append(Strict(strict))
    if gt is not None:
        type_param.append(Gt(gt))
    if ge is not None:
        type_param.append(Ge(ge))
    if lt is not None:
        type_param.append(Lt(lt))
    if le is not None:
        type_param.append(Le(le))
    if multiple_of is not None:
        type_param.append(MultipleOf(multiple_of))
    if allow_inf_nan is not None:
        type_param.append(AllowInfNan(allow_inf_nan))
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))
    return float


def conbytes(
    *,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    strict: Optional[bool] = None,
) -> Type[bytes]:
    """A wrapper around `bytes` that allows for additional constraints.

    Args:
        min_length: The minimum length of the bytes.
        max_length: The maximum length of the bytes.
        strict: Whether to validate the bytes in strict mode.

    Returns:
        The wrapped bytes type.
    """
    type_param = [bytes]
    if strict is not None:
        type_param.append(Strict(strict))
    if min_length is not None:
        type_param.append(MinLen(min_length))
    if max_length is not None:
        type_param.append(MaxLen(max_length))
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))
    return bytes


def constr(
    *,
    strip_whitespace: Optional[bool] = None,
    to_upper: Optional[bool] = None,
    to_lower: Optional[bool] = None,
    strict: Optional[bool] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    pattern: Optional[str] = None,
) -> Type[str]:
    """A wrapper around `str` that allows for additional constraints.

    Args:
        strip_whitespace: Whether to strip whitespace from the string.
        to_upper: Whether to convert the string to uppercase.
        to_lower: Whether to convert the string to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern that the string must match.

    Returns:
        The wrapped string type.
    """
    type_param = [str]
    if strict is not None:
        type_param.append(Strict(strict))
    if min_length is not None:
        type_param.append(MinLen(min_length))
    if max_length is not None:
        type_param.append(MaxLen(max_length))
    if any([strip_whitespace, to_upper, to_lower, pattern]):
        type_param.append(
            PydanticGeneralMetadata(
                strip_whitespace=strip_whitespace,
                to_upper=to_upper,
                to_lower=to_lower,
                pattern=pattern,
            )
        )
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))
    return str


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Base ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DatetimeType = TypeVar("DatetimeType", bound=datetime)
TimedeltaType = TypeVar("TimedeltaType", bound=timedelta)
T = TypeVar("T")


def const(const_v: T) -> Predicate:
    def _const(v: T) -> bool:
        # return v is const_v
        # Throwing an exception makes the error output easier to understand
        rule.timestamp_const_validator(v, "", const_v)
        return True

    return Predicate(_const)


def in_(in_v: Sequence[T]) -> Predicate:
    def _in_(v: T) -> bool:
        rule.in_validator(v, "", in_v)
        return True

    return Predicate(_in_)


def not_in(not_in_v: Sequence[T]) -> Predicate:
    def _not_in(v: T) -> bool:
        rule.not_in_validator(v, "", not_in_v)
        return True

    return Predicate(_not_in)


_ignore_param_value_tz: bool = False


def set_ignore_param_value_tz(result: bool) -> None:
    global _ignore_param_value_tz
    _ignore_param_value_tz = result


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Timedelta TYPE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def contimedelta(
    *,
    duration_const: Optional[timedelta] = None,
    duration_ge: Optional[timedelta] = None,
    duration_gt: Optional[timedelta] = None,
    duration_le: Optional[timedelta] = None,
    duration_lt: Optional[timedelta] = None,
    duration_in: Optional[Sequence[timedelta]] = None,
    duration_not_in: Optional[Sequence[timedelta]] = None,
) -> Type[timedelta]:
    type_param = [TimedeltaType]
    if duration_const is not None:
        type_param.append(const(duration_const))
    if duration_ge is not None:
        type_param.append(Ge(duration_ge))
    if duration_gt is not None:
        type_param.append(Gt(duration_gt))
    if duration_le is not None:
        type_param.append(Le(duration_le))
    if duration_lt is not None:
        type_param.append(Lt(duration_lt))
    if duration_in is not None:
        type_param.append(in_(duration_in))
    if duration_not_in:
        type_param.append(not_in(duration_not_in))
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))  # type: ignore[return-value]
    return timedelta


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Timestamp TYPE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TIMESTAMP_ANT_TYPE = Union[int, float, str, datetime]


def gt_now(v: TIMESTAMP_ANT_TYPE) -> Predicate:
    def _gt_now(_v: TIMESTAMP_ANT_TYPE) -> bool:
        rule.timestamp_gt_now_validator(_v, "", v)
        return True

    return_value = Predicate(_gt_now)
    return return_value


def lt_now(v: TIMESTAMP_ANT_TYPE) -> Predicate:
    def _lt_now(_v: TIMESTAMP_ANT_TYPE) -> bool:
        rule.timestamp_lt_now_validator(_v, "", v)
        return True

    return_value = Predicate(_lt_now)
    return return_value


def within(v: timedelta) -> Predicate:
    def _within(_v: timedelta) -> bool:
        rule.timestamp_within_validator(_v, "", v)
        return True

    return_value = Predicate(_within)
    return return_value


def ignore_tz_validator() -> AfterValidator:
    def _ignore_tz(_v: datetime) -> datetime:
        return _v.replace(tzinfo=None)

    return AfterValidator(_ignore_tz)


def t_ge(v: TIMESTAMP_ANT_TYPE) -> Predicate:
    def _t_ge(_v: TIMESTAMP_ANT_TYPE) -> bool:
        rule.timestamp_ge_validator(_v, "", v)
        return True

    return_value = Predicate(_t_ge)
    return return_value


def t_gt(v: TIMESTAMP_ANT_TYPE) -> Predicate:
    def _t_gt(_v: TIMESTAMP_ANT_TYPE) -> bool:
        rule.timestamp_gt_validator(_v, "", v)
        return True

    return_value = Predicate(_t_gt)
    return return_value


def t_le(v: TIMESTAMP_ANT_TYPE) -> Predicate:
    def _t_le(_v: TIMESTAMP_ANT_TYPE) -> bool:
        rule.timestamp_le_validator(_v, "", v)
        return True

    return_value = Predicate(_t_le)
    return return_value


def t_lt(v: TIMESTAMP_ANT_TYPE) -> Predicate:
    def _t_lt(_v: TIMESTAMP_ANT_TYPE) -> bool:
        rule.timestamp_lt_validator(_v, "", v)
        return True

    return_value = Predicate(_t_lt)
    return return_value


def t_in(in_v: Sequence[TIMESTAMP_ANT_TYPE]) -> Predicate:
    def _t_in(v: T) -> bool:
        rule.timestamp_in_validator(v, "", in_v)
        return True

    return Predicate(_t_in)


def t_not_in(not_in_v: Sequence[TIMESTAMP_ANT_TYPE]) -> Predicate:
    def _t_not_in(v: T) -> bool:
        rule.timestamp_not_in_validator(v, "", not_in_v)
        return True

    return Predicate(_t_not_in)


def contimestamp(
    *,
    timestamp_const: Optional[TIMESTAMP_ANT_TYPE] = None,
    timestamp_ge: Optional[TIMESTAMP_ANT_TYPE] = None,
    timestamp_gt: Optional[TIMESTAMP_ANT_TYPE] = None,
    timestamp_gt_now: Optional[Union[bool, Callable[[], TIMESTAMP_ANT_TYPE]]] = None,
    timestamp_le: Optional[TIMESTAMP_ANT_TYPE] = None,
    timestamp_lt: Optional[TIMESTAMP_ANT_TYPE] = None,
    timestamp_lt_now: Optional[Union[bool, Callable[[], TIMESTAMP_ANT_TYPE]]] = None,
    timestamp_in: Optional[Sequence[TIMESTAMP_ANT_TYPE]] = None,
    timestamp_not_in: Optional[Sequence[TIMESTAMP_ANT_TYPE]] = None,
    timestamp_within: Optional[timedelta] = None,
    ignore_tz: bool = False,
) -> Type[datetime]:
    type_param = [DatetimeType]
    if ignore_tz:
        type_param.append(ignore_tz_validator())
    if timestamp_const is not None:
        type_param.append(const(timestamp_const))
    if timestamp_ge is not None:
        type_param.append(t_ge(timestamp_ge))
    if timestamp_gt is not None:
        type_param.append(t_gt(timestamp_gt))
    if timestamp_gt_now is not None:
        type_param.append(gt_now(timestamp_gt_now))
    if timestamp_le is not None:
        type_param.append(t_le(timestamp_le))
    if timestamp_lt is not None:
        type_param.append(t_lt(timestamp_lt))
    if timestamp_lt_now:
        type_param.append(lt_now(timestamp_lt_now))
    if timestamp_in is not None:
        type_param.append(t_in(timestamp_in))
    if timestamp_not_in:
        type_param.append(t_not_in(timestamp_not_in))
    if timestamp_within:
        type_param.append(within(timestamp_within))
    if len(type_param) > 1:
        return Annotated.__class_getitem__(tuple(type_param))  # type: ignore[return-value]
    return datetime


pydantic_con_dict: Dict[Type, Callable] = {}


def get_origin_code(type_: Predicate) -> Optional[Tuple[str, str, List[str]]]:
    if not isinstance(type_, Predicate):
        return None
    closure = getattr(type_.func, "__closure__", None)
    if type_.func.__module__ == __name__ and closure:
        type_name = type_.func.__name__[1:]
        return __name__, type_name, [i.cell_contents for i in closure]
    return None
