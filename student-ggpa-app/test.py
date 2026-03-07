import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ggpa_db",
    user="postgres",
    password="postgres"
)
print("Connected successfully!")
conn.close()