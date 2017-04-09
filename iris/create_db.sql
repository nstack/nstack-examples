-- Database: nstack
CREATE SEQUENCE iris_id_seq;

CREATE TABLE iris
(
  iris_id integer NOT NULL DEFAULT nextval('iris_id_seq'::regclass),
  petal_length real NOT NULL,
  petal_width real NOT NULL,
  sepal_length real NOT NULL,
  sepal_width real NOT NULL,

  CONSTRAINT iris_pkey PRIMARY KEY (iris_id)
);

CREATE INDEX iris_iris_id_index ON iris (iris_id);

