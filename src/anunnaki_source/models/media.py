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

    def __add__(self, other) -> 'Media':
        new = Media()
        for key, this_value, other_value in zip(self.__dict__.keys(), self.__dict__.values(), other.__dict__.values()):
            setattr(new, key, other_value if other_value else this_value)
        return new
