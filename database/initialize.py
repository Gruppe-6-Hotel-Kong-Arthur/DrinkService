import pandas as pd
import sqlite3
import os


def init_db():
    # Specify the Excel file
    excel_file = "xlxs/drinks_menu_with_sales.xlsx"

    # Specify the SQLite database file path
    sqlite_db = os.path.join(os.getcwd(), "drinks_menu.db")

    # Delete the database file if it exists to avoid conflicts
    if os.path.exists(sqlite_db):
        os.remove(sqlite_db)

    # Read the Excel file (specifying only the needed sheet if it’s "Sheet1")
    data = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)

    # Write DataFrame to a table called "drinks"
    data.to_sql("drinks", conn, if_exists="replace", index=False)

    # Close the connection
    conn.close()

    print("Data has been successfully imported into the SQLite database with the table name 'drinks'.")
