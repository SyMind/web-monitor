import settings
from . import entity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "mysql+pymysql://%s:%s@%s:%s/%s" % (settings.DB_CONFIG["USER"], settings.DB_CONFIG["PASSWORD"], settings.DB_CONFIG["HOST"], settings.DB_CONFIG["PORT"], settings.DB_CONFIG["DATABASE"])

class MySql(object):
  def __init__(self):
    self.engine = create_engine(url, encoding='utf-8', echo=True)
    self.Session = sessionmaker(bind = self.engine)

  def get_web_list(self):
    session = self.Session()
    return session.query(entity.Web)

  def add_performance_timing(self, performance_timing):
    session = self.Session()
    session.add(performance_timing)
    session.commit()
    return performance_timing

def create_all():
  engine = create_engine(url, encoding='utf-8', echo=True)
  entity.Base.metadata.create_all(engine)