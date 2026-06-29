import requests
import os

def post_to_facebook(message: str) -> bool:
    page_id = os.environ["FB_PAGE_ID"]
    access_token = os.environ["FB_PAGE_ACCESS_TOKEN"]

    url = f"https://graph.facebook.com/v19.0/{page_id}/feed"
    data = {
        "message": message,
        "access_token": access_token
    }

    resp = requests.post(url, data=data)
    if resp.status_code == 200:
        result = resp.json()
        print(f"Posted successfully: {result.get('id')}")
        return True
    else:
        print(f"Failed to post: {resp.status_code} {resp.text}")
        return False
