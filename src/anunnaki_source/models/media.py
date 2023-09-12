from dataclasses import dataclass
from anunnaki_source.models.kind import Kind


@dataclass
class Media:
    title: str = None
    kind: Kind = None
    slug: str = None
    url: str = None
    year: int = None
    thumbnail_url: str = None
    description: str = None
    tags: list[str] = None

    @property
    def is_movie(self) -> bool:
        return self.kind == Kind.MOVIES
