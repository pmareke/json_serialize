import json

from dataclasses import dataclass, field
from src.extra import Container, Metadata


@dataclass
class Deployment:
    container: Container
    metadata: Metadata
    replicas: int
    service_account_name: str

    def __repr__(self) -> str:
        return json.dumps(self.__dict__, indent=2, default=lambda o: o.__dict__)

