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

<br>

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

<br>

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

<br>

parent는 부모 태그(현재 태그를 감싸고 있는 태그)를 가져온다.
```python
print(rank1.parent)
```   

<br>

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

<br>

네이버 웹툰 전체 목록(요일별)을 가져온다.
```python
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title인 모든 a element 반환(리스트)
for cartoon in cartoons:
    print(cartoon.get_text())
```   

<br>

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

<br>

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

<br>

인터프리터 언어라는 파이썬의 장점을 이용하여 파이썬 쉘을 이용할 수 있다.
* 터미널에 `python`을 입력하여 들어가고, `exit()`을 통해 빠져나올 수 있다.
* 복사한 내용은 마우스 오른쪽을 클릭하여 쉘에 붙여 넣을 수 있다.
* 위쪽 방향키를 통해 이전에 실행했던 내용을 쉘에 불러올 수 있다.   

<br>

## 2. 쿠팡
쿠팡에서 노트북을 검색하고 첫 번째 페이지의 노트북 정보를 가져온다. 
```python
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
print(res.text)
```
위 프로그램을 실행시켜도 아무런 동작이 일어나지 않는다. 쿠팡 사이트는 일반 사용자가 아닌 크롤러 등이 사이트에 접근하려고 할 때 접근이 차단되도록 설정되어 있다. 따라서 페이지에 접속을 할 때 user agent 값을 넘겨주어야 한다. (User agent는 접속하는 PC, 브라우저에 따라 달라진다.
```python
import requests
import re
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

print(res.text)
```
제대로 실행되는 것을 볼 수 있다.

<br>

첫 번째로 나타나는 노트북 제품을 가져온다. 클래스 값이 "search-product"로 시작하는 li element 모두를 items에 리스트로 반환한다. items의 첫 번째 요소에서 클래스 값이 "name"인 div element 하나를 텍스트로 출력한다.
```python
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
```
1페이지 전체 제품의 이름을 출력한다.
```python
for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    print(name)
```
가격, 평점, 평점 수 정보를 이름과 함께 출력한다. 평점과 평점 수가 존재하지 않는 제품을 출력할 때 오류가 발생하지 않도록 조건문으로 처리해준다.
```python
for item in items:

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
    
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점 수 없음"
    
    print(name, price, rate, rate_cnt)
```
평점과 평점 수가 없는 상품은 제품의 신뢰도가 떨어지므로 제외하고 가져온다. 평점 또는 평점 수가 없는 item의 경우 continue를 통해 for문을 빠져나오도록 한다. 
```python
for item in items:

    # name, price 생략

    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외>")
        continue
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예: (26)
        rate_cnt = rate_cnt[1:-1]
        # print("리뷰수: ", rate_cnt)
    else:
        print(" <평점 수 없는 상품 제외>")
        continue
    
    print(name, price, rate, rate_cnt)
```
지금까지의 결과에 소비자가 원하는 조건을 걸어주고, 조건에 부합하는 제품만 가져오려 한다. 조건은 다음과 같다.
* 리뷰: 50개 이상
* 평점: 4.5 이상
조건 설정 시 자료형에 주의하도록 한다. 
```python
for item in items:

    # name, price 생략
    
    # 리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        print(" <평점 없는 상품 제외>")
        continue
    
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예: (26)
        rate_cnt = rate_cnt[1:-1]
        # print("리뷰수: ", rate_cnt)
    else:
        print(" <평점 수 없는 상품 제외>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 50:
        print(name, price, rate, rate_cnt)
```

다음과 같은 조건을 걸어줄 수도 있다.
* 광고 제품 제외
* 애플 제품 제외
광고 제품 표시는 제품 이름 앞에 나오므로 for문의 맨앞에 작성해도 무방하다.
```python
for item in items:

    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외> ")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    # 애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외>")
        continue

    # 아래 내용 생략
```

<br>

1페이지부터 5페이지까지의 제품 정보를 위 같은 조건에 따라 가져오는 프로그램을 작성한다. format()을 통해 url에서 page를 나타내는 부분을 1~5까지 반복해서 넣어주도록 한다.

```python
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

for i in range(1, 6):    
    #print("페이지: ", i) 
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
        
    for item in items:

        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print(" <광고 상품 제외> ")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        
        # 애플 제품 제외
        if "Apple" in name:
            #print(" <Apple 상품 제외>")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
        
        # 리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate:
            rate = rate.get_text()
        else:
            #print(" <평점 없는 상품 제외>")
            continue
        
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수 
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            #print(" <평점 수 없는 상품 제외>")
            continue
        
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            print(name, price, rate, rate_cnt)
```
제품 링크를 추가하면 마음에 드는 제품의 링크로 바로 이동할 수 있다. 
```python   
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            #print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100) # 구분
```

## 3. 다음 이미지