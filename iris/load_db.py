#!/usr/bin/env python3
import os
import random
import psycopg2

insert_stmt = """
insert into iris (petal_length, petal_width, sepal_length, sepal_width) values (%s, %s, %s, %s);
"""

SAMPLE_SIZE = 20

def insert_row(cur, row_data):
  cur.execute(insert_stmt, row_data)

# Main entrypoint
with psycopg2.connect(os.environ['POSTGRES_CONN']) as conn, \
     conn.cursor() as cur:

    # generate randomised data based on min/max of training set with 10% shift at boundary
    for x in range(0, SAMPLE_SIZE):
        row = (random.uniform(0.9, 7.6), random.uniform(0.1, 2.8), 
               random.uniform(4, 8.5), random.uniform(1.8, 4.8))
        print("R: {}".format(row))
        insert_row(cur, row)

    conn.commit()

