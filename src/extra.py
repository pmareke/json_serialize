from dataclasses import dataclass, field


@dataclass
class Port:
    name: str
    number: int


@dataclass
class EnvVar:
    name: str
    value: str


@dataclass
class SecretRef:
    name: str
    key: str


@dataclass
class EnvVarFromSecret:
    name: str
    secret: SecretRef


@dataclass
class Container:
    image: str
    cpu: str
    memory: str
    name: str
    env: list[EnvVar | EnvVarFromSecret] = field(default_factory=list)
    ports: list[Port] = field(default_factory=list)

@dataclass
class Metadata:
    name: str
    labels: dict[str, str]
    annotations: dict[str, str]

