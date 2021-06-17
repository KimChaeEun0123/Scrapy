# HTML

## Web site
텍스트 파일. 웹사이트의 소스를 보면 이상하고 복잡한 text 파일일 뿐 이것을 실행해도 아무일도 일어나지 않는다. 이 text를 브라우저에서 실행시켜야 비로소 웹페이지가 된다. 

## Web components
### 1. HTML
웹의 내용을 작성하는 언어이다.
### 2. CSS
웹을 디자인하는 언어이다.
### 3. Javascript
웹의 동작을 구현하는 언어이다.

## HTML 
- 여는 태그, 닫는 태그 쌍 `<html></html>` 또는
- 한 문장 구성 `<html/>`

### head
이 html 문서가 어떤 문서인지 명시 
- charset: 문자의 인코딩 방식을 지정하는 속성
- title: 문서 제목. 브라우저 화면 탭바에 노출되는 내용
### body
실제 브라우저 화면에 나타나는 내용

```html
<html>
    <head>
        <meta charset="utf-8">
        <title>제목</title>
    </head>
    <body>
        <h1>내용</h1>
        내용들
    </body>
</html>
```
## input tag
### type
입력 태그의 유형
### value
입력 태그의 초기값
### name
서버로 전달되는 이름
```html
<body> 
    <input type="text" value="아이디 입력">
    <input type="password" value="패스워드 입력">
    <input type="button" value="로그인">
</body>
```
* input tag는 쌍을 이루지 않음

## Anchor tag
링크를 생성하는 태그
## href
연결할 주소 지정
## target
링크를 클릭할 때 창을 어떻게 열지 설정
- _blank, _self
## title
링크에 마우스 커서를 올릴 때 도움말 설명
```html
<body>
    <a href="http://google.com">구글로 이동</a>
    <a href="http://google.com" target="_blank">구글로 이동</a>
    <a href="http://google.com" title="Google">구글로 이동</a>
</body>
```

## Container
의미없이 요소를 묶기 위한 태그

## <div>
block-level
## <span>
inline-level
```html
<div>
    <span>Lorem</span> ipsum dolor sit.
</div>
