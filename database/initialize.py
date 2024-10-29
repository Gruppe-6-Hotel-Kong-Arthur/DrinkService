import pandas as pd
import sqlite3
import os

import pandas as pd
import sqlite3
import os

def init_db():
    # Specify the Excel file and SQLite database file path
    excel_file = "xlxs/drinks_menu_with_sales.xlsx"
    sqlite_db = os.path.join(os.getcwd(), "drinks_menu.db")

    # Delete the database file if it exists to avoid conflicts
    if os.path.exists(sqlite_db):
        os.remove(sqlite_db)

    # Read the Excel file
    data = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Connect to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Create the categories table and insert initial values
    cursor.execute("""
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT UNIQUE
        )
    """)
    
    # Insert the categories 
    cursor.execute("INSERT INTO categories (category_id, category_name) VALUES (1, 'cocktail')")
    cursor.execute("INSERT INTO categories (category_id, category_name) VALUES (2, 'coffee')")

    # Create the drinks table 
    cursor.execute("""
        CREATE TABLE drinks (
            drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
            drink_name TEXT,
            category_id INTEGER,
            price_dkk REAL,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    """)

    # Map the category names to their corresponding IDs for insertion
    category_map = {"cocktail": 1, "coffee": 2}

    # Insert data from the DataFrame into the drinks table
    for _, row in data.iterrows():
        category = row['Category'].lower()
        drink_name = row['Drink Name']
        price_dkk = row['Price (DKK)']

        # Get the corresponding category_id
        category_id = category_map.get(category)
        if category_id:
            cursor.execute("""
                INSERT INTO drinks (drink_name, category_id, price_dkk)
                VALUES (?, ?, ?)
            """, (drink_name, category_id, price_dkk))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

