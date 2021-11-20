import psycopg2
import logging

connection=psycopg2.connect(
    host='localhost',
    database='project2',
    user='postgres',
    password='admin',
    port='5432'
)


# print(connection)

jobs_table_query='''
    CREATE TABLE jobs (
        id SERIAL,
        type TEXT NOT NULL,
        location TEXT NOT NULL,
        title TEXT NOT NULL,
        compensation TEXT,
        employees TEXT NOT NULL,
        poster TEXT NOT NULL,
        description TEXT NOT NULL,
        PRIMARY KEY(id)
    )
'''


pointer = connection.cursor()

try:
    pointer.execute(jobs_table_query)
    connection.commit()
    logging.info('Table Created')
except Exception as e:
    logging.error(f'Table Error: {e}')
# finally:
#     connection.close()
