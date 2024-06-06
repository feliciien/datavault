import pyodbc
pyodbc.pooling = True

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'  # or the hostname/IP address of your SQL Server instance
    'DATABASE=mydatabase;'  # replace with your database name
    'UID=sa;'  # replace with your username
    'PWD=mysecretpassword;',  # replace with your password
    autocommit=True
)