from aiohttp import ClientSession, ClientResponse
from abc import abstractmethod
from anunnaki_source import CatalogueSource
from anunnaki_source.network import Request
from anunnaki_source.models import (
    FilterList, MediasPage, Media, Season, SeasonList,
    Episode, VideoList, SubtitleList
)
from typing import Dict, List


class HttpSource(CatalogueSource):
    base_url: str
    headers: Dict[str, str]
    session: ClientSession

    async def fetch_search_media(self, query: str, page: int, filters: FilterList = None) -> MediasPage:
        request = await self.search_media_request(query=query, page=page, filters=filters)
        resp = await self.session.request(**vars(request))
        if not resp.ok:
            return MediasPage(medias=[], has_next=False)
        return await self.search_media_parse(response=resp)

    @abstractmethod
    async def search_media_request(self, query: str, page: int, filters: FilterList = None) -> Request:
        pass

    @abstractmethod
    async def search_media_parse(self, response: ClientResponse) -> MediasPage:
        pass

    async def fetch_popular_media(self, page: int, filters: FilterList = None) -> MediasPage:
        request = await self.popular_media_request(page=page, filters=filters)
        resp = await self.session.request(**vars(request))
        if not resp.ok:
            return MediasPage(medias=[], has_next=False)
        return await self.popular_media_parse(response=resp)

    @abstractmethod
    async def popular_media_request(self, page: int, filters: FilterList = None) -> Request:
        pass

    @abstractmethod
    async def popular_media_parse(self, response: ClientResponse) -> MediasPage:
        pass

    async def fetch_latest_media(self, page: int, filters: FilterList = None) -> MediasPage:
        request = await self.latest_media_request(page=page, filters=filters)
        resp = await self.session.request(**vars(request))
        if not resp.ok:
            return MediasPage(medias=[], has_next=False)
        return await self.latest_media_parse(response=resp)

    @abstractmethod
    async def latest_media_request(self, page: int, filters: FilterList = None) -> Request:
        pass

    @abstractmethod
    async def latest_media_parse(self, response: ClientResponse) -> MediasPage:
        pass

    async def get_detail(self, media: Media) -> Media:
        return await self.fetch_media_detail(media=media)

    async def fetch_media_detail(self, media: Media) -> Media:
        request = await self.media_detail_request(media=media)
        resp = await self.session.request(**vars(request))
        if not resp.ok:
            return media

        return await self.media_detail_parse(response=resp)

    @abstractmethod
    async def media_detail_request(self, media: Media) -> Request:
        pass

    @abstractmethod
    async def media_detail_parse(self, response: ClientResponse) -> Media:
        pass

    async def get_season_list(self, media: Media) -> SeasonList:
        if media.is_movie:
            return [Season('0', [Episode(episode='0', slug=media.slug, has_next=False)], False)]

        return await self.fetch_season_list(media=media)

    async def fetch_season_list(self, media: Media) -> SeasonList:
        request = await self.season_list_request(media=media)
        resp = await self.session.request(**vars(request))
        if not resp.ok:
            return media

        return await self.season_list_parse(response=resp)

    @abstractmethod
    async def season_list_request(self, media: Media) -> Request:
        pass

    @abstractmethod
    async def season_list_parse(self, response: ClientResponse) -> SeasonList:
        pass

    async def get_video_list(self, episode: Episode) -> VideoList:
        return await self.fetch_video_list(episode=episode)

    async def fetch_video_list(self, episode: Episode) -> VideoList:
        request = await self.video_list_request(episode=episode)
        resp = await self.session.request(**vars(request))
        if not resp.ok:
            return []

        return await self.video_list_parse(response=resp)

    @abstractmethod
    async def video_list_request(self, episode: Episode) -> Request:
        pass

    @abstractmethod
    async def video_list_parse(self, response: ClientResponse) -> VideoList:
        pass

    async def get_subtitle_list(self, episode: Episode) -> SubtitleList:
        return await self.fetch_subtitle_list(episode=episode)

    async def fetch_subtitle_list(self, episode: Episode) -> SubtitleList:
        request = await self.subtitle_list_request(episode=episode)
        resp = self.session.request(**vars(request))
        if not resp.ok:
            return []
        return await self.subtitle_list_parse(response=resp)

    @abstractmethod
    async def subtitle_list_request(self, episode: Episode) -> Request:
        pass

    @abstractmethod
    async def subtitle_list_parse(self, response: ClientResponse) -> SubtitleList:
        pass
