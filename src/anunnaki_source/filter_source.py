from anunnaki_source.models import Filter, FilterList
from abc import ABC, abstractmethod

from typing import List

class FilterSource(ABC):
    @abstractmethod
    def get_filters(self) -> FilterList:
        pass
