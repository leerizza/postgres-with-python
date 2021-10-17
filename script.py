import pandas as pd
from pandas.io import gbq
import psycopg2 as db
from google.cloud import bigquery



db_host="127.0.0.1";
db_port="10022";
db_name="postgres";
db_user="postgres";
db_pass="P@ssw0rd";

conn =  db.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host, port=db_port);

cur = conn.cursor()
cur.execute("SELECT count(*) FROM datastaging_1.transactions limit 10;")

rows = cur.fetchall()

for r in rows:
    print(f"{r[0]}")



conn.commit()

cur.close()
conn.close()
