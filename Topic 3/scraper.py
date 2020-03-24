import requests
from bs4 import BeautifulSoup

url = 'https://www.dmacc.edu/Pages/welcome.aspx'
response = requests.get(url)
html = requests.get(url)
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()
soup = BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())
