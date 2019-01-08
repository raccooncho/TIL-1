### 20190104

### OS & Command Line Interface

git bash는 unix 입력어를 cmd (windows)로 전환해준다.

ls : 현재 내 위치에 있는 모든 파일을 보여줘라

pwd : 현재 위치의 파일 경로를 알려줌 /c/Users/student (맨앞에 /가 내 컴퓨터를 의미)

ls -a : all 옵션을 의미 "."이 붙은 것도 모두 보여주라는 것을 의미 (.은 숨김파일을 의미한다)

cd : 특정 디렉토리(폴더)로 이동

cd .. : 자기 전 단계 디렉토리로 이동

. : 현재 자기가 있는 곳을 의미한다 이를 이용해 git add . 으로 현재 있는 모든 것을 깃에 add하는 기능

cd ~ : 가장 기본적인 디렉토리로 이동 (/ (root dir) 바로 아래에 존재하는 권한 없이 접근할 수 있는 디렉토리)

cf) ~은 home이라고 부른다

touch : 파일을 만들기 ex) touch classmate.txt

저장하기 ?

나가기 ?

### CLI

mnoko:~/workspace : 내 위치를 의미

$  :  프롬프트 > 지금 입력을 할 수 있다는 것을 의미

ctrl + c : 취소하기

^ :  ctrl를 의미한다

echo : print문을 의미, string으로 쓸 수 있다 - 정확하게는 표준 출력을 의미

man echo : echo에 대한 메뉴얼 > 여기서는 q를 눌러야 나갈 수 있다

위아래 버튼 : 이전과 다음 명령어를 볼 수 있다

좌우 버튼 : 커서가 좌우로 움직인다

ctrl + p : 이전 명령어

clear (ctrl + l) : 화면를 위로 쭉 미루기

 ctrl + d : 아예 터미널(프로그램)을 꺼버리는 것

sleep 100s : 100초 동안 멈추기 - ctrl + c를 통해 중간에 깨울 수 있다

##### echo

echo "When I was a young boy" > black_parade.txt : 텍스트 파일 만들고 출력물로 파일을 덮기

echo 'to the black' >> black_parade.txt  : 다음 줄에 출력물을 붙이기

##### cat

cat black_parade.txt : 해당 파일을 열어보는 방법 (cat는 해당 파일의 출력을 확인하는 방법)

cat line_1.txt >> song.txt : song에다가 line_1을 추가하기 (그냥 이어서 두개를 써도 가능하다)

##### ls

ls : 폴더들 보여주기

ls -a : hidden 파일까지 모두 보여주기 (.name)

ls -l : 파일을 자세하게 길게 보여주기

ls -al : a옵션과 l옵션을 동시에 보여주기

*이름 앞에 d가 붙어 있으면 디렉토리(폴더)

*이름 앞에 /이 붙어 있으면 파일

ls name : name을 이름으로 가진 파일이 있으면 보여주고 없으면 없다고 한다

ls a* : a로 시작하는 파일이 있으면 보여주고 없으면 없다고 한다

##### 기본적인 명령어

mv old new : 이름바꾸기

cp old new : 복사하기

rm .hidden : 지우기

rm -i .hidden : 지울 것인지 물어보고 y를 입력하면 지울 수 있다

rm -f .hidden : 권한이 없는 파일조차 강제로 지우는 방법 (위험)

rm *.txt : 확장자명이 txt인 것을 모두 지우기 (와일드카드 사용)

rm *a : a로 시하는 것 모두 삭제

rm * : 그냥 있는 것 다 삭제

head name : name의 파일의 맨 위 10줄만 보기

tail name : name의 파일의 맨 아래 10줄만 보기

head sonnets.txt | wc  : |앞의 표준 출력을 | 뒤에 넣는 것을 의미한다. 여기서는 sonnets의 앞 10줄을 얻어오고 이를 wc로 글자수를 분석한다

less name : 이름을 가진 파일을 뷰어로 보기

grep rose sonnets.txt : rose라는 단어를 sonnets.txt에서 찾겠다

ps aux : 현재 사용하고 프로세스를 보여주는 것

top : 컴퓨터에서 리소스 가장 많이 잡아 먹는 것을 보여주는 기능

sudo 명령어 : 모든 명령어는 강제적으로 실행할 수 있다 -f보다 더 강력한 경우

mkdir name : name을 가진 폴더를 생성

mkdir -p ssafy/ss3/students : ssafy 아래에 ss3 아래에 students를 만들기

rm -rf : 폴더와 폴더 안에 있는 것 모두 삭제



### / name

원하는 단어 찾기 ctrl + f와 같은 기능

### curl

which curl : curl 이 있는지 확인

which name : name을 가진 것이 있다면 어디에 있는지 말해주는 기능

