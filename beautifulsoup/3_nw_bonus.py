import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page="

for i in range(11, 0, -1):
    res = requests.get(url+str(i))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    cartoons = soup.find_all("td", attrs={"class":"title"})

    for cartoon in reversed(cartoons):
        title = cartoon.a.get_text()
        link = "https://comic.naver.com"+cartoon.a["href"]
        print(title, link)



