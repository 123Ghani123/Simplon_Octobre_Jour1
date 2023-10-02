import psycopg2

def get_products(price):
    connection = None
    try:
        connection = psycopg2.connect("dbname='RecipeHub' user='postgres' host='localhost' password='Vp0258_Vp0258'")
        cursor = connection.cursor()
        # SQL query to execute
        query = "SELECT * FROM %s WHERE PRIX > %s" % ("PRODUIT_FOURNISSEUR", price)
        cursor.execute(query)
        print("The number of products with price >", price, "equal", cursor.rowcount)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Erreur: %s" % error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

if __name__ == '__main__':
    get_products(30)


