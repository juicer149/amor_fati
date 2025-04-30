from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, Dict

from amorfati.core.activity import Activity


@dataclass
class ActivityBit:
    """
    Represents a single logged occurrence of an Activity.

    Attributes:
        activity: The Activity instance being logged.
        start_time: When the activity started. If duration_minutes is provided but
            start_time is None, it will be auto-calculated based on current time.
        duration_minutes: Duration of the activity in minutes (if applicable).
        units_data: Other unit-based metrics (e.g., distance_km, repetitions).
        completed: Boolean flag for completion of boolean activities.
        amor_fati_score: Calculated score for this occurrence.
    """
    activity        : Activity
    start_time      : Optional[datetime]            = None
    duration_minutes: Optional[float]               = None
    units_data      : Optional[Dict[str, float]]    = None
    completed       : Optional[bool]                = None
    amor_fati_score : float                         = 0.0

    def __post_init__(self):
        """
        Post-initialization to set default start_time if only duration is provided,
        and normalize boolean activities.
        """
        # Auto-calculate start_time if duration is provided but start_time is missing
        if self.duration_minutes is not None and self.start_time is None:
            now = datetime.now()
            self.start_time = now - timedelta(minutes=self.duration_minutes)

        # Ensure boolean activities have no units_data and a boolean completed flag
        if self.activity.is_bool:
            self.units_data = None
            self.completed = bool(self.completed)

    def _gather_input(self) -> Dict[str, float]:
        """
        Gathers all input metrics into a unified dict for score calculation.

        Returns:
            A dict mapping metric names to float values.
        """
        data: Dict[str, float] = {}
        # Include duration if present
        if self.duration_minutes is not None:
            data["duration_minutes"] = self.duration_minutes
        # Include other units
        if self.units_data:
            data.update(self.units_data)
        # Include boolean completion as 1.0 or 0.0
        if self.completed is not None:
            data["completed"] = 1.0 if self.completed else 0.0
        return data

    def score(self) -> float:
        """
        Calculates and returns the score for this ActivityBit.

        Uses the Activity.__matmul__ method (the @ operator) for scoring.

        Returns:
            The raw score as a float.
        """
        metrics = self._gather_input()
        raw_score = self.activity @ metrics
        self.amor_fati_score = raw_score
        return raw_score
