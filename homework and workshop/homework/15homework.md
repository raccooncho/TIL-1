```sqlite
CREATE TABLE  friends (
	id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT
);

INSERT INTO friends (name, location)
VALUES
('Justin', 'Seoul'),
('Simon', 'New York'),
('Chang', 'Las Vegas'),
('John', 'Sydney');

ALTER TABLE friends ADD COLUMN married INTEGER;

UPDATE friends SET married=1 WHERE id in (1, 4);
UPDATE friends SET married=0 WHERE id in (2, 3);

DELETE FROM friends WHERE married=0;
```

