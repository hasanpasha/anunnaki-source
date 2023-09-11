from anunnaki_source.models import Media
from anunnaki_source.models import Kind

import pytest


@pytest.fixture
def media():
    return Media(
        "The Day After Tomorrow",
        Kind.MOVIES, "29067",
        "/video/ar/29067?showInfo=true",
        "poster-images/5D2C3F65-8DEF-69FE-4D0E-61E70CAD39AE_poster_medium_thumb.jpg",
        "Jack Hall, paleoclimatologist,"
        """must make a daring trek across America to reach his son, trapped 
        in the cross-hairs of a sudden international storm which plunges the planet into a new Ice Age.""",
        ["action", "adventure", "sci-fi"])


def test_media_title(media: Media):
    assert media.title == "The Day After Tomorrow"


def test_media_kind(media: Media):
    assert media.kind == Kind.MOVIES


def test_media_is_movie(media: Media):
    assert media.is_movie


def test_media_slug(media: Media):
    assert media.slug == "29067"


def test_media_tags(media: Media):
    assert len(media.tags) == 3

