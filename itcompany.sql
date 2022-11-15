BEGIN;


CREATE TABLE IF NOT EXISTS public.customers
(
    customer_id integer,
    first_name text,
    last_name text,
    phone integer,
    email text,
    PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS public.orders
(
    order_id integer,
    customer_id integer,
    product_id integer,
    order_date date,
    employee_id integer,
    PRIMARY KEY (order_id)
);

CREATE TABLE IF NOT EXISTS public.product
(
    product_id integer,
    name text,
    product_statement text,
    employee_id integer,
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS public.team
(
    employee_id integer,
    name text,
    phone integer,
    email text,
    "position" text,
    PRIMARY KEY (employee_id)
);

ALTER TABLE IF EXISTS public.orders
    ADD FOREIGN KEY (customer_id)
    REFERENCES public.customers (customer_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.orders
    ADD FOREIGN KEY (product_id)
    REFERENCES public.product (product_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.orders
    ADD FOREIGN KEY (employee_id)
    REFERENCES public.team (employee_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.product
    ADD FOREIGN KEY (employee_id)
    REFERENCES public.team (employee_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;