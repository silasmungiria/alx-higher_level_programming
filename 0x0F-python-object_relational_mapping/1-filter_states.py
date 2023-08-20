#!/usr/bin/python3
"""
Lists all states from the 'hbtn_0e_0_usa' database.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
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
    SELECT *
    FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY states.id
    """
    cur.execute(query)

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
