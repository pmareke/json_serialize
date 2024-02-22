from approvaltests.approvals import verify

from tests.builders.deployment_builder import DeploymentBuilder


class TestBadDeployment:
    def test_bad_deployment(self):
        deployment = DeploymentBuilder().build_bad()

        verify(deployment)
