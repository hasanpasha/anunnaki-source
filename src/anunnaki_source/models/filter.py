from abc import ABC
from typing import Any


class Filter(ABC):
    name: str
    state: Any
