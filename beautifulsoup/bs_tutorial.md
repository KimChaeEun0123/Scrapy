# BeautifulSoup4

## 1. 네이버 웹툰

```python
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
```   

모든 정보를 담고 있는 BeautifulSoup 객체를 생성한다. "html.parser"는 파이썬이 제공하는 html 해석기이다.
```python
soup = BeautifulSoup(res.text, "html.parser")
print(soup.title) 
# title element 전체 출력
print(soup.title.get_text())
# title element에서 텍스트만 출력

print(soup.a)
# soup 객체에서 처음 발견되는 a element 반환
print(soup.a.attrs)
# a element 속성 정보
print(soup.a["href"])
# a element의 href 속성 '값' 정보 출력
```
페이지에 대한 이해가 높을 때 위 같이 쓸 수 있다.   

find를 통해 원하는 값을 반환한다.
```python
print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# find: 첫 번째 값 반환
# class 속성이 "~"인 a element를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"}))
# class 속성이"~"인 어떤 element를 찾아줘
```   
인기 급상승 만화 1위를 다음과 같이 찾을 수 있다.
```python
print(soup.find("li", attrs={"class":"rank01"}))
# li element 전체 출력
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
# rank1에서 a element 출력
print(rank1.a.get_text())
# a element에서 텍스트만 가져오기
```   
next_sibling으로 다음 element 정보를 찾을 수 있다.
```python
print(rank1.next_sibling)
# 찾은 element로부터 다음 element 정보
print(rank1.next_sibling.next_sibling)
# 태그 사이 개행정보 있어서 두 번 next_sibling

rank2 = rank1.next_sibling.next_sibling
# 2위 웹툰
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
# 3위 웹툰 제목 출력

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
# previous_sibling: 이전 element 찾음
```   
parent는 부모 태그(현재 태그를 감싸고 있는 태그)를 가져온다.
```python
print(rank1.parent)
```   

next_sibling에 조건을 걸어줄 수 있다. 다음과 같이 작성하면 개행 정보 등으로 인해 next_sibling을 두 번씩 작성하지 않아도 된다.
```python
rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())
```   

매번 find_next_sibling 하는 것보다는 한 번에 가져오는 게 편하다. 다음과 같이 작성하면 모든 형제 태그를 가져올 수 있다. 
```python
print(rank1.find_next_siblings("li"))
# 모든 li 형제들 가져옴
```   

텍스트를 통해 태그를 찾을 수 있다.
```python
webtoon = soup.find("a", text="급식아빠-24화 지금 바로 친다!")
'''
<a 
onclick="nclk_v2(event,'rnk*p.cont','758662','1')" 
href="/webtoon/detail.nhn?titleId=758662&amp;no=24" 
title="급식아빠-24화 지금 바로 친다!">
급식아빠-24화 지금 바로 친다!</a>
-> 태그 사이에 있는 것이 text
'''
print(webtoon)
```   

네이버 웹툰 전체 목록(요일별)을 가져온다.
```python
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 a element 반환(리스트)
for cartoon in cartoons:
    print(cartoon.get_text())
```   

특정 웹툰의 회차 제목을 가져온다.
```python
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=sun"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
cartoons = soup.find_all("td", attrs={"class":"title"})
title = cartoons[0].a.get_text()
print(title)
# 1 페이지의 첫 회차 제목
title = cartoons[1].a.get_text()
print(title)
# 두 번째 회차 제목
link = cartoons[0].a["href"]
# 첫 번째 회차 링크 
print("https://comic.naver.com"+link)
# 바로 이동 가능한 링크 출력
```   

페이지 1의 전체 회차 제목과 링크를 가져온다.
```python
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title, link)
```   

페이지 1의 전체 회차 평점 평균을 계산한다.
```python
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수: ", total_rates)
print("평균 점수: ", total_rates / len(cartoons))
```   

인터프리터 언어라는 파이썬의 장점을 이용하여 파이썬 쉘을 이용할 수 있다.
* 터미널에 `python`을 입력하여 들어가고, `exit()`을 통해 빠져나올 수 있다.
* 복사한 내용은 마우스 오른쪽을 클릭하여 쉘에 붙여 넣을 수 있다.
* 위쪽 방향키를 통해 이전에 실행했던 내용을 쉘에 불러올 수 있다.   

## 2. 쿠팡

## 3. 다음 이미지