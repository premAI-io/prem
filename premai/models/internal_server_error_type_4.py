from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.internal_server_error_type_4_code import InternalServerErrorType4Code

T = TypeVar("T", bound="InternalServerErrorType4")


class InternalServerErrorType4Dict(TypedDict):
    message: str
    code: InternalServerErrorType4Code
    pass


@_attrs_define
class InternalServerErrorType4:
    """
    Attributes:
        message (str):
        code (InternalServerErrorType4Code): * `ProviderAPIConnectionError` - ProviderAPIConnectionError
    """

    message: str
    code: InternalServerErrorType4Code

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        code = self.code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        code = InternalServerErrorType4Code(d.pop("code"))

        internal_server_error_type_4 = cls(
            message=message,
            code=code,
        )

        internal_server_error_type_4.additional_properties = d
        return internal_server_error_type_4

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
