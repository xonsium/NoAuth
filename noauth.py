import re
import json
import urllib

class NoAuth():

    def __init__(self) -> None:
        pass


    def nauth(self) -> None:
        reg = '<script id="session" data-testid="session" type="application\\/json"\\>({.*})<\\/script>'
        req = urllib.request.Request("https://open.spotify.com/search")
        res = urllib.request.urlopen(req).read()
        session_text = re.findall(reg, str(res))[0]
        session_json = json.loads(session_text)

        self.access_token = session_json.get('accessToken')
        self.cliend_id = session_json.get('clientId')
        print(f"Access Token: {self.access_token}\nClient ID: {self.cliend_id}")


    def query(self, url):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        req = urllib.request.Request(url, None, headers)
        res = urllib.request.urlopen(req).read()
        json_res = json.loads(res)
        return json_res    