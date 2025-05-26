import psycopg2

# Try connecting to the default 'postgres' database first
CONNECT_DB_NAME = "postgres" # CHANGED for initial connection
TARGET_DB_NAME = "healthcare" # The database we actually want to check for

DB_USER = "postgres"
DB_PASS = "qelol669"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

print(f"Attempting to connect to default database: {CONNECT_DB_NAME} on {DB_HOST}:{DB_PORT} as user: {DB_USER}")

try:
    conn = psycopg2.connect(
        dbname=CONNECT_DB_NAME, # Use the default 'postgres' db for connection
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Connection to default database successful!")
    cur = conn.cursor()
    
    print("Executing: SELECT version();")
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print(f"PostgreSQL Version: {db_version[0] if db_version else 'Not found'}")
    
    print(f"Checking if database '{TARGET_DB_NAME}' exists by querying pg_database...")
    # Use parameterized query for safety, though TARGET_DB_NAME is from a variable here
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (TARGET_DB_NAME,))
    db_exists = cur.fetchone()
    
    if db_exists:
        print(f"Database '{TARGET_DB_NAME}' IS LISTED in pg_database.")
    else:
        print(f"Database '{TARGET_DB_NAME}' IS NOT LISTED in pg_database.")

    cur.close()
    conn.close()
    print("Connection closed.")

except psycopg2.OperationalError as e:
    print(f"Connection to {CONNECT_DB_NAME} failed - OperationalError:")
    print(e)
except Exception as e:
    print(f"Connection to {CONNECT_DB_NAME} failed - Other Exception:")
    print(e)
