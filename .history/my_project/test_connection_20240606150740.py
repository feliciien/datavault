import pymssql

try:
    conn = pymssql.connect(
        server='localhost',
        user='sa',
        password='StrongPassword123!',
        database='master'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
    conn.close()
    print("Connection successful!")
except pymssql.DatabaseError as e:
    print(f"Error connecting to database: {e}")
