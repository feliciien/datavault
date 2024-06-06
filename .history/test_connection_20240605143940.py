import pyodbc
pyodbc.pooling = True

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=your_database_name;'
    'UID=your_username;'
    'PWD=your_password',
    autocommit=True
)
