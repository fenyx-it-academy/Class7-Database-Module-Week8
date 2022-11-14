BEGIN;


CREATE TABLE IF NOT EXISTS public.students
(
    student_id integer NOT NULL,
    student_name character varying(120) COLLATE pg_catalog."default",
    CONSTRAINT pk_students PRIMARY KEY (student_id)
);

CREATE TABLE IF NOT EXISTS public.teachers
(
    teacher_id integer NOT NULL,
    teacher_name character varying(120) COLLATE pg_catalog."default",
    CONSTRAINT pk_teachers PRIMARY KEY (teacher_id)
);
END;