from enum import Enum
from typing import List
from pydantic import BaseModel, RootModel

class Resolution(Enum):
    P240 = "240p"
    P360 = "360p"
    P480 = "480p"
    P720 = "720p"
    P1080 = "1080p"
    P1440 = "1440p"
    P2160 = "2160p"
    P4320 = "4320p"


class Video(BaseModel):
    url: str
    resolution: Resolution

class VideoList(RootModel):
    root: List[Video]

