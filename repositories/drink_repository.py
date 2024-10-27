from database.connection import create_connection

# Retrieve all drinks from the database
def db_get_drinks():
    connection = create_connection()
    
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM drinks')
    
    drinks = cursor.fetchall()
    
    connection.close()
    
    return drinks