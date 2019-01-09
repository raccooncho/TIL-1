# Data Structure

### 01. String 메소드

#### 01-(1) 변형

* `a.capitalize()`  : 앞글자를 대문자로 만들어 반환
* `a.title()` : 어퍼스트로피 `'` or ` `  (공백) 의 이후 문자를 대문자로 만들어 반환
* `a.upper()` : 문자열 모두를 대문자로 만들어 반환
* `a.lower()` : 문자열을 모두 소문자로 만들어 반환
* `a.swapcase()` : 대문자는  소문자로, 소문자는 대문자로 반환
* `'a'.join(x)` : iterable한 요소 x 사이사이에 a를 넣어 문자열로 반환
* `a.replace(old, new)` : 영역 안에 있는 old를 new로 바꿔서 반환
* `a.strip(x)` : a에서 b를 제거하여 반환. 단 b를 지정하지 않을 시에는 공백을 제거



#### 01-(2) 탐색 및 검증

* `a.find(x)` : a에 있는 x 중 첫번째 x의 인덱스를 반환하며 x가 없을 시에는 -1을 반환
* `a.index(x)` : a에 있는 x 중 첫번째 x의 인덱스를 반환하지만 x가 없을 시에는 error
* `a.split(x)` : x를 기준으로 a 문자열을 나누어 **리스트**로 반환



### 02. List 메소드 

#### 02-(1) 값 추가 및 삭제

*  `list.append(x)` : list에 x를 추가
* `list.extend(x)` : list에 iterable한 x를 추가
* `list.insert(index, x)` : list의 index 위치에 x를 추가
* `list.remove(x)` : list에서 값이 x인 것을 삭제 (x가 2개 이상일 때 앞에서부터 하나씩 제거)
* `list.pop(index)` : list에서 index 위치에 있는 것을 삭제하고 삭제한 항목을 반환 단 index가 지정되지 않았으면 마지막 항목을 삭제하고 반환
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

### 04. Set 메소드

### 05. List Comprehension

### 06. Dictionary Comprehension



