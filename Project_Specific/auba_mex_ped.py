"""
Script: auba_mex_ped.py
Description: Tool for auba mex ped
Category: Project_Specific
"""
import json
import pdfplumber
import os

# Path to the PDF file
pdf_path = r"C:\Users\Henry\Desktop\New folder\41ebec39-4cb1-4a28-9a7a-ab3c73e70be2.pdf"
# Output JSON path
json_path = os.path.splitext(pdf_path)[0] + '.json'

# Template JSON structure
json_data = {
    "reference": "",
    "pedimentoNumber": "",
    "operationType": "",
    "pedimentoKey": "",
    "regime": "",
    "originDestination": None,
    "exchangeRate": "",
    "grossWeight": "",
    "customsSection": "",
    "modeOfTransport": {
        "entryOrExit": None,
        "customsArrival": None,
        "customsExit": None,
    },
    "valueInDollars": "",
    "valueForCustoms": "",
    "pricePaid": "",
    "importerOrExporter": {
        "rfc": "",
        "curp": "",
        "name": "",
        "address": {
            "street": "",
            "city": "",
            "country": "",
            "state": "",
            "postalCode": "",
            "rawAddress": ""
        }
    },
    "acceptanceCodeNumber": "",
    "supplierOrBuyer": {
        "fiscalId": "",
        "name": "",
        "address": {
            "street": "",
            "city": "",
            "country": "",
            "state": "",
            "postalCode": "",
            "rawAddress": ""
        },
        "vinculation": "",
        "invoices": [
            {
                "invoiceId": "",
                "date": "",
                "incoterm": "",
                "currency": "",
                "valueOfInvoice": "",
                "exchangeRate": "",
                "valueInUsd": ""
            }
        ]
    },
    "oceanTransport": {
        "idNumber": "",
        "sealNumbers": [],
        "containerNumbers": []
    },
    "roadTransport": {
        "identificationNumber": "",
        "country": "",
        "sealNumber": ""
    },
    "items": [
        {
            "section": "",
            "tariffFraction": "",
            "subnumber": "",
            "connections": None,
            "evaluationMethodMode": None,
            "unitOfMeasure": None,
            "quantity": "",
            "price": "",
            "producerCountryCode": "",
            "description": "",
            "valueForCustoms": "",
            "commercialValue": "",
            "unitPrice": "",
            "otherObservations": ""
        }
    ]
}

# Extract all text from the PDF
all_text = ""
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        all_text += page.extract_text() + "\n"

# Save the extracted text for reference
with open(os.path.splitext(pdf_path)[0] + '_extracted.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)

# Save the template JSON for manual mapping
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=4)

print(f"Extracted text saved to: {os.path.splitext(pdf_path)[0]}_extracted.txt")
print(f"Template JSON saved to: {json_path}") 