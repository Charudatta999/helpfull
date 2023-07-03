import csv
import sqlite3
import sys


def compare_databases(db1_file, db2_file, output_file):
    # Connect to the first database
    conn1 = sqlite3.connect(db1_file)
    cursor1 = conn1.cursor()

    # Connect to the second database
    conn2 = sqlite3.connect(db2_file)
    cursor2 = conn2.cursor()

    # Get the list of tables in the first database
    cursor1.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor1.fetchall()]

    # Open the output CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Table', db1_file, db2_file])

        # Compare the tables and their data
        for table in tables:
            # Compare the table data
            cursor1.execute(f"SELECT * FROM {table};")
            data1 = cursor1.fetchall()
            cursor2.execute(f"SELECT * FROM {table};")
            data2 = cursor2.fetchall()

            if data1 != data2:
                # Write the differences to the CSV file
                for i in range(len(data1)):
                    if data1[i] != data2[i]:
                        writer.writerow([table, data1[i], data2[i]])

    # Close the database connections
    conn1.close()
    conn2.close()


# Usage example
if len(sys.argv) != 4:
    print("Usage: python compare_databases.py <database1> <database2> <output_file>")
else:
    db1_file = sys.argv[1]
    db2_file = sys.argv[2]
    output_file = sys.argv[3]
    compare_databases(db1_file, db2_file, output_file)
