import threading, settings
from datetime import datetime
from db import repository, entity
from core import common
from core.tester import Tester
from sqlalchemy.types import DateTime

class Monitor(threading.Thread):
  def __init__(self,web):
    self.url = web.uri
    self.web_id = web.id
    self.mysql = repository.MySql()
    threading.Thread.__init__(self,name=web.uri)

  def run(self):
    performance_timing = entity.PerformanceTiming()
    performance_timing.web_id = self.web_id
    performance_timing.test_start = datetime.now()
    
    if(not common.isaccess(self.url)):
      performance_timing.access_state = False
    else:
      performance_timing.access_state = True

      dist = Tester().test(self.url)
      performance_timing.connect_start = dist['connectStart']
      performance_timing.navigation_start = dist['navigationStart']
      performance_timing.secure_connection_start = dist['secureConnectionStart']
      performance_timing.fetch_start = dist['fetchStart']
      performance_timing.dom_content_loaded_event_start = dist['domContentLoadedEventStart']
      performance_timing.response_start = dist['responseStart']
      performance_timing.dom_interactive = dist['domInteractive']
      performance_timing.domain_lookup_end = dist['domainLookupEnd']
      performance_timing.redirect_start = dist['redirectStart']
      performance_timing.request_start = dist['requestStart']
      performance_timing.unload_event_end = dist['unloadEventEnd']
      performance_timing.unload_event_start = dist['unloadEventStart']
      performance_timing.dom_complete = dist['domComplete']
      performance_timing.domain_lookup_start = dist['domainLookupStart']
      performance_timing.load_event_start = dist['loadEventStart']
      performance_timing.dom_content_loaded_event_end = dist['domContentLoadedEventEnd']
      performance_timing.redirect_end = dist['redirectEnd']
      performance_timing.connect_end = dist['connectEnd']
      performance_timing.response_end = dist['responseEnd']
      performance_timing.dom_loading = dist['domLoading']
      performance_timing.load_event_end = dist['loadEventEnd']

    self.mysql.add_performance_timing(performance_timing)

if __name__ == '__main__':
  repository.create_all()
  mysql = repository.MySql()
  query = mysql.get_web_list()
  for web in query:
    if common.isvalid(web.uri):
      monitor = Monitor(web)
      monitor.start()
      break