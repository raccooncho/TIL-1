# Data Structure

### 01. String 메소드

#### 01-(1) 변형

* `a.capitalize()`  : 앞글자를 대문자로 만들어 반환
* `a.title()` : 어퍼스트로피 `'` or ` `  (공백) 의 이후 문자를 대문자로 만들어 반환
* `a.upper()` : 문자열 모두를 대문자로 만들어 반환
* `a.lower()` : 문자열을 모두 소문자로 만들어 반환
* `a.swapcase()` : 대문자는  소문자로, 소문자는 대문자로 반환
* `'x'.join(a)` : iterable한 요소 a (ex.string) 사이사이에 x를 넣어 문자열로 반환
* `a.replace(old, new)` : 영역 안에 있는 old를 new로 바꿔서 반환
* `a.strip(x)` : a에서 x를 제거하여 반환. 단 b를 지정하지 않을 시에는 **공백**을 제거



#### 01-(2) 탐색 및 검증

* `a.find(x)` : a에 있는 x 중 첫번째 x의 인덱스를 반환하며 x가 없을 시에는 **-1**을 반환
* `a.index(x)` : a에 있는 x 중 첫번째 x의 인덱스를 반환하지만 x가 없을 시에는 **error**
* `a.split(x)` : x를 기준으로 문자열a를 나누어 **리스트**로 반환



#### 01-(3) 인덱싱 및 슬라이싱

* `a[n:m]` : 문자열 a 중 인덱스 n부터 인덱스m 전까지만 뽑아서 새로운 문자열로 반환 



### 02. List 메소드 

#### 02-(1) 값 추가 및 삭제

*  `list.append(x)` : list에 x를 추가
* `list.extend(x)` : list에 iterable한 x를 추가 (단, x에서 index에 해당하는 value값 하나씩 추가 > 이로 인해 string의 경우 **알파벳 하나씩 리스트에 추가**된다)
* `list.insert(index, x)` : list의 index 위치에 x를 추가
* `list.remove(x)` : list에서 값이 x인 것을 삭제 (x가 2개 이상일 때 앞에서부터 하나씩 제거)
* `list.pop(index)` : list에서 index 위치에 있는 것을 삭제하고 삭제한 항목을 반환 단 **index가 지정되지 않았으면 마지막 항목을 삭제하고 반환**
* `list.clear()` : 기존의 리스트의 모든 항목을 삭제 ( **원본 파괴/출력 None** )



#### 02-(2) 탐색 및 정렬

*  `list.index(x)` : list에서 x의 index를 반환

* `list.count(x)` : list에서 x 의 갯수를 반환

* `list.sort()` : 기존의 list를 새롭게 정렬 ( **원본 파괴/출력 None** )

  **단** `sorted(list)` : 정렬한 list를 출력 ( **원본은 그대로** )

* `list.reverse()` : 기존의 list를 반대로 뒤집음 ( **원본 파괴/출력 None** )



#### 02-(3) 복사

##### shallow copy (얕은 복사) : list, dict안에 있는 list, dict 까지는 복사하지 못함

* `copied_list = old_list[:]` : old_list를 복사한 list를 출력

##### deep copy (깊은 복사) : 중첩된 상황에서도 내부에 있는 모든 객체까지 복사

* `import copy` + `copied_list = copy.deepcopy(list)` : list를 복사한 copied_list를 출력



### 03. Dictionary 메소드

#### 03-(1) 추가 및 삭제

- `dict.pop(key)` : 기존 dict에서 key에 해당하는 item을 없애고 key에 해당하는 value 값을 반환 (**원본 파괴**). 없는 key를 입력하면 keyerror 발생

  > **단** `dict.pop(key,False)` 기존 dict에 입력한 key가 없을 때는 False를 반환 (False는 대체 가능)

- `dict.update(key= new value)`: 기존 dict에서 key에 해당하는 value값을 new value값으로 대체 ( **원본 파괴/출력 None**)  

  >단 dict[key] = new_value 를 통해 value를 업데이트할 수 있다

- `dict.get(key)` : dict에서 key값에 해당하는 value 값을 반환

  > 단 dict[key] 를 통해서 value값을 반환할 수 있다

  > **단** `dict.get(key not in dict)` : 기존 dict에 없는 key값을 입력할 경우 None을 반환

  > **또한** `dict.get(key, False)` : 기존 dict에 없는 key값을 입력할 경우 False를 반환 (False는 대체 가능)



### 04. Set 메소드

#### 04-(1) 추가 및 삭제

* `set.add(element)` : 기존의 set에 새로운 element를 추가 ( **원본파괴 / 출력None** )

* `set.update(*others)` : 기존의 set에 iterable한 others(여러가지 값)을 추가 ( **원본파괴/출력None** )

  > *others에 dictionary를 넣으면 key값이 추가된다

* `set.remove(element)` : 기존의 set에서 element를 삭제 ( **원본파괴/출력None/없으면 Error** )

* `set.discard(element)` : 기존의 set에서 element를 삭제 ( **원본파괴/출력None** )

* `set.pop()` : 기존의 set에서 가장 작은 원소를 제거하고 반환 ( **원본파괴/출력yes **)



### 05. List Comprehension

#### 05-(1) 간편하게 List 만들기

* `list = [x for x in X (조건)]` : x안에 있는 x들로 새로운 list를 생성 ( 조건이 있을 시에는 뒤에 추가) 

  **x 대신 x.method 또는 function(x)를 넣어도 가능!!!**

  `list = [(x, y) for x in X for y in Y (조건) ]` : 변수가 2개 이상일 때도 사용 가능



### 06. Dictionary Comprehension

#### 06-(1) 간편하게 Dict 만들기

* `dict = { key: value for key, value in dict.items() (조건)}` :  기존의 dict에 있는 key와 value로 새로운 dict을 생성

  `dict = { a: b for a in A for b in B (조건)}` : 리스트 A와 B에 있는 요소를 각각 key와 value로 지정하여 새로운 dict 생성







