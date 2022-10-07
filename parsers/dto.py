from dataclasses import dataclass
from typing import List, Dict


@dataclass
class TprogerDTO:
    tproger: List[Dict]


@dataclass
class HabrDTO:
    habr: List[Dict]


@dataclass
class ItProgerDTO:
    it_proger: List[Dict]
