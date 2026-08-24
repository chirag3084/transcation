import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Replace with your actual JSONBin.io credentials / config
BIN_ID = os.environ.get("DEFAULT_BIN_ID")
API_KEY = os.environ.get("JSONBIN_API_KEY")  # Usually sent as X-Master-Key or X-Access-Key


def send_data_to_jsonbin(request):
    """
    Extracts transaction payload from the request and updates JSONBin.
    """
    url = f"{os.environ.get("JSONBIN_API_URL")}/{BIN_ID}"

    headers = {
        "Content-Type": "application/json",
        "X-Master-Key": API_KEY,
    }

    # Extract data depending on whether your request is JSON or form-encoded
    if request.content_type == "application/json":
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            payload = {}
    else:
        payload = request.POST.dict()

    # Send data to JSONBin (use PUT to update existing bin, POST to create a new bin)
    response = requests.put(url, json=payload, headers=headers)

    return response.json()
