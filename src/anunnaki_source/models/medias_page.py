from dataclasses import dataclass
from typing import List
from anunnaki_source.models.media import Media


@dataclass
class MediasPage:
    medias: List[Media]
    has_next: bool
