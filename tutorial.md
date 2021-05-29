# Scrapy Tutorial


Scrapy가 설치 완료된 상태로 시작. 설치가 안 되어있다면 해당 문서 참조 [Installation guide](https://doc.scrapy.org/en/1.5/intro/install.html#intro-install).


## Goals
- quotes.toscrape.com 사이트를 스크레이핑 한다.


## Tasks
1. 새 Scrapy project 생성
2. 사이트를 크롤링하고 데이터를 추출하기 위해 [spider](https://doc.scrapy.org/en/1.5/topics/spiders.html#topics-spiders) 쓰기
3. command line을 통해 스크레이핑한 데이터 내보내기
4. 링크를 되풀이하도록 spider 변경
5. spider 인자 사용하기


## Creting a project
스크레이핑을 시작하기 전, 새로운 Scrapy project를 세팅한다. 

```
scrapy startproject tutorial
```

위 코드는 다음과 같은 `tutorial` directory를 생성한다. 

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

## Our first Spider
spider는 웹사이트의 정보를 스크레이핑 하는 데 사용되는 사용자 정의 클래스이다. 
spider 클래스는 반드시 `scrapy.Spider`의 서브 클래스여야 한다.

`tutorial/spiders` 디렉터리에 `quotes_spider.py` 파일을 생성한다.

```python
import scrapy
  
class QuotesSpider(scrapy.Spider):
  
  name = "quotes"                           
  
  def start_requests(self):
    urls = [
      'http://quotes.toscrape.com/page/1/',
      'http://quotes.toscrape.com/page/2/',
    ]
    for url in urls:
       yield scrapy.Request(url=url, callback=self.parse)
       
  def parse(self, response):
    page = response.url.split("/")[-2]
    filename = 'quotes-%s.html' % page
    with open(filename, 'wb') as f:
      f.write(response.body)
      self.log('Saved file %s' % filename)
```
* `name`: 다른 spider와 중복 불가한 고유의 name
* `start_requests()`: 
* `parse()`:
* 

## How to run our spider
프로젝트의 최상위 디렉터리에서 다음을 실행한다.
`scrapy crawl quotes`
이 명령은 방금 생성한 `quotes` spider를 실행한 것이다. 
crawl 명령이 `quotes.toscrape.com` 도메인에 어떠한 요청을 보냈고, 다음과 같은 결과를 얻을 수 있다.
```
...
2021-05-29 07:51:20 [scrapy.extensions.telnet] INFO: Telnet Password: eadcffe97a1c50c0
2021-05-29 07:51:20 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
...
```
