from bs4 import BeautifulSoup
import requests,openpyxl
# excel = openpyxl.Workbook()
# sheet = excel.active
# sheet.title = "Movie List"
# sheet.append(["Rank",'Movie Name','Year of Release','IMDB Rating'])
try:
    response =  requests.get("https://www.dxomark.com/smartphones/")
    soup = BeautifulSoup(response.text,"html.parser")
    # print(soup)
    phones = soup.find('div',class_ = "ranking-overflow-inner").find_all("div",class_= "row device-row")
    print(phones)
    for phone in phones:
        phone_name = phone.find('div',class_="col").find('a')
        print(phone_name)
        break
except Exception as e:
    print(e)

# excel.save("Movies.xlsx")


