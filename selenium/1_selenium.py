# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome() # "./chromedriver.exe"
browser.get("http://naver.com")

# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back() # 뒤로 가기
# browser.forward() # 앞으로 가기 
# browser.refresh() # 새로고침

# elem = browser.find_element_by_id("query")
# elem.send_keys("웹 스크래핑")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_element_by_tag_name("a")
elem = browser.find_elements_by_tag_name("a")

for e in elem:
    e.get_attribute("href")