### Obtain a Network for a device with a known IP address

### Verify that a SIM Swap has occurred in the last 4 hours for a given phone number

```python
sim_swap_verify_request_body = SimSwapVerifyRequest(
    phone_number="+44123456789",
    maxAgeHours=4,
    network_identifier=NetworkIdentifier(
        identifier_type="NetworkCode",
        identifier="123456"
    ) 
)

sim_swap_verify_response = client.sim_swap_interface.verify(
    sim_swap="SimSwap",
    body = sim_swap_verify_request_body,
    apc_gateway_id=APC_GATEWAY_ID
)

print(f"SIM Swap response: {sim_swap_verify_response.verification_result}")
```