#!/usr/bin/python3
"""Script that displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Create the SQL query with user input
    query = "SELECT * FROM states " \
            "WHERE BINARY name LIKE '{}' ORDER BY id ASC".format(state_name)

    # Execute the query with user input
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
