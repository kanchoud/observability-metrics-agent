from abc import ABC, abstractmethod
from typing import List
from agent.models import Metric

class Collector(ABC):

    @abstractmethod
    def collect(self) -> List[Metric]:
        pass
