import json
from serde.json import from_json, to_json
from entities import Configurations


def cleanup() -> None:
    print("Util clean up")


def load_configurations():
    a = {"x": 10, "y": 20}
    c = from_json(Configurations, json.dumps(a))
    print(c)
