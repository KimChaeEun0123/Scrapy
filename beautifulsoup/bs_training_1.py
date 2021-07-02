import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
# 모든 정보 담고 있는 BeautilfulSoup 객체 생성
print(soup.title)
print(soup.title.get_text())
print(soup.a)
# soup 객체에서 처음 발견되는 a element 반환
print(soup.a.attrs)
# a element 속성 정보
print(soup.a["href"])
# a element의 href 속성 '값' 정보 출력
# 페이지에 대한 이해가 높을 때 위 같이 쓸 수 있음

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# find: 첫 번째 값 반환
# class 속성이 "~"인 a element를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"}))
# class 속성이"~"인 어떤 element를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())
print(rank1.next_sibling)
# 찾은 element로부터 다음 element 정보
print(rank1.next_sibling.next_sibling)
# 태그 사이 개행정보 있어서 두 번 next_sibling
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print(rank1.parent)
# li tag의 부모 ol tag의 모든 값 출력

rank1.find_next_sibling("li")
# 조건에 해당하는 것만 찾는 것(이렇게 하면 개행 정보는 안 찍힘)
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

# 매번 find_next_sibling 하는 것보다는 한 번에 하는 게 편함
print(rank1.find_next_siblings("li"))
# 모든 li 형제들 가져옴

webtoon = soup.find("a", text="급식아빠-24화 지금 바로 친다!")
'''
<a 
onclick="nclk_v2(event,'rnk*p.cont','758662','1')" 
href="/webtoon/detail.nhn?titleId=758662&amp;no=24" 
title="급식아빠-24화 지금 바로 친다!">
급식아빠-24화 지금 바로 친다!</a>
'''
print(webtoon)