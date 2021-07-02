import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
# 일반 사용자가 아닌 크롤러 등이 사이트에 접근하려고 할 때 접근을 차단할 수 있음
# 페이지에 접속을 할 때 user agent 값을 넘겨주면 해결됨 
# user agent는 접속하는 브라우저에 따라 달라짐

for i in range(1, 6):    
    #print("페이지: ", i) 
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())
    for item in items:

        # 광고 제품은 제외
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
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            #print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100) # 구분