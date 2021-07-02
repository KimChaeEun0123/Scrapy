# Regular Expression
정규식은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어이다. 많은 프로그래밍 언어에서 문자열의 검색, 치환을 위해 지원하고 있다. 

<br>  

## 형태 
## 1) .
. 부분에 특정 문자가 들어가는 것을 의미한다.
### E.g. ca.e
* care, cafe, case (O)
* caffe (X)

## 2) ^ 
문자열의 시작에 특정 문자열이 포함되는 것을 의미한다.
### E.g. ^de
* desk, destination (O)
* fade (X)

## 3) $
문자열의 끝에 특정 문자열이 포함되는 것을 의미한다.
### E.g. se$
* case, base (O)
* face (X)   

<br>

## re 모듈
`re`는 파이썬에서 기본적으로 지원하는 모듈이다.
## 1) re.compile
원하는 정규식 형태를 변수에 넣어준다.

`p = re.compile("원하는 형태")`
## 2) match
주어진 문자열의 처음부터 일치하는지 확인한다.

`m = p.match("비교할 문자열")`   

간단한 정규식 예제 프로그램을 작성해본다.
```python
import re

p = re.compile("ca.e") 
m = p.match("cafe")

# print(m.group()) 
# 매치되지 않으면 에러 발생

if m:
    print(m.group())
else:
    print("매칭되지 않음")
```
위의 프로그램을 함수로 정리한다. 

```python
import re

p = re.compile("ca.e") 

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("care")
print_match(m)

m = p.match("careless")
print_match(m)
```   
## 3) search
주어진 문자열 중 일치하는 게 있는지 확인한다.

`m = p.search("비교할 문자열")`
## 4. findall
일치하는 모든 것을 리스트 형태로 반환한다.

`lst = p.findall("비교할 문자열")`   

<br>

## 반환
## 1) group()
일치하는 문자열을 반환한다.
## 2) string
입력받은 문자열을 반환한다. 함수가 아니라 변수이므로 괄호를 쓰지 않는다.
## 3) start()
일치하는 문자열의 시작 index를 반환한다.
## 4) end()
일치하는 문자열의 끝 index를 반환한다.
## 5) span()
일치하는 문자열의 시작/끝 index를 반환한다.   


위의 내용을 통해 정규식 프로그램을 작성해본다.
```python
import re

p = re.compile("ca.e") 

def print_match(m):
    if m:
        print("m.group(): ", m.group()) 
        print("m.string: ", m.string) 
        print("m.start(): ", m.start()) 
        print("m.end(): ", m.end())
        print("m.span(): ", m.span())
    else:
        print("매칭되지 않음")

m = p.search("careless")
print_match(m)
m = p.search("good care")
print_match(m)

lst = p.findall("careless")
print(lst)
lst = p.findall("good care")
print(lst)
lst = p.findall("good care cafe")
print(lst)
```