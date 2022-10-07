from dataclasses import dataclass
from typing import List, Dict


@dataclass
class TprogerDTO:
    tproger : List[Dict]

@dataclass
class HabrDTO:
    habr : List[Dict]