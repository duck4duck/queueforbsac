from typing import Any

from pydantic import ValidationError

from app.core.schemas.protocol_schemas import (
    AddUserAction,
    RemoveUserAction,
    SubscribeUserAction,
    UnsubscribeUserAction,
    SwapUserAction,
)

AVAILABLE_ACTIONS = {
    "add": AddUserAction,
    "remove": RemoveUserAction,
    "subscribe": SubscribeUserAction,
    "unsubscribe": UnsubscribeUserAction,
    "swap": SwapUserAction,
}


def data_validate(raw_data: dict[str, Any]):
    if raw_data.get("type") not in AVAILABLE_ACTIONS:
        raise ValueError(f"Invalid type '{raw_data.get('type')}'")
    action_schema = AVAILABLE_ACTIONS[raw_data.get("type")]
    validated_data = action_schema.model_validate(raw_data)
    return validated_data
