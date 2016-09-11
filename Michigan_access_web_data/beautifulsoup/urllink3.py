import urllib
from bs4 import BeautifulSoup

def postionURL(url,postion):
	html = urllib.urlopen(url).read()
	soup1 = BeautifulSoup(html)
	link = soup1.find_all('a')[postion].get('href')
	return link

begin_url = "http://python-data.dr-chuck.net/known_by_Ryden.html"

next1 = postionURL(begin_url, 17)
print next1
next2 = postionURL(next1, 17)
print next2
next3 = postionURL(next2, 17)
print next3
next4 = postionURL(next3, 17)
print next4
next5 = postionURL(next4, 17)
print next5
next6 = postionURL(next5, 17)
print next6
next7 = postionURL(next6, 17)
print next7



