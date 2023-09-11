from dataclasses import dataclass


@dataclass
class Episode:
    episode: str
    slug: str
    has_next: bool
    is_special: bool = False
