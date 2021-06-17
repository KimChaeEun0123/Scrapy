import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50").text

print(type(indeed_result))

indeed_soup = BeautifulSoup(indeed_result, "html.parser")

