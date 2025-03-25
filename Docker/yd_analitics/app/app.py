import psycopg2

try:
    conn = psycopg2.connect(
        host="db",
        port=5432,
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    print("✅ Успешное подключение к PostgreSQL!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", e)
    conn.close()