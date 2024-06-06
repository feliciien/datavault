import pyodbc
pyodbc.pooling = False

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=your_sql_server_host;'
    'DATABASE=your_database_name;'
    'UID=your_username;'
    'PWD=your_password',
    autocommit=True
)
