import requests
from bs4 import BeautifulSoup
from yrke import Yrke
import sys


URL = 'https://sok.riksarkivet.se/person?Namn=' + sys.argv[1]
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result_count = len(soup.find_all('div', class_='hit_middle'))

results = str(soup.find_all('div', class_='hit_middle'))

results = results[1:] # remove first [
results = results[:-1] # remove last ]
results = results.replace('<div class="hit_middle">', '======================') # replace <div> with result separator
results = results.replace('</div>', '') # remove <div> html tag
results = results.replace('<b>', '') # remove <b> html tag
results = results.replace('</b>', '') # remove </b> html tag
results = results.replace('<br/>', '') # remove <br/> html tag

revised_soup = BeautifulSoup(results, 'html.parser')

# finds name and href within a tags and puts them into lists
names = []
hrefs = []
for name in revised_soup.find_all('a'):
    names.append(name.text)
    hrefs.append('https://sok.riksarkivet.se' + name.get('href'))

# finds a tags and puts into a list
a_tags = list(revised_soup.find_all('a'))

# replaces all a tags with link with actual name of person in the results
index = 0
for tag in a_tags:
    url_data = Yrke.get_yrke_page(hrefs[index])
    add_in = str(names[index]) + '\n' + url_data
    results = results.replace(str(a_tags[index]), add_in, 1)
    index += 1

print("NUMBER OF RESULTS", result_count)

print(results)
