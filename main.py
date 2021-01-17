from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
site_data = response.text
soup = BeautifulSoup(site_data, "html.parser")
movies = soup.find_all(name="h3", class_="title")
# print(movies)
for movie in movies[::-1]:
    try:
        with open("movies.txt", "a", encoding="utf8") as file:
            file.write(f"{movie.text}\n")
    except FileNotFoundError:
        with open("movies.txt", "w") as file:
            file.write("Best 100 Movies Of All Time\n")


