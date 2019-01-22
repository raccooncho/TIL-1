# SQL

### 1. scheme

| column | datatype |
| :----: | :------: |
|   id   |   INT    |
|  age   |   INT    |
| phone  |   TEXT   |
| email  |   TEXT   |

### 2. sqlite

### Data 생성 (Create)

```sqlite
--shell에서
sqlite> CREATE TABLE menus (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT, --AUTOINCREMENT는 자동으로 숫자가 상승
   ...> menu1 TEXT NOT NULL, --빈칸이면 안되는 것
   ...> menu2 TEXT
   ...> );
```

##### data 생성

```sqlite
--파일명: insert_record.sql
INSERT INTO computers (year, company, model)
VALUES
(2018, 'Samsung', 'Series9'),
(2019, 'LG', 'Gram17');
```

##### 





##### 02. 테이블에 정보 넣기

```sqlite
--shell에서
sqlite> INSERT INTO menus (id, menu1, menu2)
   ...> VALUES (1, 'Pho', 'Pork');
```

### Date 조회 (Read, Retrieve)

```sqlite
--shell에서
sqlite> SELECT id FROM menus WHERE id=1;    --id가 1인 것에서 id를 가져오기
1
sqlite> SELECT id, menu1, menu2 FROM menus WHERE id=1; --id가 1인 것에서 여러 항목 가져오기
1|Pho|Pork
sqlite> SELECT * FROM menus      --메뉴에서 모든 것을 가져오기
```

##### 04. id값을 자동으로 지정하기

```sqlite
--파일명:create_table.sql
CREATE TABLE computers (
    id INT PRIMARY KEY,   --PRIMARY KEY를 통해 자동으로 지정 가능하다
    year INT,
    company TEXT,
    model TEXT
);
```

##### 06. 확인하기

```sqlite
--terminal(shell)에서
.read create_table.sql
.read insert_record.sql 를 입력하면 된다
확인하기 위해서
SELECT * FROM computers를 통해 확인한다
```

##### 07. TABLE 삭제

```sqlite
DROP TABLE <table_name>;
```

##### 08. TABLE 이름 수정

```sqlite
ALTER TABLE <table_name> RENAME TO <new_table_name>;
```

##### 09. SQLITE 명령어

```sqlite
--SQLITE에서
.mode column : column
.mode csv : csv처럼 보인다
.headers on : 헤더가 같이 보인다
.read <file.sql> : 해당 sql 스크립트 실행
.import <file.name> <table_name> : 해당 파일의 데이터를 지정한 테이블에 import
.schema : 모든 테이블의 schema 확인
```

### DATA 수정 (Update)

```sqlite
UPDATE <table_name>
SET <col_1>=<val_1>, <col_2>=<val_2>, .....
WHERE [condition]; -- 보통 primary key (id)로 선택
```

### DATA 삭제 (Delete, Destroy)

```sqlite
DELETE FROM <table_name>
WHERE [condition]; --보통 primary key (id) 로 선택
```

### Expression

* 해당 column의 갯수

```sqlite
SELECT COUNT(<col>) FROM <table_name>;
```

* 해당 column의 평균

* 해당 column의 총합

* 해당 column의 최대

* 해당 column의 최소

```sqlite
SELECT AVG(<col>) FROM <table_name>
SELECT SUM(<col>) FROM <table_name>
SELECT MIN(<col>) FROM <table_name>
SELECT MAX(<col>) FROM <table_name>
```

### 정렬(order)

```sqlite
SELECT <col> FROM <table_name>
ORDER BY <col_1> , <col_2> [ASC | DESC];  --ASC:오름차순 DESC:내림차순
```

### 제한(limit)

```sqlite
SELECT <col> FROM <table_name>
LIMIT <num>   --'몇개만'을 의미
```

### 제한과 정렬을 섞어서 쓰기

```sqlite
--7. 나이순으로 오름차순으로 정렬하여 상위 10개만
SELECT * FROM users ORDER BY age ASC LIMIT 10;
```

### 패턴(pattern)

```sqlite
SELECT * FROM <table_name>
WHERE <col> LIKE '<pattern>'
```

| 시작 | 예시    | 설명                                  |
| ---- | ------- | ------------------------------------- |
| `%`  | `2%`    | 2로 시작하는 값                       |
|      | `%2`    | 2로 끝나는 값                         |
|      | `%2%`   | 2가 들어가는 값                       |
| `_`  | _2      | 두번째 글자가 2인 값                  |
|      | 1____   | 1로 시작하며 4자리                    |
|      | _2%     | 한글자 뒤에 2가 오고 뒤에 이어지는 값 |
|      | `2_%_%` | 2로 시작하고 최소 3자리인 값          |

