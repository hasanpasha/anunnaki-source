from anunnaki_source.models.kind import Kind
from typing import List, Optional
from pydantic import BaseModel

class Media(BaseModel):
    title: Optional[str] = None
    kind: Optional[Kind] = None
    slug: Optional[str] = None
    url: Optional[str] = None
    year: Optional[int] = None
    thumbnail_url: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None

    @property
    def is_movie(self) -> bool:
        return self.kind == Kind.MOVIES

    def __add__(self, other) -> 'Media':
        new = Media()
        for key, this_value, other_value in zip(self.__dict__.keys(), self.__dict__.values(), other.__dict__.values()):
            setattr(new, key, other_value if other_value else this_value)
        return new
