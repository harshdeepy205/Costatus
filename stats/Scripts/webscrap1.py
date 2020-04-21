import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import os
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

def runstat():
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'
    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))
    stats = []
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        if stat:
            if len(stat) == 5:
                # last row
                stats.append(stat)

    table_header = ["Sr.No", "States/UT", "Confirmed", "Recovered", "Deceased"]
    covid_data = pd.DataFrame(data=stats, columns=table_header)

    covid_data["Confirmed"] = covid_data["Confirmed"].astype(int)
    covid_data["Recovered"] = covid_data["Recovered"].astype(int)
    covid_data["Deceased"] = covid_data["Deceased"].astype(int)
    stats1 = [[*range(1,len(covid_data["States/UT"].tolist())+1)],covid_data["States/UT"].tolist(),covid_data["Confirmed"].tolist(),covid_data["Recovered"].tolist(),covid_data["Deceased"].tolist()]
    s_no = [*range(1,len(covid_data["States/UT"].tolist())+1)]
    state_ut = covid_data["States/UT"].tolist()
    confirmed = covid_data["Confirmed"].tolist()
    recovered = covid_data["Recovered"].tolist()
    deceased = covid_data["Deceased"].tolist()
    #rows = {'rows': {'s_no': stats1[0],'States_UT': stats1[1],'Confirmed': stats1[2],'Recovered': stats1[3],'Deceased':stats1[4]}}
    rows = {'s_no': s_no, 'States_UT': state_ut, 'Confirmed': confirmed, 'Recovered': recovered,
                     'Deceased': deceased}
    return rows

