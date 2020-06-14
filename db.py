import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
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

def get_vials(search):
    """ query data from the vials table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
	#'search' needs to be the string input from search.py
        cur.execute("SELECT id, batch, product FROM vials WHERE product LIKE search")
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_vials(vial_list):
	""" insert new vials into the vials table """
	sql = "INSERT INTO vials(batch) VALUES(%s)"
	conn = None
	try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.executemany(sql,vial_list)
                conn.commit()
                cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
