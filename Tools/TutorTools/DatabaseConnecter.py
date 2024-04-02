import sqlite3
from langchain.tools import tool


class ConnectDatabase():

    @tool
    def results_available():
        """
        Returns available results from the database.
        """

        conn = sqlite3.connect('results.db')
        res = conn.execute("SELECT Topic, score FROM results").fetchall()

        return res
    

# Database file path
db_path = 'results.db'

# Connect to the SQLite database. This will create the database file if it does not exist.
conn = sqlite3.connect(db_path)

# Create a cursor object using the connection
cursor = conn.cursor()

# SQL statement to create a table
create_table_sql = """
CREATE TABLE IF NOT EXISTS results (
    Topic TEXT NOT NULL,
    score INTEGER NOT NULL
);
"""

# Execute the SQL statement to create the table
cursor.execute(create_table_sql)

# Insert sample data into the ingredients table
# This is optional and can be customized or removed
insert_data_sql = """
INSERT INTO results (Topic, score)
VALUES 
('Math', 10),
('Science', 8),
('English', 7),
('Chemistry', 10),
('Physics', 6);
"""

# Execute the SQL statement to insert data
cursor.execute(insert_data_sql)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

print("Database and table created successfully with sample data.")