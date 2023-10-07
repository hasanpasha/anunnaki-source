from typing import List
from anunnaki_source.models.media import Media
from pydantic import BaseModel

class MediasPage(BaseModel):
    medias: List[Media]
    has_next: bool
