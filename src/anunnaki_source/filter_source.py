from anunnaki_source.models import Filter
from abc import ABC, abstractmethod

from typing import List

class FilterSource(ABC):
    @abstractmethod
    def get_filters(self) -> List[Filter]:
        pass
