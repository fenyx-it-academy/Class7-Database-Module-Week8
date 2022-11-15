BEGIN;


CREATE TABLE IF NOT EXISTS public.students
(
    student_id integer,
    student_name text,
    PRIMARY KEY (student_id)
);

CREATE TABLE IF NOT EXISTS public.teachers
(
    teacher_id integer,
    teacher_name text,
    PRIMARY KEY (teacher_id)
);

INSERT INTO students (student_id, student_name) VALUES(1, 'Rumeysa');
INSERT INTO students (student_id, student_name) VALUES(2, 'Rama');
INSERT INTO students (student_id, student_name) VALUES(3, 'Zehra');

INSERT INTO teachers (teacher_id, teacher_name) VALUES(1, 'Semih');
INSERT INTO teachers (teacher_id, teacher_name) VALUES(2, 'Irfan');
INSERT INTO teachers (teacher_id, teacher_name) VALUES(3, 'Ceren');

END;