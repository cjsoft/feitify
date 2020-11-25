import requests
import json
import os


def notify(msg, hook_url=None):
    with open(os.path.join(os.environ["HOME"], ".feitifyrc"), "r") as f:
        config = json.load(f)
    resp = requests.post(
        config["hook_url"] if hook_url is None else hook_url,
        data=json.dumps({"msg_type": "text", "content": {"text": msg}}),
    )
    return resp.status_code == 200 and json.loads(resp.text)["StatusCode"] == 0
