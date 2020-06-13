import sqlalchemy as db

#connect to db
engine = db.create_engine('sqlite:///reports.sqlite')
connection = engine.connect()
metadata = db.MetaData()

vials = db.Table('vials', metadata, autoload=True, autoload_with=engine)
VIAL_COLUMNS = ['id', 'product', 'recipe']
ampoules = db.Table('ampoules', metadata, autoload=True, autoload_with=engine)


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
