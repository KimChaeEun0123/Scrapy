from selenium import webdriver

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input")
print(elem)
# elem.click()

# # 3. id, pw 입력
# browser.find_element_by_id("id").send_keys("naver_id")
# browser.find_element_by_id("pw").send_keys("password")

# # 4. 로그인 버튼 클릭
# browser.find_element_by_id("log.login").click()

