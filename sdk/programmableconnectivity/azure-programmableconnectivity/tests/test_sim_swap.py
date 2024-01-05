import os, functools

from devtools_testutils import AzureTestCase, EnvironmentVariableLoader, recorded_by_proxy

from azure.programmableconnectivity import ProgrammableConnectivityClient

AZURE_TEST_RUN_LIVE = True

SchemaRegistryPreparer = functools.partial(
    EnvironmentVariableLoader,
    'programmableconnectivity',
    programmableconnectivity_endpoint=os.environ.get("PROGRAMMABLECONNECTIVITY_ENDPOINT"),
    programmableconnectivity_group=os.environ.get("PROGRAMMABLECONNECTIVITY_GROUP"),
)

# class TestSimSwap(AzureRecordedTestCase):
class TestSimSwap(AzureTestCase):
    # Start with any helper functions you might need, for example a client creation method:
    # TODO have no idea how I'm supposed to input the actual credential here.
    def create_client(self, endpoint):
        credential = self.get_credential(ProgrammableConnectivityClient)
        # TODO check about `api_version="0.1.0"`
        client = self.create_client_from_credential(ProgrammableConnectivityClient, credential=credential, endpoint=endpoint, api_version="0.1.0", connection_verify=False)
        return client

    @SchemaRegistryPreparer()
    # @recorded_by_proxy
    def test_check_sim_swap(self, programmableconnectivity_endpoint):
        client = self.create_client(programmableconnectivity_endpoint)
        assert client is not None
        sim_resp = client.sim_swap_interface.verify(
                    sim_swap="SimSwap",
                    body = {
                    "networkIdentifier": {
                        "identifier": "Microsoft_Operator_OpenGatewayCIBA",
                        "identifierType": "IPv4"
                    },
                    "maxAgeHours": 240  # Optional. Maximum lookback for SimSwap verification.
                    },
                    apc_gateway_id="<something>"
        )
        assert sim_resp is not None