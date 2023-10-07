from typing import List
from anunnaki_source.models.episode import Episode
from pydantic import BaseModel, RootModel


class Season(BaseModel):
    season: str
    episodes: List[Episode]
    has_next: bool

class SeasonList(RootModel):
    root: List[Season]
