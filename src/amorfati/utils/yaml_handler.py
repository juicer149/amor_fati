import yaml
from pathlib import Path

class YAMLHandler:
    def __init__(self, path: Path):
        """Initialize with a path to a YAML file."""
        self.path = path

    def __bool__(self) -> bool:
        """Returns True if file exists."""
        return self.path.exists()

    def load(self) -> dict:
        """Loads YAML file content."""
        with open(self.path, 'r') as f:
            return yaml.safe_load(f)

    def save(self, data: dict):
        """Saves a dict as YAML to the file."""
        with open(self.path, 'w') as f:
            yaml.dump(data, f, sort_keys=False)

    def prompt_overwrite(self) -> bool:
        """Asks the user if they want to overwrite an existing file."""
        answer = input(f"File {self.path} exists. Overwrite? (y/n): ").strip().lower()
        return answer == 'y'

    def __eq__(self, other: dict) -> bool:
        """Compares the content of the YAML file with another dict."""
        if not self:
            return False
        current_data = self.load()
        return current_data == other

