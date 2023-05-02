from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

star_table = soup.find_all('table', {"class":"wikitable sortable"})

dwarf_list= []

tr_tag = star_table[2].find_all('tr')

for tr in tr_tag:
    td_tag = tr.find_all('td')
    temp_list = []
    for td in td_tag:
        temp_list.append(td.text)
    dwarf_list.append(temp_list)

Star_names = []
Distance = []
Mass = []
Radius = []

print(dwarf_list)

for i in range(1,len(dwarf_list)):
    Star_names.append(dwarf_list[i][0])
    Distance.append(dwarf_list[i][5])
    Mass.append(dwarf_list[i][7])
    Radius.append(dwarf_list[i][8])

headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")                           
