#!/usr/bin/python3
"""
Lists all cities and their corresponding states,
from the 'hbtn_0e_0_usa' database.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a database connection
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor
    cur = db.cursor()

    # Execute the query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    """
    cur.execute(query)

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
