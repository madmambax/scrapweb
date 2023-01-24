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
   -h, --help            show this help message and exit
   -u URL, --Url URL     Region URL for scrap. (default: None)
   -o OUTPUT, --Output OUTPUT 
                       CSV output file for elections results (default: None)

## Example of the program running


## Partial output