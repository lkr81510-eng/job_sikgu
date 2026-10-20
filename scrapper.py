import requests
from bs4 import Beautifulsoup

keyword = "파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
r = requests.get(url)
# print(r.text)
soup = Beautifulsoup(r.txt, "html.parser")
#print(soup.prettify())

soup.find_all("li", class_="c-col")
#print(lis)
#print(len(lis))

for li in lis:
    li.find("a",class_="cpname").text
    print(conpany)
    