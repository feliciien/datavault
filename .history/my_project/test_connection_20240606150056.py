import pyodbc

try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=my_database;'
        'UID=my_user;'
        'PWD=StrongPassword123!',
        timeout=30  # Increase timeout to 30 seconds
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    row = cursor.fetchone()
    print("Connection successful, fetched row:", row)
except Exception as e:
    print("Error connecting to database:", e)
