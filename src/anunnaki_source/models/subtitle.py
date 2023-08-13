from dataclasses import dataclass
from anunnaki_source.models import FileExtension


@dataclass
class Subtitle:
    url: str
    language: str
    extension: FileExtension
