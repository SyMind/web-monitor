import threading
import repository,common,performance
from settings import DB_CONFIG

class Monitor(threading.Thread):
  def __init__(self,web):
    self.url = web.uri
    self.web_id = web.id
    threading.Thread.__init__(self,name=web.uri)

  def run(self):
    dist = performance.test(self.url)
    print(dist)
    performance_timing = repository.PerformanceTiming()
    performance_timing.web_id = self.web_id
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
    repository.add_performance_timing(performance_timing)

if __name__ == '__main__':
  # query = repository.get_web_list()
  # for web in query:
  #   if common.isvalid(web.uri) and common.isaccess(web.uri):
  #     monitor = Monitor(web)
  #     monitor.setDaemon(True)
  #     monitor.start()
  print(DB_CONFIG)
