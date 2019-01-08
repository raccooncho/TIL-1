# CLI

### 1. BASIC

##### 1-1 What is CLI?

* GUI : Graphic User Interface로 명령어 입력 없이 마우스로 클릭을 통해 작업을 수행할 수 있다
* CLI : Command Line Interface로 command line(명령어)를 통해 작업을 수행할 수 있다

##### 1-2  Prompt

* 컴퓨터가 새로운 명령어를 받아드릴 준비가 되었음을 보여주는 표시. 이 표시가 떠 있을 때 명령어를 입력해야한다
* 일반적으로 `$` 사인을 사용한다

##### 1-3 간단한 명령어

* `Ctrl+C` : 자신이 입력한 명령어를 취소할 때
* `Ctrl+L` : 터미널을 깔끔하게 만들기 (Clear)
* `Ctrl+D` or `$ exit` : 터미널 및 다른 프로그램 종료
* `$ cat` : 특정 파일의 내용을 볼 때
* `$ ehco` : 화면에 출력하기 (Standard Out)
* `$ man input` : input에 관한 공식 매뉴얼 페이지 보기 (Manual Page)
* `$ touch a`  :  a라는 이름의 새로운 파일을 만들기
* `>` : redirect로 출력물로 파일로 덮는 것을 의미
* `>>` : append로 출력물을 파일에 추가시키는 것을 의미
* `ls` : 현재 디렉토리(폴더) 안에 있는 모든 파일과 디렉토리들을 보여준다 (단 숨겨진 파일은 제외)
* `mv a b` : a파일의 이름을 b파일로 바꾸기
* `cp a b` :  a파일을 b라는 이름으로 복사하기
* `rm a` :  a라는 파일을 삭제하기
* `rm -i a` :  a라는 파일을 삭제하는데 시행 전에 확인하며 y를 입력할 경우 파일이 삭제된다
* `rm -f a` :  a라는 파일을 삭제하는데 확인이나 절차를 무시하고 강제로 삭제한다
* `rm *a` :  a로 끝나는 모든 파일을 삭제하는 wild-card `*`
* `rm b*` :  b로 시작하는 모든 파일을 삭제하는 wild-card `*`
* `command_A | command_B` :  command_A의 출력을 command_B의 입력을 보낸다 
* `wc a` :  a 파일의 글자수 세기
* `grep string a` :  파일 a에서 문자열을 찾기
* `grep -i string a`  :  파일 a에서 문자열을 대소문자 구분 없이 찾기
* `$ ps aux` :  프로세스들을 보여준다
* `kill -15 pid` :  pid 값을 가진 프로세스를 종료
* `pkill -15 -f name`  :  name을 가진 프로세스를 종료



### 2. Manipulating Files - 파일 조작

##### 2-1 Redirecting and appending

```python
$ echo "when i was a young boy" > black_parade.txt
# 문자열이 black_parade.txt에 저장이 되었다
$ cat black_parade.txt
when i was a young boy
# cat 명령어를 통해 black_parade.txt에 저장된 문자열을 확인할 수 있다
$ echo "my father took me into the city" >> black_parade.txt
# black_parade.txt에 있는 마지막 문자열 다음에 새로운 문자열이 추가된다
```

##### 2-2 Listing & New file

```python
$ ls
Desktop
Document
Downloads
Library
black_parede.txt
#현재 디렉토리에 있는 파일과 디렉토리를 보여준다
$ ls -a # 숨긴 파일까지 모두(all) 보여주기
$ ls -l # long-format으로 보여주기
$ ls -t # 가장 최근에 수정된 순서(time)로 보여주기
$ ls -r # 역순(reverse)로 보여주기
```

##### 2-3 Renaming, copying, deleting

```python
$ mv test test_file.txt
# test 파일이 test_file.txt라는 이름으로 바뀐다
$ cp test copy_file.txt
# test 파일이 copy_file.txt라는 이름으로 복사된다
$ rm test
# test 파일이 삭제된다
```

# 3. Inspecting files - 파일 검사

##### 3-1 Downloading a file (through curl)

```python
$ curl -OL neovansoarer.github.io/files/sonnet.txt
# sonnet.txt 파일이 다운로드 된다
```

##### 3-2 Making `head`  and `tail` of it

```python
$ head sonnets.txt
# 첫 열줄만 출력
$ tail sonnets.txt
# 마지막 열줄만 출력
```

##### 3-3 Wordcount `wc` and pipes `|`

```python
$ wc sonnets.txt
2620 17670 95635 sonnets.txt
#줄, 단어, bytes
$ head sonnets.txt | wc
# 첫 열줄의 단어수를 세는 방법
```

##### 3-4 less

```python
$ less sonnets.txt
# sonnets.txt 파일을 미리보기 할 수 있다	
```

`/string` + `enter`  을 통해 찾고 싶은 문자열을 찾아볼 수 있다

##### 3-5 Grepping

`grep string a` :  파일 a에서 문자열을 찾기

`grep -i string a`  :  파일 a에서 문자열을 대소문자 구분 없이 찾기