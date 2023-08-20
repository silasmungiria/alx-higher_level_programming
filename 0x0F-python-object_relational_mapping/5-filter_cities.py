#!/usr/bin/python3
"""
Lists the names of cities in a specified state from,
the 'hbtn_0e_0_usa' database.
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
    state_name = sys.argv[4]
    query = """
    SELECT cities.name
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    """
    cur.execute(query, (state_name,))

    # Fetch and process results
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Close the cursor and database connection
    cur.close()
    db.close()
