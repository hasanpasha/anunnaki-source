from pydantic import BaseModel, RootModel
from typing import Any, List


class Filter(BaseModel):
    name: str
    state: Any

class FilterList(RootModel):
    root: List[Filter]
