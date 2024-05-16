import requests
from bs4 import BeautifulSoup

EMPIRE_WEB_URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(EMPIRE_WEB_URL)

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, 'html.parser')

top_100_movies_title_tags = soup.find_all(name='h3', class_ = 'listicleItem_listicle-item__title__BfenH')

top_100_movies = [movie.getText() for movie in top_100_movies_title_tags]

with open('../python-projects/PROJECT-45/top_100_movies.txt','w') as file:
    for movie in top_100_movies[::-1]:
        file.write(f'{movie}\n')