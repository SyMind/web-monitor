from urllib import request
import sys
import re

URL_REGEX = r'^(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]$'

def isvalid(url):
  tf = re.match(URL_REGEX, url)
  if tf:
    return True
  else:
    return False

def isaccess(url):
  try:
    response = request.urlopen(url)
    code = response.getcode()
  except:
    return False
  if code == 200:
    return True
  else:
    return False

if __name__ == '__main__':
  print(isvalid(r'httpss://google'))
