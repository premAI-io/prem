from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="V1ChatCompletionsCreateJsonBodyResponseFormatType0")


class V1ChatCompletionsCreateJsonBodyResponseFormatType0Dict(TypedDict):
    pass


@_attrs_define
class V1ChatCompletionsCreateJsonBodyResponseFormatType0:
    """An object specifying the format that the model must output."""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        v1_chat_completions_create_json_body_response_format_type_0 = cls()

        v1_chat_completions_create_json_body_response_format_type_0.additional_properties = d
        return v1_chat_completions_create_json_body_response_format_type_0

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
