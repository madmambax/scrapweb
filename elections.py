""""
elections.py: Third project to Engeto Online Python Academy
author: Martin Mannsbarth
email: mann.m@seznam.cz
discord: Martin M.#4226
"""

# import modules and packages for projdet
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
# url = args.Url
uri = args.Url
out_f = args.Output

# print debug
print(uri)
print(out_f)