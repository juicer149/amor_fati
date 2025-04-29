import yaml
from amorfati.core.activity import Activity

def load_activity_from_yaml(path: str) -> Activity:
    
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    
    return Activity(
            name            = path.split('/')[-1].replace('.yaml', ''),
            type            = data['type'],
            value           = data['value'],
            duration_weight = data.get('duration_weight'),
            description     = data.get('description')
    )
