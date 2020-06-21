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

def get_vials(search):
    """ query data from the vials table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
	#Search works but have to be exact to return results eg '12345678 Morphine Sulfate' returns but 'Morphine' or '12345678' doesnt
        s = "SELECT * FROM vials WHERE vials.batch LIKE (%s)"
        cur.execute(s, [search])
        rows = cur.fetchall()
#        for row in rows:
#        	print (row)
# not sure if i need to loop them, in php i would but i feel like fetch all is already return them all nicely?
        print (rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_ampoules(search):
    """ query data from the vials table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        s = "SELECT * FROM ampoules WHERE ampoules.batch LIKE (%s)"
        cur.execute(s, [search])
        rows = cur.fetchall()
        print (rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_vials(vial_list):
	""" insert new vials into the vials table """
	sql = "INSERT INTO vials(username,product_id,recipe,batch,start_date,end_date,inspected,accepted,rejected,technical_rejects) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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


def insert_ampoules(ampoules_list):
	""" insert new ampoules into the ampoules table """
	sql = "INSERT INTO ampoules(username,product_id,recipe,batch,start_date,end_date,inspected,accepted,rejected,technical_rejects) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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
