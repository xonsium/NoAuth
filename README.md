# NoAuth

A python micro lib to make api query to spotify without api key. Idea taken from [kaangiray26](https://github.com/kaangiray26/noauth)

## Demo
```sh
python3 demo.py
```

## Installation
Simply download and add the noauth.py file to your project and use it. No external installation required.

## Usage
NoAuth is built with core python libraries.

```python
from noauth import NoAuth

api = NoAuth()
api.nauth() # authenticate with web access token
data = api.query('https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n') # returns json data

```

## Note
This is possible since spotify allows users to use their web app without account. For that, provate api data such as user account details are inaccessible.