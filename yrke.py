import requests
from bs4 import BeautifulSoup

class Yrke:
    def get_yrke_page(url):
        yrke_page = requests.get(url)
        soup = BeautifulSoup(yrke_page.content, 'html.parser')

        results = str(soup.find_all('div', class_='post_faltdata'))

        # removes all unnecessary crap at bottom
        if results.find('bild'):
            split_string = results.split('<div class="span8 post_faltdata post_faltButton post">', 1)
            results = split_string[0]
        if results.find('<a href=" https://www.kb.se/besok-och-anvand/kopiera-och-fotografera/bestall-kopior.html" target="_new">'):
            split_string = results.split('<a href=" https://www.kb.se/besok-och-anvand/kopiera-och-fotografera/bestall-kopior.html" target="_new">', 1)
            results = split_string[0]

        results = results.replace('[', '')
        results = results.replace('</b>', '') # remove </b> html tag
        results = results.replace('</i>', '')
        results = results.replace('<i>', '')
        results = results.replace('<b class="visible-phone">', '') # remove <visible-phone> html tag
        results = results.replace('<div class="span7 post_faltdata">', '')
        results = results.replace('</div>', '')
        results = results.replace('<div class="span7 post_faltdata">', '')
        results = results.replace('<br/>', '')
        results = results.replace(',', '')
        results = results.replace('<u>', '****** \n')
        results = results.replace('</u>', '')

        return results
