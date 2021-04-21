from bs4 import BeautifulSoup

file = open("index.html", "r", encoding='UTF8')
lines = file.read(-1)
#print(lines)
soup = BeautifulSoup(lines, features="html.parser")
print(soup.find_all("a"))

file.close()
