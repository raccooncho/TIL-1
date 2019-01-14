[TOC]



# A. List

## A01. list

* **순서가 있는 수정가능한** 객체의 집단
* 수정, 삭제, 추가가 가능하다
* `[]` 로 작성되며 내부 원소는 `,`로 구분된다



## A02. list 사용

* list는 0부터 시작하는 인덱스로 접근할 수 있다

```python
a = ['a', 1, True, 5, 3, 4, 5]
a[0] = a
a[1] = 1
a[2] = True
```

* list 선언

```python
b = list()
type(b) = class 'list'
c = []
type(c) = class 'list'
```

* list에 원소 추가하기

```python
b = []
b.append(5)
print(b) = [5]

b = [5]
c = ['a', 'b', 'c']
print(b + c) # [5, 'a', 'b', 'c']
print(b + [4, 5]) # [5, 4, 5]
print([1, 2, 3] + [2.4]) # [1, 2, 3, 2.4]

c = b + [1, 2, 3]
print(c) # [5, 1, 2, 3]

d = [1, 2, 3] + [4, 5, 6]
print(d) # [1, 2, 3, 4, 5, 6]
```

* 문자열을 list로 변형하기

```python
list("나는리스트")
print(list("나는리스트"))
# ['나', '는', '리', '스', '트']
```



## A03. list indexing (인덱싱)

* 문자열을 리스트로 만들기 위해서는 `.split()` 을 이용한다
* list(string)을 할 경우 띄어쓰기도 원소로 분류한다
* -1값을 활용하여 마지막 열을 쉽게 찾을 수 있다

```python
s = "hi my name is mnoko".split()
s = ['hi', 'my', 'name', 'is', 'mnoko']
"""
list(s) 할 경우 단어 사이에 space도 하나의 원소로 분류된다
ex) print(list(s))
['h', 'i', ' ', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'm', 'n', 'o', 'k', 'o']
"""

s[0] = 'hi'
s[1] = 'my'
s[-1] = 'mnoko'
```



## A04. list slicing (슬라이싱)

* 리스트를 자르는 법 `리스트변수[시작인덱스:종료인덱스:step]` 이며 마지막 인덱스는 포함하지 않고 step은 생략이 가능하다

```python
s = "hi my name is mnoko"
s[0:2] # ['hi', 'my']
s[0:-1] # ['hi', 'my', 'name', 'is']
s[0:5:2] # ['hi', 'name', 'mnoko']
s[0:] # ['hi', 'my', 'name', 'is', 'mnoko'] 시작 인덱스부터 끝까지
s[:1] # ['hi', 'my'] 처음부터 종료 인덱스까지
```



## A05. list 관련 메소드 및 연산

* `list`.index(item) 으로 리스트 안에서 해당 item의 index 번호를 가져올 수 있다
* `list`.count(item) 으로 리스트에 매칭되는 item의 갯수를 세줄 수 있다

```python
a = ['서울', '대구', '제주', '부산', '서울']
a.index('서울') # 0 (첫 index만 출력)
a.index('제주') # 2
a.count('서울') # 2
a.count('부산') # 1
a.count('인천') # 0
```



## A06. list 원소 추가, 삭제

##### list 원소 추가

* `list_name.append(값)` : **원소**를 리스트 마지막에 추가
* `list_name.insert(index, 값)` : **원소**를 원하는 인덱스 위치에 추가
* `list_name.extend(new_list)` : **리스트**를 리스트 마지막에 추가

```python
a = ['서울', '대구', '부산', '제주']
b = ['인천', '대전']

a.append('서울') # ['서울', '대구', '부산', '제주', '서울']
a.insert(1, '서울') # ['서울', '서울', 대구', '부산', '제주']
a.extend(b) # ['서울', '대구', '부산', '제주', '인천', '대전']
```

##### list 원소 제거

*  `del list_name[index]` : list에서 인덱스를 통해 원소를 제거
* `list_name.remove(값)` : list에서 이름을 통해 원소를 제거 



## A07. list 정렬

##### list 본체를 정렬하기

* `list_name.reverse()` : 리스트를 거꾸로 뒤집기
* `list_name.sort()` : 리스트를 정렬하기 (기본값은 오름차순 정렬)

