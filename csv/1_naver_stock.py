import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="


filename = "시가총액-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
# 엑셀파일에서 한글 깨짐 있으면 utf -> utf-8-sig
# newline: 줄바꿈 개행문자 없게
writer = csv.writer(f)

# 복사 붙여넣기 해와서 table 상단 넣어주기
# title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# writer.writerow(title)

for page in range(1, 5):
    
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    
    # 스크래핑을 통해서 table 상단 넣어주기
    if(page==1):
        titles = soup.find("table", attrs={"class":"type_2"}).find("thead").find("tr")
        titles = titles.find_all("th")
        # print(titles)
        table_top = []
        for title in titles:
            table_top.append(title.string)
        #print(table_top)
        writer.writerow(table_top)

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        cols = row.find_all("td")
        if len(cols) <= 1:
            continue 
        # 의미 없는 데이터 리스트 생성을 막음

        data = [col.get_text().strip() for col in cols]
        # strip()으로 리스트 안쪽 공백 제외하고 리스트 입력

        #print(data)
        # if문과 strip 없을 땐 불필요한 공백, 탭 등이 함께 출력됨
        
        writer.writerow(data)

