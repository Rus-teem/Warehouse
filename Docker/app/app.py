import psycopg2

conn = psycopg2.connect(
    host="db",
    port=5432,
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

print("✅ Успешное подключение к PostgreSQL!")

conn.close()