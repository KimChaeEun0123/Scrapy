import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50").text
# text로 해줘야 오류 안 생김

indeed_soup = BeautifulSoup(indeed_result, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')
'''
for page in pages:
    print(page.find("span"))
'''
spans = []
for page in pages:
    spans.append(page.find("span"))

spans = spans[:-1]
print(spans)