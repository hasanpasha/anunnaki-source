from dataclasses import dataclass
from typing import List
from anunnaki_source.models.episode import Episode


@dataclass
class Season:
    season: str
    episodes: List[Episode]
    has_next: bool
