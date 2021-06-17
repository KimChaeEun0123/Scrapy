# requests

## get()
URL에 접속해서 정보를 가져온다.

```python
import requests

res = requests.get("http://naver.com")
```
## status_code
```python
import requests

res = requests.get("https://naver.com")
# res = requests.get("https://news.naver.com/")
# robots.txt 확인: 네이버는 첫 페이지만 접근 허가

print("응답코드: ", res.status_code) # 200이면 정상
```
## requests.codes.ok
정상적인 status code를 의미한다.
```python
import requests

res = requests.get("http://naver.com")
if res.status_code == requests.codes.ok:
    print("정상입니다")
else: 
    print("문제가 생겼습니다. [에러코드: ", res.status_code, "]")
```

## raise_for_status()
정상 코드가 아닌 경우 오류를 발생시키는 함수이다.
```python
import requests

res = requests.get("http://naver.com")
# res = requests.get("https://news.naver.com/")
res.raise_for_status()
print("웹 스크래핑을 진행합니다")

```


# BeautifulSoup