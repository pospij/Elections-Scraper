# Elections-Scraper
Engeto projekt 3.


## Popis
Tento projekt slouží k extrahování a ukládaní výsledků z parlamentních voleb z roku 2017.

Odkaz [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

## Instalace knihoven
Použité knihovny jsou uložené v souboru requirements.txt.

Instalace:
> $ pip install (knihovna)   #nainstalujete knihove dle requirements.txt


## Spuštění
Spuštění souboru Scraper.py v příkazovém řádku vyžaduje dva povinné argumenty
Argumenty se zadavájí jako string
1. argument je odkaz územního celku (Odkaz pod X ve sloupci Výběr obce)
2. argument je název CSV souboru do kterého chceme data uložit (název bez přípony souboru)
>python Scraper.py 'odkaz' 'název souboru'

## Ukázka průběhu
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4206
2. argument: teplice

Spuštění:
>python Scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4206' 'teplice'

Průběh:
>Zadané URL je správné, pokračuji v procesu.\
>Stahuji data z https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4206... \
>Prosím čekejte, proces může chvíli trvat...\
>Ukládám data do souboru teplice.csv ...\
>Proces dokončen. Data uložena do souboru teplice.csv. 

Částečný výstup:
>code,location,registred,envelopes,valid, ... \
> 567451,Bílina,11 953,5 242,5 184,398,13,2,330,119,675,58,40,57,4, ... \
> 567469,Bořislav,327,195,194,26,0,0,12,7,24,2,2,4,0,1,21,0,17,48,0,0,2,0,2,0,2,21,3 \
>567477,Bystřany,1 599,926,920,89,3,0,80,25,73,13,12,11,1,4,75,1,32,340,0,6,12,1,2,2,3,131,4 \
> ...