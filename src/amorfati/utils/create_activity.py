from pathlib import Path
from amorfati.utils.yaml_handler import YAMLHandler
from pathlib import Path

# Dynamiskt hitta projektroten
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent


def create_activity(name: str, save_dir: str, template_path: str):
    """Creates a new activity YAML based on a template."""
    save_path = Path(save_dir) / f"{name}.yaml"
    handler = YAMLHandler(save_path)

    template_handler = YAMLHandler(Path(template_path))
    activity_data = template_handler.load()

    if handler and not handler.prompt_overwrite():
        print("Operation cancelled.")
        return

    if handler == activity_data:
        print("The file already has the same content. No changes made.")
        return

    handler.save(activity_data)
    print(f"Created {save_path}")


if __name__ == "__main__":
    name = input("Name of the activity (no spaces!): ")
    save_dir = input("Save directory (ex: ./config/activities): ").strip()
    # standard lagring om inget anges, kan tas bort om man senare vill skapa
    # andra templates än bara för config/activities
    if not save_dir:
        save_dir = "config/activities"
    template_path = PROJECT_ROOT / 'templates' / 'activity_template.yaml'
    create_activity(name, save_dir, template_path)
