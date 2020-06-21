import psycopg2
from config import config


def create_tables():
    """ drops tables if already created then will create tables in the PostgreSQL database"""
    commands = (
	""" DROP TABLE IF EXISTS vials, ampoules; """,
        """
        CREATE TABLE vials (
            username VARCHAR(255) NOT NULL,
            product_id VARCHAR(255) NOT NULL,
            recipe VARCHAR(255) NOT NULL,
            batch VARCHAR(255) NOT NULL,
            start_date VARCHAR(255) NOT NULL,
            end_date VARCHAR(255) NOT NULL,
            inspected VARCHAR(255) NOT NULL,
            accepted VARCHAR(255) NOT NULL,
            rejected VARCHAR(255) NOT NULL,
            technical_rejects VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE ampoules (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            product_id INT NOT NULL,
            recipe VARCHAR(255) NOT NULL,
            batch VARCHAR(255) NOT NULL,
            start_date VARCHAR(255) NOT NULL,
            end_date VARCHAR(255) NOT NULL,
            inspected INT NOT NULL,
            accepted INT NOT NULL,
            rejected INT NOT NULL,
            technical_rejects INT NOT NULL
                )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print ("Success")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
