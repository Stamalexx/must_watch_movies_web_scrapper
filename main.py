from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
movie_titles_all = soup.find_all(name="h3", class_="title")

movie_titles_list = []
for movie_titles in movie_titles_all:
    movie_titles_list.append(movie_titles.getText())

movie_titles_list.reverse()
print(movie_titles_list)

with open("movies.txt","w",encoding="UTF-8") as file:
    for movies in movie_titles_list:
        file.write(movies + "\n")