import psycopg2
connection = psycopg2.connect(
    host = 'database-3.crwje1myrxfu.us-west-1.rds.amazonaws.com',
    port = 5432,
    user = 'postgres',
    password = 'passwords',
    database= 'postgres'
    )
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Revenues(
id SERIAL PRIMARY KEY,
quarter text,
company text,
ticker text,
indicator text,
unit text,
amount integer)""")

connection.commit()

import pandas as pd

sql = """
SELECT "table_name","column_name", "data_type", "table_schema"
FROM INFORMATION_SCHEMA.COLUMNS
WHERE "table_schema" = 'public'
ORDER BY table_name  
"""
df = pd.read_sql(sql, con=connection)
print (df)

\copy revenues from '/New Folder/df_new.csv' WITH DELIMITER ',' CSV;

connection.commit()