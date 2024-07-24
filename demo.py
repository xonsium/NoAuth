from noauth import NoAuth

api = NoAuth()
api.nauth()
data = api.query("https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n")
print(data)