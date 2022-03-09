-- Bee_Types

-- Select
SELECT type_id, type_name, age, description FROM Bee_Types ORDER BY type_id DESC;

-- Create
INSERT INTO Bee_Types (type_name, age, description) VALUES (%s, %s, %s);

-- Update
UPDATE Bee_Types SET type_name = %s, age = %s, description = %s WHERE type_id = %s;

-- Delete
DELETE FROM Bee_Types WHERE type_id = %s;



----------
-- Tasks
----------

-- Select
SELECT task_id, task_type, description, assignment_length FROM Tasks ORDER BY task_id DESC;

-- Create
INSERT INTO Tasks (task_type, description, assignment_length) VALUES (%s,%s,%s);

-- Update
UPDATE Tasks SET task_type = %s, description = %s, assignment_length = %s WHERE task_id = %s;

-- Delete
DELETE FROM Tasks WHERE task_id = %s;



----------
-- Bees
----------

-- Select
SELECT bee_id, bee_type, dob, bee_name FROM Bees ORDER BY bee_id DESC;

-- Create
INSERT INTO Bees (bee_type, dob, bee_name) VALUES (%s,%s,%s);

-- Update
UPDATE Bees SET bee_type = %s, dob = %s, bee_name = %s WHERE bee_id = %s;

-- Delete
DELETE FROM Bees WHERE bee_id = %s;



----------
-- Cells
----------

-- Select
SELECT cell_id, cell_type, location, size FROM Cells ORDER BY cell_id DESC;

-- Create
INSERT INTO Cells (cell_type, location, size) VALUES (%s,%s,%s);

-- Update
UPDATE Cells SET cell_type = %s, location = %s, size = %s WHERE cell_id = %s;

-- Delete
DELETE FROM Cells WHERE cell_id = %s;



----------
-- Bee_Tasks
----------

-- Select
SELECT bee_id, task_id FROM Bee_Tasks ORDER BY bee_id DESC;

-- Create
INSERT INTO Bee_Tasks (bee_id, task_id) VALUES (%s, %s);

-- Update

-- Delete
DELETE FROM Bee_Tasks WHERE bee_id = %s AND task_id = %s;



----------
-- Task_Cells
----------

-- Select
SELECT task_id, cell_id FROM Task_Cells ORDER BY task_id DESC;

-- Create
INSERT INTO Task_Cells (task_id, cell_id) VALUES (%s, %s);

-- Update

-- Delete
DELETE FROM Task_Cells WHERE task_id = %s AND cell_id = %s;