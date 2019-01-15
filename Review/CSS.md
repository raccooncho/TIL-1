# CSS (cascading style sheet)

## Naming Things (class & id)

* 기능을 의미하는 것으로 이름을 잘 지어야 한다
* 포괄적인 이름은 좋지 않다
* class id를 만들 때 피해야할 것 : 어떻게 보여질지로 id를 정하면 안된다 (보여지는 것은 변경되기 때문에)
* CSS는 가능하면 class를 이용하는 것이 좋다 (java에서 id값을 자주 가져가기 때문에)
* **important 사용하지 말기**
* 우선순위 
  * 수도코드 (절대쓰지말것)
  * 인라인
  * 미디어 커리
  * 사용자 정의
  * class or id
  * 똑같은 css로 정의했을 때 아래에 있는 내용(마지막 또는 최신에 한 것)이 적용된다
  * style sheet에 작성된 것 (class나 id 말고 그냥 적은 것 ex. a, div 등등)
  * 브라우저 default (단 직접 수정할 경우 수정된 것이 위에 네 번째로 올라간다)

* 

## Basic Function

* `<link rel="stylesheet" type="text/css" href="위치"> `  :  css파일을 html에 연결시키기 
* `#id명` : id를 부르는 방법
* `.class명` : class를 부르는 방법
* `.class명 태그명` : 특정 tag안에 있는 class를 부르는 방법 

