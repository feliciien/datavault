import pyodbc

connection = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=your_sql_server_host;'
    'DATABASE=your_database_name;'
    'UID=your_username;'
    'PWD=your_password'
)
cursor = connection.cursor()
cursor.execute("SELECT 1")
row = cursor.fetchone()
print(row)
a