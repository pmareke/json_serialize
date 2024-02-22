from approvaltests.approvals import verify

from src.extra import Container, Metadata

from tests.builders.deployment_builder import DeploymentBuilder


class TestGoodDeployment:
    def test_good_deployment(self):
        deployment = DeploymentBuilder().build_good()

        verify(deployment)
        
    def test_good_deployment_with_container(self):
        container = Container(name="my-container", image="my-image", cpu="1", memory="512Mi")
        deployment = DeploymentBuilder().with_container(container).build_good()

        verify(deployment)

    def test_good_deployment_with_metadata(self):
        metadata = Metadata(name="my-deployment", labels={"app": "my-app"}, annotations={"author": "me"})
        deployment = DeploymentBuilder().with_metadata(metadata).build_good()

        verify(deployment)

    def test_good_deployment_with_more_replicas(self):
        deployment = DeploymentBuilder().with_replicas(2).build_good()

        verify(deployment)

    def test_good_deployment_with_service_account(self):
        deployment = DeploymentBuilder().with_service_account_name("another-service-account").build_good()

        verify(deployment)
