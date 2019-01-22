```sqlite
CREATE TABLE bands (
	id INTEGER PRIMARY KEY,
    name TEXT,
    debut INTEGER
);

INSERT INTO bands (name, debut)
VALUES ('Queen', 1973), ('Coldplay', 1998), ('MCR', 2001);
```

```sqlite
SELECT id, name FROM bands;
```

```sqlite
SELECT name FROM bands WHERE debut < 2000;
```

