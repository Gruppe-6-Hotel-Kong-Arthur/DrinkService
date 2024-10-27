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

    # Read the Excel file
    data = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Create a new table with an auto-incrementing id column and columns based on the Excel data
    cursor.execute("""
        CREATE TABLE drinks (
            id INTEGER PRIMARY KEY,
            drink_name TEXT,
            category TEXT,
            price_dkk REAL,
            units_sold INTEGER
        )
    """)

    # Insert data from the DataFrame into the "drinks" table
    for _, row in data.iterrows():
        cursor.execute("""
            INSERT INTO drinks (drink_name, category, price_dkk, units_sold)
            VALUES (?, ?, ?, ?)
        """, (row['Drink Name'], row['Category'], row['Price (DKK)'], row['Units Sold']))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database has been initialized successfully.")
