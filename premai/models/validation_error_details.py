from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.validation_error_details_additional_property import ValidationErrorDetailsAdditionalProperty

T = TypeVar("T", bound="ValidationErrorDetails")


class ValidationErrorDetailsDict(TypedDict):
    pass


@_attrs_define
class ValidationErrorDetails:
    """Detailed information about the validation errors."""

    additional_properties: Dict[str, "ValidationErrorDetailsAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_error_details_additional_property import ValidationErrorDetailsAdditionalProperty

        d = src_dict.copy()
        validation_error_details = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ValidationErrorDetailsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        validation_error_details.additional_properties = additional_properties
        return validation_error_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ValidationErrorDetailsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ValidationErrorDetailsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
