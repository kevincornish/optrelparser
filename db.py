import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
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
        # Search works but have to be exact to return results eg '12345678 Morphine Sulfate' returns but 'Morphine' or '12345678' doesnt
        s = f"SELECT * FROM vials WHERE vials.batch_number LIKE '%{search}%'"
        cur.execute(s)
        rows = cur.fetchall()
        for row in rows:
        	print("Username = ", row[0], )
        	print("Product ID = ", row[1], )
        	print("Recipe = ", row[2], )
        	print("Batch Name = ", row[3], )
        	print("Batch Number = ", row[4], )
        	print("Start Date = ", row[5], )
        	print("End Date = ", row[6], )
        	print("Inspected = ", row[7], )
        	print("Accepted = ", row[8], )
        	print("Rejected = ", row[9], )
        	print("Technical Rejects = ", row[10], "\n" )
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_ampoules(search):
    """ query data from the ampoules table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        s = f"SELECT * FROM ampoules WHERE ampoules.batch_number LIKE '%{search}%'"
        cur.execute(s)
        rows = cur.fetchall()
        for row in rows:
        	print("Username = ", row[0], )
        	print("Product ID = ", row[1], )
        	print("Recipe = ", row[2], )
        	print("Batch Name = ", row[3], )
        	print("Batch Number = ", row[4], )
        	print("Start Date = ", row[5], )
        	print("End Date = ", row[6], )
        	print("Inspected = ", row[7], )
        	print("Accepted = ", row[8], )
        	print("Rejected = ", row[9], )
        	print("Technical Rejects = ", row[10], "\n" )
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_vials(data):
    """ insert new vials into the vials table """
    sql = f"""
    INSERT INTO vials(
        username, product_id, recipe, batch_name, batch_number, start_date, end_date, inspected, accepted, rejected, technical_rejects
        ) 
    VALUES(
    '{data['username']}', '{data['product_id']}', '{data['recipe']}', '{data['batch_name']}', '{data['batch_number']}', '{data['start_date']}', 
    '{data['end_date']}', '{data['inspected']}', '{data['accepted']}', '{data['rejected']}', '{data['technical_rejects']}')
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print ("importing...")
        cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_ampoules(data):
    """ insert new ampoules into the ampoules table """
    sql = f"""
    INSERT INTO ampoules(
        username, product_id, recipe, batch_name, batch_number, start_date, end_date, inspected, accepted, rejected, technical_rejects
        ) 
    VALUES(
    '{data['username']}', '{data['product_id']}', '{data['recipe']}', '{data['batch_name']}', '{data['batch_number']}', '{data['start_date']}', 
    '{data['end_date']}', '{data['inspected']}', '{data['accepted']}', '{data['rejected']}', '{data['technical_rejects']}')
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print ("importing...")
        cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
