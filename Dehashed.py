from bs4 import BeautifulSoup
from colorama.initialise import reset_all
import requests, openpyxl
from colorama import Fore, Style
import os

command = "Dehashed.xlsx"
LINK = 'https://www.dehashed.com/data'

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Dehashed Data'
print(excel.sheetnames)
sheet.append(['WEBSITE', 'DESCRIPTION', 'DATE', 'COUNT', 'DATA'])

try:
    source = requests.get(LINK)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')

    data = soup.find('tbody').find_all('tr')
    
    for da in data:
       website = da.find('td', class_="align-middle").text
       description = da.find('abbr', class_="bs-tooltip").text
       date = da.find('span', class_="text-nowrap").text
       count = da.find('span', class_="text-nowrap").find_next('span').get_text(strip=True)
       data = da.find('abbr', class_="bs-tooltip").find_next('abbr').get_text(strip=True)


       ##print(website + '\t\t' + description + '\t' + date)
       sheet.append([website, description, date, count, data])
        

except Exception as ex:
    print(ex)

excel.save('Dehashed.xlsx')
print(Fore.GREEN + 'FILE SALVATO!')
print(Style.RESET_ALL)
os.startfile(command)