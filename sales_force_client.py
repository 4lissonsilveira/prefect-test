from simple_salesforce import Salesforce
from pprint import pprint


ACCESS_TOKEN = "00DgK00000BavTO!AQEAQGP2ez94XFw90C3M346a2XNQ5xuTkz9Nu8O3eitzP8XWenIAJ0gGP9yJIle_7VM89g_ZNLgkXeMePICAV.AATuliQ42c"
INSTANCE_URL = "https://orgfarm-fa4f9b8218-dev-ed.develop.my.salesforce.com"

sf_client: Salesforce = Salesforce(
    session_id=ACCESS_TOKEN,
    instance_url=INSTANCE_URL,
    version="64.0"
)

leads: dict[str, list[dict[str, str]]] = sf_client.query(
    "SELECT Id, casenumber, status, subject FROM Case WHERE Status = 'New'"
)

for lead in leads["records"]:
    for field in ["Id", "CaseNumber", "Status", "Subject"]:
        print(field, ":", lead[field])
    print("")