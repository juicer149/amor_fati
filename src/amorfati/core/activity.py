from dataclasses import dataclass
from typing import Dict, Optional

import yaml


@dataclass
class Activity:
    """
    Datapoints for actitivties:
        name            :   The specific activity 'name', ex 'trail-running'
        type            :   type of activity, ex 'running' or 'meditaion'
        description     :   description for the specific activity
        primary_focus   :   Which unit that is prioritized for score
        units           :   units -> { 'distance_km': {'weight': 1.0}, etc}
    """

    name            : str
    type            : str
    description     : Optional[str]                         = None
    units           : Optional[Dict[str, Dict[str, float]]] = None
    primary_focus   : Optional[str]                         = None
    requirements    : Optional[Dict[str, str]]              = None
    value           : Optional[float]                       = None

    def __post_init__(self):
        """Define if the activity has units or is a boolean activity"""
        self.is_bool = not bool(self.units)

    @classmethod
    def from_yaml(cls, path: str) -> 'Activity':
        """Loads one Activity from an YAML-file."""
        with open(path, 'r') as f:
            data = yaml.safe_load(f)

        if not isinstance(data, dict):
            raise ValueError(f"Activity YAML is empty or invalid: {path}")

        return cls(
            name=path.split('/')[-1].replace('.yaml', ''),
            type=data.get('type', 'unknown'),
            description=data.get('description'),
            units=data.get('units'),
            primary_focus=data.get('primary_focus'),
            requirements=data.get('requirements'),
            value=data.get('value'),
        )

    def __iter__(self):
        return iter(self.units.items() if self.units else [])

    def __str__(self):
        return f"Activity: {self.name} ({self.type})"

    def __matmul__(self, input_data: Dict[str, float]) -> float:
        """
        För 1.5 och framåt, beräkna score med en matris för lättare mönster
        för ai.
        """
        if self.units:
            score = 0.0

            for unit_name, unit_props in self.units.items():
                weight = unit_props["weight"]
                value = input_data.get(unit_name, 0)
                score += weight * value

            return score

        if self.value is not None:
            completed = input_data.get("completed", 0.0)
            return float(self.value) * completed

        return 0.0
