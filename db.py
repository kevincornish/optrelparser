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

def get_vials(search):
    """ query data from the vials table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM vials WHERE vials.batch like 'Morphine Sulfate'")
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchall()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_vials(vial_list):
	""" insert new vials into the vials table """
	sql = "INSERT INTO vials(id,username,product_id,recipe,batch,start_date,end_date,inspected,accepted,rejected,technical_rejects) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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
