from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import BigInteger, DATETIME
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:coder@localhost:3306/test', encoding='utf-8', echo=True)

Base = declarative_base()

class Web(Base):
  __tablename__ = 'web'

  id = Column(Integer, primary_key = True, autoincrement = True)
  uri = Column(String(200))

  def __repr__(self):
    return "<Web(id='%d', uri='%s')>" % (self.id, self.uri)

class PerformanceTiming(Base):
  __tablename__ = 'performance_timing'

  id = Column(Integer, primary_key=True, autoincrement=True)
  web_id = Column(Integer)
  connect_start = Column(BigInteger)
  navigation_start = Column(BigInteger)
  secure_connection_start = Column(BigInteger)
  fetch_start = Column(BigInteger)
  dom_content_loaded_event_start = Column(BigInteger)
  response_start = Column(BigInteger)
  dom_interactive = Column(BigInteger)
  domain_lookup_end = Column(BigInteger)
  redirect_start = Column(BigInteger)
  request_start = Column(BigInteger)
  unload_event_end = Column(BigInteger)
  unload_event_start = Column(BigInteger)
  dom_complete = Column(BigInteger)
  domain_lookup_start = Column(BigInteger)
  load_event_start = Column(BigInteger)
  dom_content_loaded_event_end = Column(BigInteger)
  redirect_end = Column(BigInteger)
  connect_end = Column(BigInteger)
  response_end = Column(BigInteger)
  dom_loading = Column(BigInteger)
  load_event_end = Column(BigInteger)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

def get_web_list():
  session = Session()
  return session.query(Web)

def add_performance_timing(performance_timing):
  session = Session()
  session.add(performance_timing)
  session.commit()
  return performance_timing

# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# Session = sessionmaker(bind = engine)
# session = Session()
# session.add(ed_user)
# session.commit()

if __name__ == '__main__':
  print(get_web_list().all())