from anunnaki_source.models.filter import Filter
from dataclasses import dataclass


class TextEntry(Filter):
    name: str
    state: str
