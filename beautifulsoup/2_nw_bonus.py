import re
import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

day_lst = ['월', '화', '수', '목', '금', '토', '일']

for i, day in enumerate(day_lst):
    if i==0:
        day_toon = soup.find("div", attrs={"class":re.compile("^col")})
    else:
        day_toon = day_toon.find_next_sibling("div")

    cartoons = day_toon.find_all("a", attrs={"class":"title"})
    # class 속성이 title인 모든 a element 반환(리스트)
    print()
    print(day+"요일")
    for cartoon in cartoons:
        print(cartoon.get_text(), end=" / ")