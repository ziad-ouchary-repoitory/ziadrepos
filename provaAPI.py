import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv

url = "https://socialblade.com/youtube/top/50"
request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'})
page = urllib2.urlopen(request)
##soup = BeautifulSoup(page.content, 'html.parser')
print(page)


""" rows = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)[4:]

file = open('ciao.xlsx', 'w')

writer = csv.writer(file)

writer.writerow('Username')

for row in rows:
    ##username = row.find('a').text.strip()
    username = row.find('div', attrs={'style': 'float: left; width: 350px; line-height: 25px;'}).a.text.strip()
    ##numbers = row.find_all('span', attrs={'style': 'color#555;'})
    ##uploads = numbers[0].text.strip()
    ##views = numbers[2].text.strip()

    print(username)
    writer.writerow(username.encode('utf-8'))

file.close() """