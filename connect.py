# To connect to MYSQL< we need mysql-connector-python
import mysql.connector as mydbconnection # using an alias for clarity
from mysql.connector import Error # Error function for special MYSQL errors

def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password=''
        )
        if conn.is_connected():
            print('✅connected to MYSQL database')

    except Error as e:
        print(f'❌ Errot: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')


if __name__ == "__main__":
    connect()