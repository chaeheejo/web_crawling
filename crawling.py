from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

address = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8B%AC%EB%9F%AC+%ED%99%98%EC%9C%A8"
url = Request(address,headers={'User-Agent' : 'Mozilla/5.0'})
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

value = soup.find("span", {"class" : "spt_con up"}).find("strong")
text = value.get_text()
print('Today Exchange Rate')
print(text)