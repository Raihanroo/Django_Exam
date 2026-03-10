import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="AsH@b124568",
        host="db.xagnehidrqjpkzsmguvn.supabase.co",
        port="5432",
    )

    cursor = conn.cursor()
    cursor.execute("SELECT version();")

    db_version = cursor.fetchone()
    print("Connected successfully!")
    print("PostgreSQL version:", db_version)

    cursor.close()
    conn.close()

except Exception as e:
    print("Connection failed!")
    print("Error:", e)
