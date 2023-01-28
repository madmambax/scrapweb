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

# Return list of candidate parties
def get_listofparties():
    parties_collection = []
    town_p = get_paths()
    html = requests.get(town_p[0])
    html_municipal = bs4.BeautifulSoup(html.text, "html.parser")
    parties = html_municipal.find_all("td", "overflow_name")
    for part in parties:
        parties_collection.append(part.text)
    return parties_collection

# summary for voters, attendance and valid vote
def get_summary_voters():
    paths = get_paths()
    for path in paths:
        html_path = requests.get(path)
        html_municipal = bs4.BeautifulSoup(html_path.text, "html.parser")
        votes = html_municipal.find_all("td", headers="sa2")
        for vote in votes:
            vote = vote.text
            people_votes.append(vote.replace('\xa0', ' '))

        attendance = html_municipal.find_all("td", headers="sa3")
        for attend in attendance:
            attend = attend.text
            attendance_votes.append(attend.replace('\xa0', ' '))

        valid_v = html_municipal.find_all("td", headers="sa6")
        for valid in valid_v:
            valid = valid.text
            valid_votes.append(valid.replace('\xa0', ' '))

# take html output from paths
def get_html_path(link):
    get_html_link = requests.get(link)
    html_link = bs4.BeautifulSoup(get_html_link.text, "html.parser")
    print("Download links from URL:", link)
    return html_link

# Take results for parties
def get_parties_result():
    path_p = get_paths()
    votes_party = []
    for path in path_p:
        html = get_html_path(path)
        vote_find = html.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        temp = []
        for vote in vote_find:
            temp.append(vote.text + ' %')
        votes_party.append(temp)
    return votes_party

# Create row output for csv file
def create_rows_output():
    rows_out = []
    get_summary_voters()
    towns = get_towns()
    ids = get_ids()
    votes = get_parties_result()
    zipped = zip(ids, towns, people_votes, attendance_votes, valid_votes)
    join_zipped = []
    for idn, town, pvs, att, vvs in zipped:
        join_zipped.append([idn, town, pvs, att, vvs])
    zip_joined_votes = zip(join_zipped, votes)
    for jz, vs in zip_joined_votes:
        rows_out.append(jz + vs)
    return rows_out

# create csv file, driving by main function, check if links is valid for election web
def elections(uri, out_f):
    try:
        headers = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        bodies = create_rows_output()
        parties = get_listofparties()
        print("SAVING DATA TO FILE: ", out_f)
        for party in parties:
            headers.append(party)
        with open(out_f, 'w', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(headers)
            f_writer.writerows(bodies)
        print("ENDING...:", uri)
    except IndexError:
        print("There is some problem, probably invalid link, ending...")
        quit()

# debug purpose
# part_out = get_parties__result()
# print(part_out)

# elections main run for scrap
if __name__ == '__main__':
    link_path = uri
    out_file = out_f
    elections(link_path, out_file)