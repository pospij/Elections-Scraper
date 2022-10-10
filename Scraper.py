import csv
import sys

import requests
from bs4 import BeautifulSoup

def stazeni(url):
    stazeni = requests.get(url)
    soup = BeautifulSoup(stazeni.text, 'html.parser')
    return soup


def mesta(soup):
    seznam_mest = []
    for l in soup.select('td.cislo a'):
        seznam_mest.append("https://volby.cz/pls/ps2017nss/"+l["href"])
    return seznam_mest

def cisla_okrsku(soup):
    cisla = []
    for cislo_okrsku in soup.select('td.cislo a'):
        cisla.append(cislo_okrsku.get_text())
        return cisla

def strany(soup, modifier):
    strany = []
    for strana in soup.select(f"div.t2_470 table tr td:nth-of-type({modifier})"):
        strany.append(strana.get_text())
    return strany

def nazev(soup):
    nazev = []
    celek = soup.find_all('td', 'cislo')
    for nazvy in celek:
        nazev.append(nazvy.find_next_sibling('td').get_text())
    return nazev

def scrapping(seznam_mest):

    header = ["code", "location", "registred", "envelopes", "valid"]
    vysledky = []
    index = 0
    for obec in seznam_mest:
        data = []
        soup = stazeni(web)
        nazev, cislo = nazev(soup), cisla_okrsku(soup)
        data.append(nazev[index])
        data.append(cislo[index])
        index += 1
        obec_soup = stazeni(obec)
        for i, j in enumerate(obec_soup.find_all("td", class_="cislo")):
            if i in (3, 4, 7):
                data.append(str(j.get_text()).replace(u'\xa0', u' '))
            elif i == 8:
                break
        for pocty_hlasu in strany(obec_soup, 3):
            data.append(pocty_hlasu)
        vysledky.append(data)
    obec_soup = stazeni(obec)
    for strana in strany(obec_soup, 2):
        header.append(strana)
    vystup = (header, vysledky)
    return vystup

def csv_zapis(vystup):
    with open(f'{nazev_souboru}.csv', mode='w',newline='', encoding='utf-8') as soubor:
        zapsani = csv.writer(soubor)
        zapsani.writerow(vystup[0])
        zapsani.writerow(vystup[1])

if __name__ == '__main__':
    web = sys.argv[1]
    nazev_souboru = sys.argv[2]
    vystup = scrapping(mesta(stazeni(web)))
