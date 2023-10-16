from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

#bk

try:
    response =  requests.get("https://www.imdb.com/chart/top")
    soup = BeautifulSoup(response.text,"html.parser")
    # print(soup)
    movies = soup.find('tbody',class_="lister-list").find_all('tr')
    movie_list ={"movie_rank":[],"movie_name":[],"movie_year":[],"movie_rate":[]}
    for movie in movies:
        # print(movie)
        movie_name = movie.find('td', class_='titleColumn').a.text
        rate = movie.find('td', class_='ratingColumn imdbRating').strong.text
        year= movie.find('td', class_='titleColumn').span.text#.replace("(","").replace(")","")
        rank = movie.find('td', class_='titleColumn').get_text(strip = True).split('.')[0] # strip is used to removing the tags in th data
        # print(rank,movie_name, rate , year)
        movie_list["movie_rank"].append(rank)
        movie_list["movie_name"].append(movie_name)
        movie_list["movie_year"].append(year)
        movie_list["movie_rate"].append(rate)

        # print(rate)
        # break
except Exception as e:
    print(e)

df = pd.DataFrame(data=movie_list)
print(df.head())
connection = sqlite3.connect("text.db")
cursor = connection.cursor()
qry = "CREATE TABLE IF NOT EXISTS movies(movie_rank,movie_name,movie_year,movie_rate)"
cursor.execute(qry)
for i in range(len(df)):
    cursor.execute("insert into movies values (?,?,?,?)",df.iloc[i])

connection.commit()
connection.close()

