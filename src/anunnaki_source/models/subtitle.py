from dataclasses import dataclass
from anunnaki_source.models.file_extensions import FileExtension


@dataclass
class Subtitle:
    url: str
    lang: str
    extension: FileExtension
