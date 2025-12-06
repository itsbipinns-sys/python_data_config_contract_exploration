from dataclasses import fields
from typing import Type, Any, Dict

def map_to_dataclass(dataclass_type: Type, input_dict: Dict[str, Any], key_map: Dict[str, str]) -> Any:
    """
    Generic mapper: creates a dataclass instance from input_dict using key_map.
    key_map: {dataclass_field: input_dict_key}
    """
    filtered = {
        f.name: input_dict[key_map[f.name]]
        for f in fields(dataclass_type)
        if key_map.get(f.name) in input_dict
    }
    return dataclass_type(**filtered)
