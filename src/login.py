from requests.auth import HTTPBasicAuth as basicAuth
from requests import post


def login_flow(username, password, client_id, client_secret):
    client_auth = basicAuth(client_id, client_secret)
    post_data = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    headers = {"User-Agent": "reddit-login/1.0 by Chromadream"}
    response = post(
        "https://www.reddit.com/api/v1/access_token",
        auth=client_auth,
        data=post_data,
        headers=headers,
    )
