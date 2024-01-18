from typing import Literal

current_ID: int = 0


def get_new_id() -> int:
    global current_ID
    id_ = current_ID
    current_ID += 1
    return id_


class Info:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 gender: Literal["male", "female", "other"],
                 other: str | None = None) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.gender: Literal["male", "female", "other"] = gender
        self.other_gender: str | None = other if gender == "other" else None

        self.ID: int = get_new_id()


