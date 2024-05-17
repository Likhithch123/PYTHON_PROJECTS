import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from os import environ

# Scraping Billboard 100
input_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
response = requests.get(f'https://www.billboard.com/charts/hot-100/{input_date}')
bill_board_web_page = response.text
soup = BeautifulSoup(bill_board_web_page, 'html.parser')
top_100_songs_elements = soup.select('li ul li h3')
top_100_songs = [song.getText().strip() for song in top_100_songs_elements]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=environ.get('SPOTIFY_CLIENT_ID'),
        client_secret=environ.get('SPOTIFY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt", 
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = input_date.split("-")[0]
for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
