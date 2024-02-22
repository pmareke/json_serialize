from approvaltests.approvals import verify

from tests.builders.deployment_builder import DeploymentBuilder


class TestDeployment:
    def test_bad_deployment(self):
        deployment = DeploymentBuilder().build_bad()

        verify(deployment)

    def test_good_deployment(self):
        deployment = DeploymentBuilder().build_good()

        verify(deployment)
