import pyodbc

try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_sql_server_host;'
        'DATABASE=sqlserver;'
        'UID=your_username;'
        'PWD=your_password'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    row = cursor.fetchone()
    print("Connection successful, fetched row:", row)
except Exception as e:
    print("Error connecting to database:", e)
/opt/homebrew/bin/sqlcmd -S localhost,1433 -U sa -P 'YourStrong!Passw0rd' -Q "CREATE DATABASE sqlserver;"a
