import re
import subprocess
import uuid
import time
import requests
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool

u = UserAgent()
headers = {'User-Agent': u.random}
url = "https://www.163.com"
s = requests.Session()

res = s.get(url, headers=headers)
print(res.status_code)

