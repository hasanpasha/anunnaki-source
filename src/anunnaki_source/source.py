from anunnaki_source.models import (
    Media, Season, SeasonList, Episode, EpisodeList,
    Video, VideoList, Subtitle, SubtitleList, Filter
)

from abc import ABC, abstractmethod
from typing import Union, List


class Source(ABC):
    name: str
    pkg: str
    lang: str
    id: int

    @abstractmethod
    async def get_detail(self, media: Media) -> Media:
        pass

    @abstractmethod
    async def get_season_list(self, media: Media) -> SeasonList:
        pass

    @abstractmethod
    async def get_video_list(self, episode: Episode) -> VideoList:
        pass

    @abstractmethod
    async def get_subtitle_list(self, episode: Episode) -> SubtitleList:
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"
