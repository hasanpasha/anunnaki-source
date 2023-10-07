from aiohttp import ClientSession

from abc import abstractmethod
from anunnaki_source import Source
from anunnaki_source.models import (
    Filter, MediasPage, Media, Season, Episode, Video, Subtitle
)

from typing import Dict, List

class CatalogueSource(Source):
    base_url: str
    headers: Dict[str, str]
    session: ClientSession
    support_latest: bool

    async def init_session(self) -> None:
        self.session = ClientSession(headers=self.headers)

    @abstractmethod
    async def fetch_search_media(self, query: str, page: int, filters: List[Filter] = None) -> MediasPage:
        pass
    
    @abstractmethod
    async def fetch_popular_media(self, page: int, filters: List[Filter] = None) -> MediasPage:
        pass

    @abstractmethod
    async def fetch_latest_media(self, page: int, filters: List[Filter] = None) -> MediasPage:
        pass
    
    @abstractmethod
    async def fetch_media_detail(self, media: Media) -> Media:
        pass
    
    @abstractmethod
    async def fetch_season_list(self, media: Media) -> List[Season]:
        pass
    
    @abstractmethod
    async def fetch_video_list(self, episode: Episode) -> List[Video]:
        pass
    
    @abstractmethod
    async def fetch_subtitle_list(self, episode: Episode) -> List[Subtitle]:
        pass