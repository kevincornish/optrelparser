import sqlalchemy as db

# connect to db
engine = db.create_engine('sqlite:///reports.sqlite')
connection = engine.connect()
metadata = db.MetaData()
# load the tables
vials = db.Table('vials', metadata, autoload=True, autoload_with=engine)
ampoules = db.Table('ampoules', metadata, autoload=True, autoload_with=engine)

search = input("Product search:")
v = vials.select().where(vials.c.product == search)
result = connection.execute(v)

for row in result:
    print("id:", row[vials.c.id], "; product:", row[vials.c.product])
