from typing import Any


def get_first_item(items: list[Any], default=None) -> Any:
    return items[0] if items else default
