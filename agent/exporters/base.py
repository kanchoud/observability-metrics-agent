from abc import ABC, abstractmethod
from typing import List
from agent.models import Metric

class Exporter(ABC):

    @abstractmethod
    def send(self, metrics: List[Metric]):
        pass
