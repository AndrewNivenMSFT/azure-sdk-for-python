import functools

from azure.programmableconnectivity import ProgrammableConnectivityClient

credential = self.get_credential(ProgrammableConnectivityClient)
# TODO check about `api_version="0.1.0"`
client = self.create_client_from_credential(ProgrammableConnectivityClient, credential=credential, endpoint=endpoint, api_version="0.1.0")

