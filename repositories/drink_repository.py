from database.connection import create_connection


# Retrieve all drinks from the database
def db_get_drinks():
    connection = create_connection()
    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM drinks')
    
    drinks_list = [dict(row) for row in cursor.fetchall()]
    
    connection.close()
    
    return drinks_list

# Retrieve a drink by its ID from the database
def db_get_drink_by_id(drink_id):
    connection = create_connection()
    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM drinks WHERE id = ?', (drink_id,))
    
    drink = cursor.fetchone()
    
    connection.close()
    
    return dict(drink) if drink else None


# Update the units sold for a drink in the database by an amount
def db_update_units_sold(drink_id, amount):
    connection = create_connection()
    
    cursor = connection.cursor()
    cursor.execute('UPDATE drinks SET units_sold = units_sold + ? WHERE id = ?', (amount, drink_id))
    
    connection.commit()
    connection.close()

