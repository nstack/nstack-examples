#!/usr/bin/env python3

import csv
import re
import psycopg2

def parse_row(row):
  # title and year parsing
  title_year = row[1].split("(")
  title = title_year[0].strip()
  if len(title_year) == 2:
    year = int(title_year[1][0:4])
  else:
    year = None

  if row[2] == "(no genres listed)":
    categories = []
  else:
    categories = row[2].split("|")
  
  print("T: {}, Y: {}, C: {}".format(title, year, categories))
  return (title, year, categories)

insert_stmt = """
with f1 as (
  insert into film (title, release_year) values (%s, %s) returning film_id
)
, c1 as (
  select category_id from category
  where name = any(%s)
)
insert into film_category (film_id, category_id) 
  (select f1.film_id, c1.category_id
  from f1 cross join c1)
;
"""

def insert_row(cur, row_data):
  cur.execute(insert_stmt, row_data)

# Main entrypoint
with open('movies.csv', newline='') as csvfile, \
     psycopg2.connect("dbname=movies") as conn, \
     conn.cursor() as cur:
  rows = csv.reader(csvfile, delimiter=',', quotechar='"')  
  next(rows, None) # skip header
  for row in rows:
    insert_row(cur, parse_row(row))
  conn.commit()

