DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS Bees;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Cells;

--Remove these-------------------------------------------
CREATE TABLE user (                                    --
  id INTEGER PRIMARY KEY AUTOINCREMENT,                --
  username TEXT UNIQUE NOT NULL,                       --
  password TEXT NOT NULL                               --
);                                                     --
                                                       --
CREATE TABLE post (                                    --
  id INTEGER PRIMARY KEY AUTOINCREMENT,                --
  author_id INTEGER NOT NULL,                          --
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,--
  title TEXT NOT NULL,                                 --
  body TEXT NOT NULL,                                  --
  FOREIGN KEY (author_id) REFERENCES user (id)         --
);                                                     --
--Remove these-------------------------------------------

CREATE TABLE Bees (
  bee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  bee_type INTEGER NOT NULL,
  dob DATE NOT NULL,
  bee_name VARCHAR(255) NOT NULL
);

CREATE TABLE Cells (
  cell_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  cell_type VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL,
  size INTEGER NOT NULL
);

CREATE TABLE Tasks (
  task_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  task_type VARCHAR(255) NOT NULL,
  description VARCHAR(1000) NOT NULL,
  assignment_length INTEGER
);

CREATE TABLE Bee_Types (
  type_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  type_name VARCHAR(255) NOT NULL,
  age VARCHAR(10) NOT NULL,
  description VARCHAR(1000) NOT NULL
);