Scott Chapman - 101233571
Steps to run the code:
On pgAdmin 4, set up a server with a db called a3db, fill in the empty DB_USER, DB_PASS, DB_HOST and DB_PORT then save the file.
Then to set up the database run these in the db's query line (or use the a3p1dbCreation.sql file):

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

CREATE SEQUENCE counter;

ALTER TABLE students ALTER COLUMN student_id SET DEFAULT NEXTVAL('counter');

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

In your terminal, enter:
pip install psycopg2
to install psycopg2
When all that is done, run the file with "python .\a3p1.py"


link to the youtube video:
https://youtu.be/WpgsZDJx69I
