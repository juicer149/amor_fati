from dataclasses import dataclass
from typing import Optional

@dataclass
class Activity:
    name            : str
    type            : str
    value           : int
    duration_weight : Optional[float]   = None
    description     : Optional[str]     = None

