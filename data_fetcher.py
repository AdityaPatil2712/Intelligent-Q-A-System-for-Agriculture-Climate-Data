import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DATA_GOV_API_KEY")

AGRI_RESOURCE_UIDS = [
    "9ef84268-d588-465a-a308-a864a43d0070"   
]

CLIMATE_RESOURCE_UIDS = [
    "4a69f6f6-6f81-4c07-a063-9f69e26ac5a1"   
]

DEFAULT_LIMIT = 100  

def build_url(resource_uid):
    return f"https://api.data.gov.in/resource/{resource_uid}"

def get_data_from_resource(resource_uid, limit=DEFAULT_LIMIT, extra_params=None):
    url = build_url(resource_uid)
    params = {"api-key": API_KEY, "format": "json", "limit": limit}
    if extra_params:
        params.update(extra_params)
    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            records = data.get("records", [])
            return records, resp.status_code
        else:
            return [], resp.status_code
    except Exception as e:
        return [], None

def get_agriculture_data(limit=DEFAULT_LIMIT):
    for uid in AGRI_RESOURCE_UIDS:
        records, status = get_data_from_resource(uid, limit=limit)
        if records:
            return {"records": records, "resource_uid": uid}
    return {"records": [], "resource_uid": None}

def get_climate_data(limit=DEFAULT_LIMIT):
    for uid in CLIMATE_RESOURCE_UIDS:
        records, status = get_data_from_resource(uid, limit=limit)
        if records:
            return {"records": records, "resource_uid": uid}
    return {"records": [], "resource_uid": None}
