from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from zeep import Client
from zeep.wsdl import Document
from lxml import etree

app = FastAPI(debug=True)

# Load the WSDL file
WSDL_PATH = "src/salesforce_erp_sync/erp_salesforce_sync_flows/case/clients/navision_wsdl.xml"  # Replace with the path to your WSDL file
client = Client(WSDL_PATH)

# Serve the WSDL file
@app.get("/wsdl")
async def get_wsdl():
    """
    Serve the WSDL file for clients to consume.
    """
    return FileResponse(WSDL_PATH, media_type="application/xml")


@app.post("/")
async def soap_endpoint(request: Request):
    """
    Handle SOAP requests and route to the appropriate operation.
    """
    # Parse the incoming SOAP request
    body = await request.body()
    envelope = etree.fromstring(body)
    print(envelope)
    # Extract the operation name
    soap_body = envelope.find("{http://schemas.xmlsoap.org/soap/envelope/}Body")
    if soap_body is None or len(soap_body) == 0:
        return Response(content="Invalid SOAP request", status_code=400)

    operation_name = soap_body[0].tag.split("}")[1]  # Extract operation name
    operation = client.service._binding._operations.get(operation_name)

    if not operation:
        return Response(content=f"Unknown operation: {operation_name}", status_code=400)

    # Extract parameters from the SOAP request
    params = {}
    for param in soap_body[0]:
        params[param.tag.split("}")[1]] = param.text

    # Call the operation
    # try:
    #     response_data = operation(**params)
    # except Exception as e:
    #     return Response(content=f"Error processing operation: {str(e)}", status_code=500)
    response_data = f"""
            <wSClaim>
                <ClaimHeader>
                    <No>123</No>
                    <WarrantyNo>456</WarrantyNo>
                    <ClaimLine>
                        <LineNo>1</LineNo>
                        <ProductType>TypeA</ProductType>
                    </ClaimLine>
                </ClaimHeader>
            </wSClaim>"""
    # Generate the SOAP response
    response_xml = f"""
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <{operation_name}Response>
                {response_data}
            </{operation_name}Response>
        </soap:Body>
    </soap:Envelope>
    """
    return Response(content=response_xml, media_type="text/xml")
