import requests
import yaml

local_metadata = {
    "version": {
        "monitorizer": 2.3,
        "toolkit": 1.4
    }
}

try:
    metadata_github = yaml.safe_load(
        requests.get("https://raw.githubusercontent.com/BitTheByte/Monitorizer/master/version.yaml").text)
except:
    metadata_github = local_metadata
