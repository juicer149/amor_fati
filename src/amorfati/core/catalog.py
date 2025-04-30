import logging
from pathlib import Path
from typing import List, Dict, Optional

from amorfati.core.activity import Activity


class ActivityCatalog:
    """
    Catalog for managing Activity instances loaded from YAML files.

    Args:
        base_path (str): Root directory where YAML activity files are stored.
    """
    def __init__(self, base_path: str = "config/activities"):

        self.base_path  =   Path(base_path)
        
        # Control that the catalog exist
        if not self.base_path.exists():
            logger.warning(f"Activity base_path {self.base_path!r} does not exist.")

        self._activities:   Dict[str, Activity] =   {}
        self.reload()

    
    def reload(self) -> None:
        """
        Reloads all activities from YAML files under base_path.
        Clear any previously loaded activities.

        Uses Path.rglob(pattern) to search for files, including subdirectories
        """

        if not self.base_path.exists():
            logger.warning(f"Activity base_path {self.base_path!r} does not exist.")

        self._activities.clear()
        for yaml_file in self.base_path.rglob("*.yaml"):
            try:
                act = Activity.from_yaml(str(yaml_file))
                self._activities[act.name] = act
            except Exception as e:
                logger.error(f"Failed loading {yaml_file}: {e}") 


    def all(self) -> List[Activity]:
        """
        Returns a list of all loaded Activity by its name, 
        or None if not found.

        vore det bättre att göra en __iter__?
        """

        return list(self._activities.values())

    
    def get(self, name: str) -> Optional[Activity]:
        """
        Retrieves a single Activity by its name, or None if not found
        """

        return self._activities.get(name)

    
    def filter_by_type(self, type_name: str) -> List[Activity]:
        """
        Returns a list of activities mathing the given type.

        Args:
            type_name (str): The activity type to filter by.
        """

        return [act for act in self._activities.values() if act.type == type_name]


    def __contains__(self, name: str) -> bool:
        """
        Enables use of 'name in catalog' to check existence.
        """
        return name in self._activities

    
    def __getitem__(self, name: str) -> Activity:
        """
        Allows catalog[name] syntax to retrieve an Activity.
        Raises KeyError if not found.
        """
        return self._activities[name]


    def __iter__(self):
        """
        Makes the catalog itself iterable over Activity instances.

        Example:
            for activity in catalog:
                print(activity)
        """
        return iter(self._activities.values())


    def __len__(self) -> int:
        return len(self._activities)


    def __repr__(self) -> str:
        return f"<ActivityCatalog: {len(self)} activities>"


