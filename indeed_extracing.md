# Extracing Indeed Pages
공부하면서 적은 초기 코드

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