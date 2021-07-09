from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome() # "./chromedriver.exe"
browser.get("http://daum.net")

elem = browser.find_element_by_name("q")
elem.send_keys("웹 스크래핑")
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()
browser.quit() # 모든 브라우저 닫기
browser.close() # 탭 닫기