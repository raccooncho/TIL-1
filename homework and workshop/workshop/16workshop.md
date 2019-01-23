```sqlite
--DB작성
CREATE TABLE bands (
	id INTEGER PRIMARY KEY,
    name TEXT,
    debut INTEGER
);

INSERT INTO bands (name, debut)
VALUES
('Queen', 1973),
('Coldplay', 1998),
('MCR', 2001);

--해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라
ALTER TABLE bands ADD COLUMN members INTEGER;

UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;

--id가 3인 레코드의 members를 5로 수정하라
UPDATE bands SET members=5 WHERE id=3;
--id가 2인 레코드를 삭제하라
DELETE FROM bands WHERE id=2;
```

