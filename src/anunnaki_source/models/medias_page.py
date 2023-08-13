from dataclasses import dataclass
from anunnaki_source.models import Media


@dataclass
class MediasPage:
    medias: list[Media]
    has_next: bool
