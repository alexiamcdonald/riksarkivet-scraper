import requests
from bs4 import BeautifulSoup

URL = 'https://sok.riksarkivet.se/person?Namn=peter+tottie'
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

print("NUMBER OF RESULTS", result_count)

print(results)
