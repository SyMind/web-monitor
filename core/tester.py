from selenium import webdriver

class Tester(object):
  def __init__(self):
    self.driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

  def test(self, web):
    self.driver.get(r'https://www.baidu.com')
    return self.driver.execute_script('return performance.timing')

# driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# def test(web):
#   driver.get(r'https://www.baidu.com')
#   return driver.execute_script('return performance.timing')

# def test_loop(web):
#   print('test...')
#   print(driver.get(web['uri']).response)
#   info = {
#     #DNS查询耗时
#     'domain_lookup' : driver.execute_script('return performance.timing.domainLookupEnd - performance.timing.domainLookupStart'),
#     #TCP链接耗时
#     'connect' : driver.execute_script('return performance.timing.connectEnd - performance.timing.connectStart'),
#     #request请求耗时
#     'response' : driver.execute_script('return performance.timing.responseEnd - performance.timing.responseStart'),
#     #解析dom树耗时
#     'dom' : driver.execute_script('return performance.timing.domComplete - performance.timing.domInteractive'),
#     #白屏时间
#     'response' : driver.execute_script('return performance.timing.responseStart - performance.timing.navigationStart'),
#     #dom_ready时间
#     'dom_content_loaded' : driver.execute_script('return performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart'),
#     #onload时间
#     'load' : driver.execute_script('return performance.timing.loadEventEnd - performance.timing.navigationStart')
#   }
#   driver.close()
#   return info

# if __name__ == '__main__':
#   test({'id':1, 'uri':'http://jwzx.sut.edu.cn/'})
