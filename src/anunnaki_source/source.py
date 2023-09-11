from anunnaki_source.models import (
    Media, Season, Episode, Video, Subtitle, Filter
)

from abc import ABC, abstractmethod
from typing import Union


class Source(ABC):
    name: str
    pkg: str
    lang: str
    id: int

    @abstractmethod
    def get_detail(self, media: Media) -> Media:
        pass

    @abstractmethod
    def get_season_list(self, media: Media) -> list[Season]:
        pass

    @abstractmethod
    def get_video_list(self, episode: Episode) -> list[Video]:
        pass

    @abstractmethod
    def get_subtitle_list(self, episode: Episode) -> list[Subtitle]:
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"
