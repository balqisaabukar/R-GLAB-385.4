# To connect to MySQL, we need mysql-connector-python
import mysql.connector as mydbconnection # using an alias for clarity
from mysql.connector import Error # Error function for special MySQL errors


def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='' # password for mysql server
        )

        if conn.is_connected():
            print('✅ Connected to MySQL database')

        # Creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()

       # Create a SQL Query we want to run
        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (21, 'Hp Windows', 1000, '2021-07-15')
        '''

    

        # Executes query in SQL engine/server
        cursor.execute(query)
        print('✅ Query Executed.')

        conn.commit()
        print('✅ Transaction Commited.')

        print(f'✅ {cursor.rowcount}: Record inserted successfully.')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 Connection Closed')



if __name__ == "__main__":
    connect()