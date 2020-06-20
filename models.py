from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Vials(Base):
    __tablename__ = 'vials'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    product_id = Column(String)
    recipe = Column(String)
    batch = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    inspected = Column(Integer)
    accepted = Column(Integer)
    rejected = Column(Integer)
    technical_rejects = Column(Integer)

    def __repr__(self):
        return "<Vial(username='{}', product_id='{}', recipe={}, batch={}, start_date={}, end_date={}, inspected={}, accepted={}, rejected={}, technical_rejects={})>"\
                .format(self.username, self.product_id, self.recipe, self.batch, self.start_date, self.end_date, self.inspected, self.accepted, self.rejected, self.technical_rejects)

