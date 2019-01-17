# Python file edit function

## 01. Open file

```python
f = open("위치/파일이름.txt", 'w')
f.close()
```

* 파일이름만 입력하면 현재 위치한 폴더에서 파일이 만들어진다
* 'w'의 경우 파일열기모드로 읽기보드(r), 쓰기모드(w), 추가모드(a)가 있다



## 02. Write down data

```python
f = open("위치/파일이름.txt", 'w')
for i in range(1, 11):
    data = f'this is line {i}.\n'
    f.write(data)
f.close()
```

* 파일에 입력할 data를 정의하고 f.write(data)를 통해 이를 대상파일에 쓴다
* python은 자동으로 파일을 끄지만 만약의 충돌을 대비하여 f.close()로 꺼주자



## 03. Add data

```python
f = open('위치/파일이름.txt', 'a')
for i in range(11, 20):
    data = f'this is additional line{i}.\n'
    f.write(data)
f.close()
```

* 파일을 열 때 추가모드 'a' 열어준다
* 파일을 쓰는 방법과 동일하게 함수를 적용한다



## 04. Read data

```python
f = open("위치/파일이름.txt", 'r')
data = f.read()
print(data)
f.close	
```

* 읽기모드 'r'으로 파일을 열고 f.read()를 통해 읽은 것을 data에 할당한다
* 그 후 할당된 data를 출력한다



## 05. Easy way to read, write, add data

```python
with open("위치/파일이름.txt", '?') as f:
	#1.read / ? = 'r'
    data = f.read()
    print(data)
    #2.write data / ? = 'w'
    f.write("data내용")
    #3.add data / ? = 'a'
    f.write("data내용")
```

* `with open('파일이름.txt', '?') as f:`로 함수 f 를 통해 파일을 연다
* 각자 목적이 무엇이냐에 따라 모드를 다르게 하여 연다
* 다음 각각의 목적에 따른 함수를 입력한다 `f.read(), f.write()`



## 06. Crawling from HTML

```python
import requests
from bs4 import BeautifulSoup

url = 'url address'

response = requests.get(url).text #url에서 request를 통해 html소스를 가져온다
soup = BeautifulSoup(response, 'html.parser') #이러한 html을 파싱한다

data_set = soup.select('.value') #셀렉터를 이용하여 필요한 정보를 얻어낸다
data = data_set[i].text 

print(data)
```

* parsing(파싱) : 데이터를 다른 모양으로 가공하는 것을 의미한다
* response = request.get(url) 이후에 response.status_code를 출력했을 때 200이 나온다면 정상적으로 가져온 것
* 그 후 response.content를 출력하면 텍스트가 출력된다

