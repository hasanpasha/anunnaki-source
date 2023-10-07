from pydantic import BaseModel, RootModel
from typing import List, Optional

class Episode(BaseModel):
    episode: str
    slug: str
    has_next: bool
    is_special: Optional[bool] = False

class EpisodeList(RootModel):
    root: List[Episode]