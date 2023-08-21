#!/usr/bin/python3
"""
Lists all states from the 'hbtn_0e_0_usa' database based,
on a provided name pattern.
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
    name_pattern = sys.argv[4]
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(name_pattern)
    )
    cur.execute(query)

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
