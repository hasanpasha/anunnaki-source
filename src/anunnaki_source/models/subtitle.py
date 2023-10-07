from anunnaki_source.models.file_extensions import FileExtension
from pydantic import BaseModel, RootModel
from typing import List

class Subtitle(BaseModel):
    url: str
    lang: str
    extension: FileExtension

class SubtitleList(RootModel):
    root: List[Subtitle]