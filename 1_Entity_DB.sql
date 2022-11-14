BEGIN;


CREATE TABLE IF NOT EXISTS public."Team"
(
    "Employee_ID" serial NOT NULL DEFAULT nextval('tem_id_seq'::regclass),
    "Employee_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Employee_Phone" integer NOT NULL,
    "Employee_Roll" character varying COLLATE pg_catalog."default" NOT NULL,
    "Employee_Email" character varying NOT NULL,
    CONSTRAINT team_pkey PRIMARY KEY ("Employee_ID")
);

CREATE TABLE IF NOT EXISTS public."Custumers"
(
    "Customer_ID" serial NOT NULL DEFAULT nextval('tem_id_seq'::regclass),
    "Customer_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Customer_Phone" integer NOT NULL,
    "Customer_Email" character varying NOT NULL,
    CONSTRAINT "Custumers_pkey" PRIMARY KEY ("Customer_ID")
);

CREATE TABLE IF NOT EXISTS public."Product"
(
    "Product_ID" serial NOT NULL DEFAULT nextval('tem_id_seq'::regclass),
    "Product_Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Product_Developer" character varying NOT NULL,
    CONSTRAINT "Product_pkey" PRIMARY KEY ("Product_ID")
);

CREATE TABLE IF NOT EXISTS public."Orders"
(
    "Order_ID" serial NOT NULL DEFAULT nextval('tem_id_seq'::regclass),
    "Customer_ID" integer NOT NULL,
    "Order_Date" date NOT NULL,
    "Product_ID" integer NOT NULL,
    "Order_Developer" integer NOT NULL,
    CONSTRAINT "Order_pkey" PRIMARY KEY ("Order_ID")
);

ALTER TABLE IF EXISTS public."Product"
    ADD CONSTRAINT "fk_Product_Developer" FOREIGN KEY ("Product_Developer")
    REFERENCES public."Team" ("Employee_ID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Orders"
    ADD CONSTRAINT "fk_Custumer_ID" FOREIGN KEY ("Customer_ID")
    REFERENCES public."Custumers" ("Customer_ID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Orders"
    ADD CONSTRAINT "fk_Product_ID" FOREIGN KEY ("Product_ID")
    REFERENCES public."Product" ("Product_ID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."Orders"
    ADD CONSTRAINT "fk_Developer_ID" FOREIGN KEY ("Order_Developer")
    REFERENCES public."Product" ("Product_Developer") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;