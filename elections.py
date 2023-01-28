""""
elections.py: Third project to Engeto Online Python Academy
author: Martin Mannsbarth
email: mann.m@seznam.cz
discord: Martin M.#4226
"""

# import modules and packages for project
import argparse
import bs4
import sys
import requests
import csv
import validators

# global variables as storages for data - voters, attendance and valid votes
people_votes = []
attendance_votes = []
valid_votes = []

# Initialize parser for parameters
parser = argparse.ArgumentParser(description="Help for scrap program run",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# create parameters for program run - two URL and CSV file
parser.add_argument("-u", "--Url", help="Region URL for scrap.")
parser.add_argument("-o", "--Output", help="CSV output file for elections results")

# Read arguments from command line by parser
args = parser.parse_args()

# save URL from argument, save url and output file name for later purpose
# url -> args.Url
uri = args.Url
out_f = args.Output

# return html content
def get_link(uri):
    take_html = requests.get(uri)
    html = bs4.BeautifulSoup(take_html.text, "html.parser")
    print("DOWNLOAD DATA FROM URL:", uri)
    return html

# check arguments order, url format and output file format
def check_argum(uri, out_f):
    if (uri is None) and (out_f is None):
        parser.error("Insert two arguments for program run:\nregion URL and output CSV file put both "
                     "between \" \",\nfor help run python elections.py -h from command prompt.")
        quit()
    elif uri is None:
        parser.error("Missing Url argument, ending...")
        quit()
    elif out_f is None:
        parser.error("Missing CSV argument ending...")
        quit()
    elif not validators.url(uri):
        parser.error("Incorrect URL format or missing quotation marks, ending....")
        quit()
    elif sys.argv[1] in ['-o', '--Output']:
        parser.error("Incorrect argument order, ending...")
        quit()
    elif not out_f.endswith(".csv"):
        parser.error("Missing file extension .csv, ending...")
        quit()
    else:
        # check = False
        # return check
        pass

# verify input
check_arg = check_argum(uri, out_f)

# save to variable for repeating usage
page_html = get_link(uri)

# get towns from election region
def get_towns():
    towns = []
    towns_find = page_html.find_all("td", "overflow_name")
    for town in towns_find:
        towns.append(town.text)
    return towns

# Returns the URL address to get the details of individual municipalities of the requested district
def get_paths():
    path_municipal = []
    path_find = page_html.find_all("td", "cislo", "href")
    for path_town in path_find:
        path_town = path_town.a["href"]
        path_municipal.append(f"https://volby.cz/pls/ps2017nss/{path_town}")
    return path_municipal

# Return ids for single municipalities
def get_ids():
    town_ids = []
    ids = page_html.find_all("td", "cislo")
    for i_d in ids:
        town_ids.append(i_d.text)
    return town_ids