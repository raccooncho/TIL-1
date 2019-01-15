# HTML

### 01. 기본 tag

인용구 : `blockquote`  (한칸 들이기)

li*3 후에 tab(또는 enter)을 누르면 3개가 만들어짐

* `iframe` : 미디어 관련을 가져오는  방법
* `table>tr>th*3` table 한번에 만들기
* `<div></div>`의 경우 전체 영역을 갖는다 (전체 네모 박스)
* `<span></span>` 의 경우 문자열이 있는 곳까지만 영역을 갖는다 (마지막 글자가 끝나는 곳)
* `<em></em>` : 중요한 부분을 기울게 하여 강조하기
* `<strong></strong>` : 중요한 부분을 굵게 하여 강조하기
* `<br>` : 문장바꾸기 (enter 기능)
* `<ul></ul> 안에 <li></li>` 를 통해 unodered list tag를 만들 수 있다
* `<ol></ol> 안에 <li></li>` 를 통해 ordered list tag를 만들 수 있다
* `<img src="image-location.jpg" />` 를 통해 이미지를 삽입할 수 있다
* `<img src="image-location.jpg" alt="string"/>` 을 통해 이미지를 호출하지 못할 때 대신 string을 출력할 수 있다
* `<video src="viedo.mp4" width="320" height="240" controls> Video not supported </video>` 를 통해 통영상을 출력하며 Video not supported의 경우 브라우저가 동영상을 재생할 수 없을 때 출력된다. controls는 기본적인 기능인 pause, play, skip을 가진다는 것을 의미한다
* `<a href="링크" target="_blank"></a>` 를 통해 링크를 삽입할 수 있다. 여기서 `a` 는 anchor로 닻을 의미한다. 그리고 `target="_blank"` 의 경우 링크를 새로운 창에서 열라는 것을 의미한다
* `<p id="특정이름">` 식으로 위치를 id를 지정해두면 `<a href="#특정이름">문구</a>`를 통해 바로 접근할 수 있다
* `<!--주석처리할 내용-->` 를 통해 주석 처리할 수 있다 . `ctrl + /로 만들 수 있다`
* `<hr>` : 직선 만들기



### 02. Table 만들기

* `<table></table>`을 통해 테이블을 만들 수 있다
* `<tr></tr>` 을 통해 테이블 row를 만들고 반복하여 row를 추가할 수 있다
* `<th></th>` 를 통해 테이블 heading을 만들 수 있고 `<td></td>` 로 안에 데이터를 채울 수 있다
* `<td colspan="2"></td>` 를 통해 테이블을 합칠 수 있다 (column 가로)
* `<td rowspan="2"></td>` 를 통해 테이블을 합칠 수 있다 (row 세로)
* `<tbody></tbody>` 를 통해 row가 긴 테이블을 만들 수 있다. body안에 row를 많이 넣는다
* `<thead></thead>` 를 통해 테이블의 윗부분을 만들 수 있다 (변수명 등을 위해 사용)
* `<tfoot></tfoot>` 를 통해 테이블의 아랫부분을 만들 수 있다 (합계 등을 위해 사용)



### 03. Form 기능 이용하기 (서버에 정보를 POST하기)

* `<form action="정보를 받을 곳.html" method="POST"></form>` 을 통해 html에 새로운 정보를 post할 수 있다
* `<input type="text" name="id"/>` 를 통해 입력창을 만들 수 있다 
* `<input type="text" placeholder="회색글씨" />` 을 사용하면 hint를 활용할 수 있다
* `<form>과 </form>` 사이에 `input type=""~` 를 넣으면 거기서 얻는 정보가 `value="입력한 문자"`로 바뀌고  `"id=입력한문자" `가 `정보를 받을 곳.html`에 보내진다
* `<label>표시할텍스트</label>` 를 통해 입력창에 위에 텍스트를 보여줄 수 있다
* `<label for="input의 id">표시할텍스트</label>` 을 이용해 라벨이 어느 것을 설명하기 위한 것인지 표시 할 수 있다
* `<input type="passward" id="user-password nama="user-password>` 을 이용하면 비밀번호 입력창 같이 *** 로 채울 수 있다
* `<input type="number">` 로 하면 숫자만 입력이 가능하다
* `<textarea></textarea>` 로 하면 텍스트 입력창의 크기를 조절할 수 있다
* `<input type="date">` 를 사용할 경우 달력을 가져올 수 있다
* 



