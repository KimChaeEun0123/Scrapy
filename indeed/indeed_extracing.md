# Extracing Indeed Pages
- 코드 정리 전의 내용
- 공부하면서 적은 코드 설명(마구마구 써서 더러움!)

```
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50").text
# 검색 결과를 50개씩 보여주는 페이지
# get()으로 source 받아온다. 
# text로 바꿔줘야 BeautifulSoup 사용 가능. 
# content: 바이너리 원문, json(): 딕셔너리 객체


indeed_soup = BeautifulSoup(indeed_result, "html.parser")
# html.parser: 파이썬에서 제공하는 html 해석기
# BeautifulSoup(markup, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})
# div 태그의 class="pagination"을 *한 개* 찾는다.

links = pagination.find_all('a')
# pagination에서 a 태그를 *모두* 찾는다. 
# find_all은 리스트(Result Set) 형태로 반환

'''
for link in links:
    print(link.find("span"))
'''

pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]

for i in range(max_page):
    print(f"start={i*50}")

```
```
def extract_indeed_jobs(last_page):
    for page in range(last_page):
        # print(f"&start={page*LIMIT}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
        # status code: 200 (success)
```
```
def extract_indeed_jobs(last_page):
    jobs=[]
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}") 
    # 20페이지 다 출력되면 오래걸리므로 테스트용으로 0번째 것만 출력
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    # print(results)

    for result in results:
        #print(result.find("h2", {"class": "title"}))
        '''
        title = result.find("h2", {"class": "title"})
        print(title.find("a")) # anchor 전부 출력
        anchor = title.find("a")["title"]
        print(anchor)
        '''
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        # find("a")["title"]: 속성 얻기
        print(title)
    return jobs
```
## beautifulsoup 메서드 정리

```

1. 모든 a 태그 검색
soup.find_all("a")
soup("a")

2. string 이 있는 title 태그 모두 검색
soup.title.find_all(string=True)
soup.title(string=True)

3. a 태그를 두개만 가져옴
soup.find_all("a", limit=2)

4. string 검색
soup.find_all(string="Elsie") # string 이 Elsie 인 것 찾기
soup.find_all(string=["Tillie", "Elsie", "Lacie"]) # or 검색
soup.find_all(string=re.compile("Dormouse")) # 정규식 이용

5. p 태그와 속성 값이 title 이 있는거
soup.find_all("p", "title")
예)

6. a태그와 b태그 찾기
soup.find_all(["a", "b"])

7. 속성 값 가져오기
soup.p['class']
soup.p['id']

8. string을 다른 string으로 교체
tag.string.replace_with("새로운 값")

9. 보기 좋게 출력
soup.b.prettify()

10. 간단한 검색
soup.body.b # body 태그 아래의 첫번째 b 태그
soup.a # 첫번째 a 태그

11. 속성 값 모두 출력
tag.attrs

12. class 는 파이썬에서 예약어이므로 class_ 로 쓴다.
soup.find_all("a", class_="sister")

13. find
find()
find_next()
find_all()

14. find 할 때 확인
if soup.find("div", title=True) is not None:
i = soup.find("div", title=True)

15. data-로 시작하는 속성 find
soup.find("div", attrs={"data-value": True})

16. 태그명 얻기
soup.find("div").name

17. 속성 얻기
soup.find("div")['class'] # 만약 속성 값이 없다면 에러
soup.find("div").get('class') # 속성 값이 없다면 None 반환

18. 속성이 있는지 확인
tag.has_attr('class')
tag.has_attr('id')
있으면 True, 없으면 False

19. 태그 삭제
a_tag.img.unwrap()

20. 태그 추가
soup.p.string.wrap(soup.new_tag("b"))
soup.p.wrap(soup.new_tag("div")
```
