from anunnaki_source.models import Filter
from abc import ABC, abstractmethod


class FilterSource(ABC):
    @abstractmethod
    def get_filters(self) -> list[Filter]:
        pass
