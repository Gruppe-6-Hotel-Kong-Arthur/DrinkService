import pandas as pd
import sqlite3
import os

# Specify the Excel file and the desired SQLite database file name
excel_file = "xlxs/drinks_menu_with_sales.xlsx"
sqlite_db = "drinks_menu.db"

# Read the Excel file
data = pd.read_excel(excel_file, sheet_name=None)

# Connect to the SQLite database (or create it if it doesn’t exist)
conn = sqlite3.connect(sqlite_db)

# Loop through each sheet and store it as a table in SQLite
for sheet_name, df in data.items():
    df.to_sql(sheet_name, conn, if_exists="replace", index=False)

# Close the database connection
conn.close()

print("Data has been successfully imported into the SQLite database.")
