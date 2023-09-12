from requests import Session
from abc import abstractmethod
from anunnaki_source import Source
from anunnaki_source.models import (
    Filter, MediasPage, Media, Season, Episode, Video, Subtitle
)

class CatalogueSource(Source):
    base_url: str
    headers: dict[str, str]
    session: Session
    support_latest: bool 

    @abstractmethod
    def fetch_search_media(self, query: str, page: int, filters: list[Filter] = None) -> MediasPage:
        pass
    
    @abstractmethod
    def fetch_popular_media(self, page: int, filters: list[Filter] = None) -> MediasPage:
        pass

    @abstractmethod
    def fetch_latest_media(self, page: int, filters: list[Filter] = None) -> MediasPage:
        pass
    
    @abstractmethod
    def fetch_media_detail(self, media: Media) -> Media:
        pass
    
    @abstractmethod
    def fetch_season_list(self, media: Media) -> list[Season]:
        pass
    
    @abstractmethod
    def fetch_video_list(self, episode: Episode) -> list[Video]:
        pass
    
    @abstractmethod
    def fetch_subtitle_list(self, episode: Episode) -> list[Subtitle]:
        pass