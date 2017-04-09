-- Database: nstack
CREATE SEQUENCE category_id_seq;
CREATE SEQUENCE film_id_seq;
CREATE SEQUENCE output_id_seq;

CREATE DOMAIN year
  AS integer
  CONSTRAINT year_check CHECK (VALUE >= 1901 AND VALUE <= 2155);

CREATE TABLE category
(
  category_id integer NOT NULL DEFAULT nextval('category_id_seq'::regclass),
  name character varying(25) NOT NULL,
  CONSTRAINT category_pkey PRIMARY KEY (category_id)
);

CREATE TABLE film
(
  film_id integer NOT NULL DEFAULT nextval('film_id_seq'::regclass),
  title character varying(255) NOT NULL,
  release_year year,
  CONSTRAINT film_pkey PRIMARY KEY (film_id)
);

CREATE TABLE film_category
(
  film_id integer NOT NULL,
  category_id integer NOT NULL,
  CONSTRAINT film_category_pkey PRIMARY KEY (film_id, category_id),
  CONSTRAINT film_category_category_id_fkey FOREIGN KEY (category_id)
      REFERENCES category (category_id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT film_category_film_id_fkey FOREIGN KEY (film_id)
      REFERENCES film (film_id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE output
(
  output_id integer NOT NULL DEFAULT nextval('output_id_seq'::regclass),
  title character varying(255) NOT NULL,
  name character varying(25) NOT NULL,
  score integer NOT NULL,
  poster bytea NOT NULL,
  CONSTRAINT output_pkey PRIMARY KEY (output_id)
);


CREATE INDEX film_film_id_index ON film (film_id);
CREATE INDEX category_category_id_index ON category (category_id);
CREATE INDEX film_category_film_id_index ON film_category (film_id);
CREATE INDEX film_category_category_id_index ON film_category (category_id);


-- pre-load categories
insert into category (name) values 
  ('Action'),
  ('Adventure'),
  ('Animation'),
  ('Children'),
  ('Comedy'),
  ('Crime'),
  ('Documentary'),
  ('Drama'),
  ('Fantasy'),
  ('Film-Noir'),
  ('Horror'),
  ('Musical'),
  ('Mystery'),
  ('Romance'),
  ('Sci-Fi'),
  ('Thriller'),
  ('War'),
  ('Western');
