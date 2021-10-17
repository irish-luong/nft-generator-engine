from serde import serialize, deserialize
from dataclasses import dataclass, asdict


@dataclass
class Base:
    def serialize(self):
        return asdict(self)


@serialize
@deserialize
@dataclass
class Configurations(Base):
    x: int
