--  creates a table called first_table in the current database
--  with two columns: id and name
--  id is an integer and name is a string

CREATE TABLE IF NOT EXISTS first_table (
    id INTEGER PRIMARY KEY,
    name varchar(256),
);
