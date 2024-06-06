from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

try:
    connection_string = (
        "mssql+pyodbc://sa:StrongPassword123!@localhost:1433/master"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        for row in result:
            print(row)
    print("Connection successful!")
except SQLAlchemyError as e:
    print(f"Error connecting to database: {e}")