```python
a = [1, 100, 42, 2345, 23]
a.reverse() # [23, 2345, 42, 100, 1]
a.sort() # [1, 23, 42, 100, 2345]
```

##### 정렬된 list 결과를 받기 (list 본체는 그대로 있고 반환된 새로운 list 결과를 받는 것)

* `new_list = sorted(list)` : 정렬된 리스트를 반환
* `new_list = reversed(list)` : 뒤집어진 결과를 반환 **BUT** 다시 list()를 통해 변형해야 list가 된다

```python
a = [1, 100, 42, 2345, 23]
b = sorted(a)  # [1, 23, 42, 100, 2345]
c = reversed(a) # <list_reverseiterator object at 0x7f0725ececc0>
list(c) # [23, 2345, 42, 100, 1]  
```



# B. Tuple

## B01. Tuple

* tuple은 **불변한 순서가 있는** 객체의 집단
* list와 비슷하지만 한 번 생성되면 값을 변경할 수 없다
* 순서가 있기 때문에 list와 마찬가지로 index로 접근할 수 있다

```python
t = (1, 'hi', True, 4)

t[0] # 1
t[1] # hi
t[2] # True
```

* 괄호가 없어도 tuple이다

```python
t = 1, 2, 3, 4, 5
type(t) = class 'tuple'
```



## B02. tuple 활용하기

* tuple을 이용하여 함수에서 여러 값을 한꺼번에 리턴시킬 수 있다

```python
def minmax(items):
    return min(items), max(items)
minmax([7, 5, 2, 1, 11, 15, 55])
# (1, 55)
```

* tuple을 이용하여 변수를 스왑할 수 있다

```python
a, b = 'hi', 'mnoko'
a, b = b, a
print(a, b) # mnoko hi
```



# C. Dictionary

## C01. Dictionary

* Dictionary는 불변한 key와 수정가능한 value로 맵핑되어 있는 순서가 없는 집합

```python
ex_dict = {'a': 1, 'b': 2}
```

*  key값으로 dictionary, list, set은 사용할 수 없으나 tuple은 사용할 수 있다

```python
a = { {1, 3}: 1, {2, 4}: 2} # set이므로 error
b = { [1, 3]: 1, [2, 4]: 2} # list이므로 error
c = { {"a": 3}: 1, {"abc", 3}: 2} # dictionary이므로 error 
d = { (1, 3): 1, (2, 4): 2} # tuple이므로 정상적으로 작동
```

* key값이 중복되면 마지막 value 값으로 설정 (단 value 값은 중복이 가능하다)

```python
d = {'a': 1, 'a': 2}  #key값이 중복
d = {'a': 2}
```

* 순서가 없기 때문에 index가 아닌 key로 접근해야한다
* key로 접근하여 value를 바꿀 수 있다
* 새로운 key와 value 값을 추가할 수 있다

```python
#key로 접근하기
d = {'a': 1, 'b': 2, 'c': 3}
d['a'] # 1

#key로 접근하여 value를 바꾸기
d['a'] = 100
print(d) # {'a': 100, 'b': 2, 'c': 3}

#새로운 key와 value를 추가하기
d['d'] = -200
print(d) # {'a': 100, 'b': 2, 'c': 3, 'd': -100}
```



## C02. Dictionary 선언

* Dictionary를 선언할 때 빈 중괄호 `{}`를 사용한다
* `dict()`로 명시적으로 선언할 수 있다
* dict constructor을 통해 키와 값을 할당하며 선언할 수 있다

```python
#중괄호로 dict 선언하기
d = {}
type(d) # class 'dict'

#명시적으로 선언하기
d = dict()
type(d) # class 'dict'

#dict constructor을 통해 선언하기
d = dict(a = 5, b = 7, c= 2)
print(d) # {'a': 5, 'b': 7, 'c': 2}
```



## C03. Dictionary 변환



## C04. Dictionary 복사



## C05. Dictionary update



## C06. Dictionary for 문



## C07. Dictionary의 in



## C08. Dictionary 요소 삭제



## C09. Dictionary



# D. Set

