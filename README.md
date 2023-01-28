# Scrap web

# Elections scraper
Project 3 to Engeto Python Academy

## Project goal
Get election data, extract it from web volby.cz, election year 2017
for the selected district [Link] (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)
(column *Výběr obce*) and save result to CSV file.

## Modules and packages required for the program to run
Modules and packages are stored in the file requirements.txt

## Program run
File elections.py is need run from command prompt and requires two arguments.

## How to run

 > python elections.py -u "URL for election district" -o "filename.csv"
 
Output is .csv file with election result.

## Example

Result for district "Kolín"

> 1. argument >>> https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104
> 2. argument >>> Kolin_volby2017.csv


RUN:

  > python elections.py -u "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104" -o "Kolin_volby2017.csv"

Help for run:

> python elections.py -h

Ouput is simple help for set program parameters.

>usage: elections.py [-h] [-u URL] [-o OUTPUT]

Help for scrap program run

options:

-h, --help  show this help message and exit

-u URL, --Url URL  Region URL for scrap. (default: None)

-o OUTPUT, --Output OUTPUT CSV output file
                    for elections results (default: None)

## Example of the program running from terminal

> DOWNLOAD DATA FROM URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104
> 
> Download links from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=533173&xvyber=2104
> 
> Download links from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=533181&xvyber=2104
> 
> .......................
> .......................
> ,,,,,,,,,,,,,,,,,,,,,,,
> 
> Download links from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=538035&xvyber=2104
> 
> Download links from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=533947&xvyber=2104
> 
> SAVING DATA TO FILE:  Kolin_volby2017.csv
> 
> ENDING...: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104

## Partial output

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,
Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,
Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,
"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,
Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,
SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,
Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
533173,Barchovice,185,132,132,"6,06 %","0,00 %","0,00 %","8,33 %","0,00 %","10,60 %","8,33 %","0,00 %","0,00 %",
"1,51 %","0,75 %","0,00 %","20,45 %","0,00 %","0,00 %","6,06 %","28,03 %","0,00 %","1,51 %","1,51 %","0,00 %",
"0,75 %","0,00 %","0,75 %","5,30 %","0,00 %"
533181,Bečváry,822,492,491,"8,35 %","0,00 %","0,20 %","6,51 %","0,00 %","19,14 %","9,77 %","0,61 %","0,61 %","0,61 %",
"0,00 %","0,00 %","6,92 %","0,00 %","0,00 %","2,03 %","34,01 %","0,00 %","0,61 %","1,22 %","0,00 %","0,40 %","0,00 %",
"0,40 %","8,35 %","0,20 %"
533190,Bělušice,229,123,123,"7,31 %","0,00 %","0,00 %","9,75 %","0,00 %","13,00 %","14,63 %","0,00 %","0,81 %","0,00 %",
"0,00 %","0,00 %","6,50 %","0,00 %","0,00 %","0,00 %","37,39 %","0,00 %","0,00 %","0,81 %","0,00 %","0,00 %","0,00 %",
"0,00 %","9,75 %","0,00 %"
