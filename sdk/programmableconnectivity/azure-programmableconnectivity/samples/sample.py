import os
from dotenv import load_dotenv

from azure.programmableconnectivity import (
    ProgrammableConnectivityClient,
)
from azure.programmableconnectivity.models import (
    DeviceNetworkIdentifier,
    LocationVerifyRequest,
    LocationDevice,
    NumberVerifyRequest,
    SimSwapRetrieveRequest,
    SimSwapVerifyRequest,
    NetworkIdentifier,
)
from azure.identity import ClientSecretCredential

load_dotenv("../../../../.env")

credential = ClientSecretCredential(
    tenant_id=os.environ.get("PROGRAMMABLECONNECTIVITY_TENANT_ID"),
    client_id=os.environ.get("PROGRAMMABLECONNECTIVITY_CLIENT_ID"),
    client_secret=os.environ.get("PROGRAMMABLECONNECTIVITY_CLIENT_SECRET"),
)

APC_GATEWAY_ID = "xxxx"

client = ProgrammableConnectivityClient(
    endpoint="https://20.26.169.136",
    credential=credential,
    api_version="0.1.0",
    connection_verify=False,
)

### Network Retrieve

network_retrieve_request_body = DeviceNetworkIdentifier(
    identifier_type="IPv4",
    device_identifier="1.2.3.4",
)

network_retrieve_response = client.networks.retrieve(
    network="Network", body=network_retrieve_request_body, apc_gateway_id=APC_GATEWAY_ID
)

print(f"The device is associated with the Network with code {network_retrieve_response.network_code}")

### Location Verify

location_verify_request_body = LocationVerifyRequest(
    network_identifier=NetworkIdentifier(identifier_type="NetworkCode", identifier="123456"),
    latitude=51.650911,
    location=-0.079278,
    accuracy=0.1,
    location_device=LocationDevice(ipv4_address="1.2.3.4"),
)

location_verify_response = client.location_interface.verify(
    location="Location", body=location_verify_request_body, apc_gateway_id=APC_GATEWAY_ID
)

print(f"Location verification response: {location_verify_response.verification_result}")

### Number Retrieve

number_retrieve_request_body = NetworkIdentifier(identifier_type="NetworkCode", identifier="123456")

number_retrieve_response = client.number_interface.retrieve(
    number="Number", body=number_retrieve_request_body, apc_gateway_id=APC_GATEWAY_ID
)

print(f"The number of the device used to call this endpoint is {number_retrieve_response.phone_number}")

### Number Verify

number_verify_request_body = NumberVerifyRequest(
    phone_number="+44123456789",
    network_identifier=NetworkIdentifier(identifier_type="NetworkCode", identifier="123456"),
)

number_verify_response = client.number_interface.verify(
    number="Number", body=number_verify_request_body, apc_gateway_id=APC_GATEWAY_ID
)

print(f"Number verification response: {number_verify_response.verification_result}")

### SIM Swap Retrieve

sim_swap_retrieve_body = SimSwapRetrieveRequest(
    phone_number="+44123456789",
    network_identifier=NetworkIdentifier(identifier_type="NetworkCode", identifier="123456"),
)

sim_swap_retrieve_response = client.sim_swap_interface.retrieve(
    sim_swap="SimSwap", body=sim_swap_retrieve_body, apc_gateway_id=APC_GATEWAY_ID
)

print(f"Time since last SIM Swap: {sim_swap_retrieve_response.date}")

### SIM Swap Verify

sim_swap_verify_request_body = SimSwapVerifyRequest(
    phone_number="+44123456789",
    maxAgeHours=4,
    network_identifier=NetworkIdentifier(identifier_type="NetworkCode", identifier="123456"),
)

sim_swap_verify_response = client.sim_swap_interface.verify(
    sim_swap="SimSwap", body=sim_swap_verify_request_body, apc_gateway_id=APC_GATEWAY_ID
)

print(f"SIM Swap verification response: {sim_swap_verify_response.verification_result}")
