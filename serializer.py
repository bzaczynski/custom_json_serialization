import importlib
import json
from typing import Any


def to_json(instance: Any, indent=4) -> str:
    """Serialize a custom object to JSON."""
    return json.dumps(instance, default=_serialize, indent=indent)


def from_json(json_text: str) -> Any:
    """Deserialize a custom object from JSON."""
    return json.loads(json_text, object_hook=_deserialize)


def _fqn(instance: Any) -> str:
    """Return a fully-qualified name of the object's type."""
    module_name = type(instance).__module__
    class_name = type(instance).__name__
    return f"{module_name}.{class_name}"


def _import_type(fqn: str) -> type:
    """Return a class object based on its fully-qualified name."""
    names = fqn.split(".")
    module_name, class_name = ".".join(names[:-1]), names[-1]
    module = importlib.import_module(module_name, ".")
    return getattr(module, class_name)


def _serialize(value: Any) -> Any:
    if hasattr(value, "__json__"):
        fields = value.__json__()
    elif hasattr(value, "__dict__"):
        fields = {k: _serialize(v) for k, v in vars(value).items()}
    else:
        return value
    metadata = {"__type__": _fqn(value)}
    return fields | metadata


def _deserialize(value) -> Any:
    if isinstance(value, dict) and "__type__" in value:
        type_ = _import_type(value.pop("__type__"))
        return type_(**{k: _deserialize(v) for k, v in value.items()})
    return value
