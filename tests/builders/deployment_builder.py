from src.deployment_bad import Deployment as BadDeployment
from src.deployment_good import Deployment as GoodDeployment
from src.extra import Container, Metadata, Port, EnvVar, EnvVarFromSecret, SecretRef


class DeploymentBuilder:
    def __init__(self) -> None:
        self._container = Container(
            image="any-image",
            cpu="any-cpu",
            memory="any-memory",
            name="any-name",
            ports=[Port(name="http", number=80)],
            env=[
                EnvVar(name="ENV", value="any-value"),
                EnvVarFromSecret(
                    name="secret", secret=SecretRef(name="secret", key="key")
                ),
            ],
        )
        self._metadata = Metadata(
            name="any-name",
            labels={"app": "any-app"},
            annotations={"author": "any-author"},
        )
        self._replicas = 1
        self._service_account_name = "any-service-account-name"

    def with_container(self, container: Container) -> "DeploymentBuilder":
        self._container = container
        return self

    def with_metadata(self, metadata: Metadata) -> "DeploymentBuilder":
        self._metadata = metadata
        return self

    def with_replicas(self, replicas: int) -> "DeploymentBuilder":
        self._replicas = replicas
        return self

    def with_service_account_name(
        self, service_account_name: str
    ) -> "DeploymentBuilder":
        self._service_account_name = service_account_name
        return self

    def build_bad(self) -> BadDeployment:
        return BadDeployment(
            self._container, self._metadata, self._replicas, self._service_account_name
        )

    def build_good(self) -> GoodDeployment:
        return GoodDeployment(
            self._container, self._metadata, self._replicas, self._service_account_name
        )
