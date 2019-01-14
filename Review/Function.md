# Function

### 01. 개요

##### 01-(1) 활용법

* `def function_name(parameter1, parameter2):` : function의 기본 형태
* 함수는 동작후에 return을 통해 결과값을 전달 할 수도 있다. (단 return값이 없으면, None을 반환)



##### 01-(2) return

* 함수는 모든 객체를 반환할 수 있다.
* 함수는 단 하나의 객체만 반환
* return은 생략 가능



##### 01-(3) parameter(인자/매개변수)

* `parameter` : 함수를 호출할 때 인수로 전달된 값을 내부에서 사용할 수 있게 해주는 변수

* 함수는 parameter(매개변수)를 넘겨줄 수 있다
* parameter(매개변수)가 없는 함수도 있다



##### 01-(4) argument (인수)

* `argument` : 함수가 호출될 때 함수로 값을 전달해주는 변수를 가르킨다
* 함수는 기본적으로 인수를 위치로 판단



##### 01-(5) Default Argument Values (기본값)

* parameter의 value를 미리 정해두면 함수를 사용할 때, parameter를 지정하지 않아도 기본 값(parameter)를 받을 수 있다

  `def my_sum(a, b=0)에서 my_sum(3)으로 입력하면 b는 default값으로 0을 갖는다`



##### 01-(6) Keyword Arguments (키워드 인자)

* 함수는 기본적으로 인수를 위치로 판단하지만 키워드 인자를 사용하면 위치를 무시할 수 있다 

  `def func(a, b)에서 def func(b = 1, a = 2)로 위치를 무시할 수 있다`



##### 01-(7) 가변 인자 리스트

* 활용법 : `def func(*args):`

* 정해지지 않은 임의의 인자를 받기 위해 가변인자를 활용한다.

* 가변인자는 **tuple** 형태로 처리된다

  `def unknown_args(*args): + return(args)`  (args말고 다른 단어도 사용 가능)



##### 01-(8) 정의되지 않은 인자

* 활용법 : `def func(**args):`

* **kwagrs를 통해 인자를 받아 처리할 수 있다

* kwagrs는 **dict**형태로 처리된다

  `def unknown_args(**args): + return(args)`



##### 01-(9) dictionary를 인자로 넘기기 (unpacking arguments list)

* 함수가 복수의 인자를 요구할 때,  인자들을 dictionary로 만들어 넘길 수 있다

  `def func(a, b, c):일때, d1 = {'a': 1, 'b': 2, 'c': 3}을 이용하여 func(**d1)으로 할 수 있다`



##### 01-(10) 이름공간 및 스코프(scope)

* 파이선에서 사용되는 이름들은 이름공간에 저장된다. 그리고 변수에서 값을 찾을 때  `LEGB` 순으로 이름을 찾는다
* `Local scope` : 정의된 함수
* `Enclosed scope` : 상위 함수
* `Global scope` : 함수 밖의 변수 혹은 import된 모듈
* `Buit-in scope` : 파이썬안에 내장되어 있는 함수 또는 속성



### 02. Recursive Function (재귀함수)

##### 02-(1) Recursive Function란?

* `Recursive Function` : 함수 내부에서 자기 자신을 호출하는 함수를 뜻한다
* 재귀함수의 경우 반드시 `base case`가 존재해야 한다
* `base case`는 점점 범위가 줄어들어 반복되지 않는 단계, 즉 최종적으로 도달하는 곳이다



### 03. Map 함수

#### 03-(1) 개요

- `def func(parameter1, parameter2): + return` : 함수의 기본 형태
- 함수는 동작 후 return을 통해 결과값을 전달하는데 return이 없으면 None을 반환

#### 03-(2) (*) Map

- `map(function, iterable)` : iterable한 원소에 function을 적용한 후 그 결과를 map object 형태로 반환

  따라서 map()의 결과에 list() 함수를 적용하면 list로 반환 `ex. list(map(int, strings))`