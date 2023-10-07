from pydantic import BaseModel, RootModel
from typing import List

class Episode(BaseModel):
    episode: str
    slug: str
    has_next: bool
    is_special: bool = False

class EpisodeList(RootModel):
    root: List[Episode]