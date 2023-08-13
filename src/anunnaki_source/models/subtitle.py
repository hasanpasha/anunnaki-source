from dataclasses import dataclass
from anunnaki_source.models.file_extensions import FileExtension


@dataclass
class Subtitle:
    url: str
    language: str
    extension: FileExtension
