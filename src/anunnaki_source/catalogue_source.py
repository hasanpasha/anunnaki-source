from aiohttp import ClientSession

from abc import abstractmethod
from anunnaki_source import Source
from anunnaki_source.models import (
    Filter, FilterList, MediasPage, Media, Season, SeasonList, 
    Episode, EpisodeList, Video, VideoList, Subtitle, SubtitleList
)

from typing import Dict, List

class CatalogueSource(Source):
    base_url: str
    headers: Dict[str, str]
    session: ClientSession
    support_latest: bool

    async def init_session(self) -> None:
        self.session = ClientSession(headers=self.headers)

    async def get_search_media(self, query: str, page: int, filters: FilterList = None) -> MediasPage:
        return await self.fetch_search_media(query, page, filters)

    @abstractmethod
    async def fetch_search_media(self, query: str, page: int, filters: FilterList = None) -> MediasPage:
        pass
    
    async def get_popular_media(self, page: int, filters: FilterList = None) -> MediasPage:
        return await self.fetch_popular_media(page, filters)

    @abstractmethod
    async def fetch_popular_media(self, page: int, filters: FilterList = None) -> MediasPage:
        pass

    async def get_latest_media(self, page: int, filters: FilterList = None) -> MediasPage:
        return await self.fetch_latest_media(page, filters)
    
    @abstractmethod
    async def fetch_latest_media(self, page: int, filters: FilterList = None) -> MediasPage:
        pass
 
    async def get_detail(self, media: Media) -> Media:
        return await self.fetch_media_detail(media)
    
    @abstractmethod
    async def fetch_media_detail(self, media: Media) -> Media:
        pass
    
    async def get_season_list(self, media: Media) -> SeasonList:
        return await self.fetch_season_list(media)
    
    @abstractmethod
    async def fetch_season_list(self, media: Media) -> SeasonList:
        pass
    
    async def get_video_list(self, episode: Episode) -> VideoList:
        return await self.fetch_video_list(episode)
    
    @abstractmethod
    async def fetch_video_list(self, episode: Episode) -> VideoList:
        pass
    
    async def get_subtitle_list(self, episode: Episode) -> SubtitleList:
        return await self.fetch_subtitle_list(episode)

    @abstractmethod
    async def fetch_subtitle_list(self, episode: Episode) -> SubtitleList:
        pass