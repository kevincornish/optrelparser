import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

def insert_vials_from_dict(data):
    """
    example data:
    {
        "id": 1,
        "product": 'blah',
        "recipe": "something"
    }
    :param data:
    :return:
    """
    required_columns = VIAL_COLUMNS
    if set(required_columns) != set(data.keys()):
        raise Exception("Columns are not correct")
    query = db.insert(vials).values(**data)
    connection.execute(query)
