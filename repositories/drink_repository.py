from database.connection import create_connection
import sqlite3


# Retrieve all drinks from the database
def db_get_drinks():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute( """
        SELECT d.drink_id, d.drink_name, c.category_name AS category, d.price_dkk
        FROM drinks d
        JOIN categories c ON d.category_id = c.category_id
    """
    )
    
    drinks_list = [dict(row) for row in cursor.fetchall()]
    
    connection.close()
    return drinks_list

# Retrieve a drink by its ID from the database
def db_get_drink_by_id(drink_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute( """
        SELECT d.drink_id, d.drink_name, c.category_name AS category, d.price_dkk
        FROM drinks d
        JOIN categories c ON d.category_id = c.category_id
        WHERE d.drink_id = ?
    """, (drink_id,)
    )

    drink = cursor.fetchone()
    connection.close()
    return dict(drink) if drink else None



