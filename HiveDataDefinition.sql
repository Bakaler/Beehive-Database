-- Drops
DROP TABLE IF EXISTS Bee_Tasks;
DROP TABLE IF EXISTS Task_Cells;
DROP TABLE IF EXISTS Bees;
DROP TABLE IF EXISTS Cells;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Bee_Types;


-- Create Tables

CREATE TABLE Bee_Types (
  type_id INTEGER AUTO_INCREMENT NOT NULL,
  type_name VARCHAR(255) NOT NULL,
  age VARCHAR(10) NOT NULL,
  description VARCHAR(1000) NOT NULL,
  PRIMARY KEY (type_id)
);

CREATE TABLE Bees(
    bee_id INTEGER AUTO_INCREMENT NOT NULL,
    bee_type INTEGER,
    dob DATE NOT NULL,
    bee_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (bee_id), 
    FOREIGN KEY (bee_type)
    REFERENCES Bee_Types(type_id)
    ON DELETE SET NULL
);

CREATE TABLE Cells (
    cell_id INTEGER AUTO_INCREMENT NOT NULL,
    cell_type VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    size INTEGER NOT NULL,
    PRIMARY KEY (cell_id)
);

CREATE TABLE Tasks(
    task_id INTEGER AUTO_INCREMENT NOT NULL,
    task_type VARCHAR(255) NOT NULL,
    description VARCHAR(1000) NOT NULL,
    assignment_length INTEGER NOT NULL,
    PRIMARY KEY (task_id)
);

CREATE TABLE Bee_Tasks(
    bee_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    PRIMARY KEY (bee_id, task_id), 
    FOREIGN KEY (bee_id)
    REFERENCES Bees(bee_id)
    ON DELETE CASCADE,
    FOREIGN KEY (task_id)
    REFERENCES Tasks(task_id)
    ON DELETE CASCADE
);

CREATE TABLE Task_Cells(
    cell_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    PRIMARY KEY (cell_id, task_id), 
    FOREIGN KEY (cell_id)
    REFERENCES Cells(cell_id)
    ON DELETE CASCADE,
    FOREIGN KEY (task_id)
    REFERENCES Tasks(task_id)
    ON DELETE CASCADE
);

-- Fill Tables

-- Bee Types
INSERT INTO Bee_Types (type_name, age, description) VALUES
("HouseKeeper", "1-2", "Cleans the cell and keeps the brood warm"),
("Nurse", "3-5", "Feeds older larvae with honey and pollen"),
("Nanny", "6-11", "Feeds younger larvae with royal jelly"),
("Builder", "12-17", "Produces wax and constructs combs, ripens honey"),
("Guard", "18-21", "Guards the hive entrance and ventilates the hive"),
("Forager", "22-35", "Gathers pollen, nectar, propolis, and water for the hive");

-- Tasks
INSERT INTO Tasks (task_type, description, assignment_length) VALUES
("Honeycomb Cleaner", "Cleans honeycombs and keeps honey at a warm tempature", 1),
("Brood Cleaner", "Cleans brood cells and keeps brood warm", 1),
("Larvae Nurse", "Gathers honey from hive and feeds older larvae", 3),
("Larvae Nanny", "Gathers royal jelly from hive to feed young larvae", 5),
("Nurse", "Kills and removes injured or sick larvae", 5),
("Royal Nurse", "Cares for and keeps eggs warm", 5),
("Supervisor", "Assigns daily hive maintance duties including comb construction", 5),
("Carpenter", "Builds new hive combs and repairs damages", 2),
("Converter", "Converts pollen into building materials for carpenters", 4),
("Enterance Guard", "Refuses entrance from bees carrying in diseases and infections", 3),
("Venetilator", "Ensures proper hive ventilation", 3),
("Royal Gaurd", "Attacks invaders and protects the hive, usually with their life", 3),
("Scout", "Finds new flower pathcehs for foragers", 3),
("Hydro Homie", "Collects water for the hive", 5),
("Forager", "Collects pollen for the hive", 5),
("Pollen Alchemy", "Converts pollen into honey", 2);

-- Bees

INSERT INTO Bees (bee_type, dob, bee_name) VALUES
(1, "1995-11-29", "McBuzzin"),
(2, "1996-10-11", "Cardi Bee"),
(3, "1997-09-14", "Buzz Lightyear"),
(4, "1998-08-23", "Black Eyed Bee"),
(5, "1999-07-05", "Marty McFly"),
(6, "2000-06-02", "Beeyonce");

-- Cells

INSERT INTO Cells (cell_type, location, size) VALUES
("HoneyComb", "CellBlock-A", 10),
("Entrance", "CellBlock-B", 10),
("Lair", "CellBlock-C", 10),
("Hive Wall", "CellBlock-D", 10),
("Hatchery", "CellBlock-E", 10),
("Spawning", "CellBlock-F", 10);

-- Bee_Tasks

INSERT INTO Bee_Tasks (bee_id, task_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6);

-- Task_Cells

INSERT INTO Task_Cells (cell_id, task_id) VALUES
(1, 6),
(2, 5),
(3, 4),
(4, 3),
(5, 2),
(6, 1);

