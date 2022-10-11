import csv
import sys

import requests
from bs4 import BeautifulSoup


def download(URL):
    down = requests.get(URL)
    soup = BeautifulSoup(down.text, 'html.parser')
    return soup


def links(soup):
    list_links = []
    for link in soup.select("td.cislo a"):
        list_links.append('https://volby.cz/pls/ps2017nss/' + link['href'])
    return list_links


def nums(soup):
    nums = []
    for cislo_ok in soup.select('td.cislo a'):
        nums.append(cislo_ok.get_text())
    return nums


def political(soup, modifier):
    political = []
    for strana in soup.select(f'div.t2_470 table tr td:nth-of-type({modifier})'):
        political.append(strana.get_text())
    return political


def names(soup):
    name = []
    all_names = soup.find_all('td', 'cislo')
    for i in all_names:
        name.append(i.find_next_sibling('td').get_text())
    return name


def scraping(list_links):
    print(f'''Stahuji data z {URL}...
Prosím čekejte, proces může chvíli trvat...''')
    header = ['code', 'location', 'registred', 'envelopes', 'valid']
    results = []
    index = 0
    for town in list_links:
        data = []
        soup = download(URL)
        name, number = names(soup), nums(soup)
        data.append(number[index])
        data.append(name[index])
        index += 1
        soup_town = download(town)
        for i, j in enumerate(soup_town.find_all('td', class_='cislo')):
            if i in (3, 4, 7):
                data.append(str(j.get_text()).replace(u'\xa0', u' '))
            elif i == 8:
                break
        for num_votes in political(soup_town, 3):
            data.append(num_votes)
        results.append(data)
    soup_town = download(town)
    for group in political(soup_town, 2):
        header.append(group)
    output = (results, header)
    return output


def file_write(results):
    with open(f'{file_name}.csv', mode='w', newline='', encoding='utf-8') as file:
        writing = csv.writer(file)
        writing.writerow(results[1])
        writing.writerows(results[0])


if __name__ == '__main__':
    URL = sys.argv[1]
    file_name = sys.argv[2]
    vysledky = scraping(links(download(URL)))
    print(f'Ukládám data do souboru {sys.argv[2]}.csv ...')
    file_write(vysledky)
    print(f'Proces dokončen. Data uložena do souboru {sys.argv[2]}.csv.')
