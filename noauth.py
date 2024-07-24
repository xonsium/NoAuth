import re
import json
import urllib.request, urllib.error
import os

class NoAuth():

    def __init__(self, log) -> None:
        self.log = log
        if os.path.isfile("session.json"):
            with open("session.json", 'r') as f:
                file_json = json.load(f)
                self.access_token = file_json.get('accessToken')
                print(self.access_token)
                self.cliend_id = file_json.get('clientId')
        else:
            self.auth()

        if log: print(f"Access Token: {self.access_token}\nClient ID: {self.cliend_id}")

    def auth(self) -> None:
        reg = '<script id="session" data-testid="session" type="application\\/json"\\>({.*})<\\/script>'
        req = urllib.request.Request("https://open.spotify.com/search")
        res = urllib.request.urlopen(req).read()
        session_text = re.findall(reg, str(res))[0]
        with open("session.json", 'w') as f:
            f.write(session_text)
        session_json = json.loads(session_text)

        self.access_token = session_json.get('accessToken')
        self.cliend_id = session_json.get('clientId')
        if self.log: print(f"Access Token: {self.access_token}\nClient ID: {self.cliend_id}")


    def query(self, url):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        req = urllib.request.Request(url, None, headers)
        try:
            print(self.access_token)
            res = urllib.request.urlopen(req).read()
        except urllib.error.HTTPError:
            self.auth()
            headers = {
            "Authorization": f"Bearer {self.access_token}"
            }
            res = urllib.request.urlopen(req).read()
        json_res = json.loads(res)
        return json_res