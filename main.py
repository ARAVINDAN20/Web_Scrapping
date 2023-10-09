from bs4 import BeautifulSoup
import requests,openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Movie List"
sheet.append(["Rank",'Movie Name','Year of Release','IMDB Rating'])
try:
    response =  requests.get("https://www.imdb.com/chart/top")
    soup = BeautifulSoup(response.text,"html.parser")
    # print(soup)
    movies = soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        # print(movie)
        movie_name = movie.find('td', class_='titleColumn').a.text
        rate = movie.find('td', class_='ratingColumn imdbRating').strong.text
        year= movie.find('td', class_='titleColumn').span.text#.replace("(","").replace(")","")
        rank = movie.find('td', class_='titleColumn').get_text(strip = True).split('.')[0] # strip is used to removing the tags in th data
        print(rank,movie_name, rate , year)
        sheet.append([rank,movie_name, year , rate])
        # print(rate)
        # break
except Exception as e:
    print(e)

excel.save("Movies.xlsx")


