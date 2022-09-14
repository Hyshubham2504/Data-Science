# from bs4 import BeautifulSoup
# with open('index.html','r') as f:
#     contents=f.read()
#     soup=BeautifulSoup(contents,'lxml')
#     print(soup.h2)
#     print(soup.head)
#     for child in soup.recursiveChildGenerator():
#         if child.name:
#             print(child.name)

import requests
from bs4 import BeautifulSoup
url="https://www.kiit.ac.in"
response=requests.request("GET",url)
data=BeautifulSoup(response.text,'html.parser')
print(data)