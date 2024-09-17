import sys
from pprint import pprint
from urllib.parse import urljoin

import requests

if __name__ == "__main__":
    helptxt = (
        "> configurator.py <API_TOKEN> <USER> <WEB_PROJECT> <DOMAIN>\n"
        "Note that web project must have a virtual env and a main.py associated with it"
    )
    if [y for y in sys.argv if "-h" in y]:
        pprint(helptxt)
        exit()
    try:
        _, api_token, user, web_project, domain_name = sys.argv
    except ValueError:
        print("need all values provided")
        print(helptxt)
        exit()
    headers = {"Authorization": f"Token {api_token}"}
    api_base = f"https://www.pythonanywhere.com/api/v1/user/{user}/"
    command = (
        f"/home/{user}/.virtualenvs/{web_project}/bin/uvicorn "
        "--uds $DOMAIN_SOCKET "
        f"--ssl-certfile=/home/{user}/{domain_name}.cert "
        f"--ssl-keyfile=/home/{user}/{domain_name}.key "
        f"{web_project}.main:app"
    )
    response = requests.post(
        urljoin(api_base, "websites/"),
        headers=headers,
        json={
            "domain_name": domain_name,
            "enabled": True,
            "webapp": {"command": command},
        },
    )
    pprint(response)
    pprint(response.json())
