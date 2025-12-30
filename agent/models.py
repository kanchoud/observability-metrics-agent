from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Metric:
    name: str
    value: float
    type: str  # gauge, counter
    tags: Optional[List[str]] = None
