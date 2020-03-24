import requests

url = ''
response = requests.get(url)
html = requests.get(url)
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()
soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())
