from prefect import flow
from simple_salesforce import Salesforce  # Importing Salesforce explicitly for type hinting
from clients.salesforce import create_salesforce_client



@flow(log_prints=True) # type: ignore
def flow_sync_case_object() -> None:
    client = create_salesforce_client(
        "orgfarm-fa4f9b8218-dev-ed.develop.my",  # domain or instance url
        "3MVG9rZjd7MXFdLhb._HMnhm1AWRnoV0BYmerX0NeniOwjGnCpLB5V63WpobYGesT7kU.6xZTzWo5FDqHLNs4", # client id
        "86B4D3A674F80344FEDE761EEC0DD0DE6073D47736E7F0A4E179553DC172BE30" # client secret
    )

    cases = client.get_claims()
    rows_to_update: dict[str, dict[str, str]] = {}

    for case in cases:
        for field in ["Id", "CaseNumber", "Status"]:
            print(field, ":", case[field])

        rows_to_update[case["Id"]] = {
            "Nav_Id__c": "1234"
        }

    client.update_claims(rows_to_update)


if __name__ == "__main__":
    flow_sync_case_object()