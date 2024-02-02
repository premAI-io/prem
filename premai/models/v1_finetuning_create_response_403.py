from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.v1_finetuning_create_response_403_code import V1FinetuningCreateResponse403Code

T = TypeVar("T", bound="V1FinetuningCreateResponse403")


class V1FinetuningCreateResponse403Dict(TypedDict):
    message: str
    code: V1FinetuningCreateResponse403Code
    pass


@_attrs_define
class V1FinetuningCreateResponse403:
    """
    Attributes:
        message (str):
        code (V1FinetuningCreateResponse403Code): * `PermissionDeniedError` - PermissionDeniedError
    """

    message: str
    code: V1FinetuningCreateResponse403Code

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

        code = V1FinetuningCreateResponse403Code(d.pop("code"))

        v1_finetuning_create_response_403 = cls(
            message=message,
            code=code,
        )

        v1_finetuning_create_response_403.additional_properties = d
        return v1_finetuning_create_response_403

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
