from dataclasses import dataclass
from anunnaki_source.models import Episode


@dataclass
class Season:
    season: str
    episodes: list[Episode]
    has_next: bool