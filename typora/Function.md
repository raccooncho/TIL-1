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



##### 01-(6) Keyword Arguments (키워드 인자)

* 함수는 기본적으로 인수를 위치로 판단하지만 키워드 인자를 사용하면 위치를 무시할 수 있다 



##### 01-(7) 가변 인자 리스트

* 활용법 : `def func(*args):`
* 정해지지 않은 임의의 인자를 받기 위해 가변인자를 활용한다.
* 가변인자는 tuple 형태로 처리된다



##### 01-(8) 정의되지 않은 인자

* 활용법 : `def func(**args):
* **kwagrs를 통해 인자를 받아 처리할 수 있다
* kwagrs는 dict형태로 처리된다



##### 01-(9) dictionary를 인자로 넘기기 (unpacking arguments list)

##### 01-(10) 이름공간 및 스코프(scope)