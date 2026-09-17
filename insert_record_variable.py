# To connect to MySQL, we need mysql-connector-python
import mysql.connector as mydbconnection # using an alias for clarity
from mysql.connector import Error # Error function for special MySQL errors


def insert_record(id, name, price, date):
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='' # password for mysql server
        )

        if conn.is_connected():
            print('✅ Connected to MySQL database.')

        # Creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()

        record = (id, name, price, date) # Took function parameters and made a tuple to be inserted

        # Create a SQL Query we want to run, used parameterized values
        query = '''
            INSERT INTO laptop (Id, Name, Price, Purchase_date)
            VALUES (%s, %s, %s, %s)
        '''

        # Executes query in SQL engine/server
        cursor.execute(query, record)
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






insert_record(1, 'Mac Book Pro', 3000, '2026-09-17')
insert_record(12, 'Lenovo Think Pad', 1400, '2026-09-16')
insert_record(9, 'Alienware', 5000, '2026-08-17')