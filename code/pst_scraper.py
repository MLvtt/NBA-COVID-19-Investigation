import requests, copy, json
from bs4 import BeautifulSoup

class PSTScrape:
    def __init__(self, url, start, end):
        self.url = url
        self.all_rows = []
        for x in range(start, end+1, 25):
            self.scraper_function(x)
            
    def scraper_function(self, x):
        r = requests.get(self.url+str(x))
        soup = BeautifulSoup(r.content, "html")
        div = soup.find("div", {"class": "container"})
        table = div.find("table")
        rows = table.find_all("tr")
        empty_row = {"Date": None, 
                     "Team": None, 
                     "Healed": None, 
                     "Injured": None, 
                     "Notes": None}
        for row in rows[1:]:
            new_row = copy.copy(empty_row)
            columns = row.find_all("td")
            new_row['Date'] = columns[0].text.strip()
            new_row['Team'] = columns[1].text.strip()
            new_row['Healed'] = columns[2].text.strip()[2:]
            new_row['Injured'] = columns[3].text.strip()[2:]
            new_row['Notes'] = columns[4].text.strip()
            self.all_rows.append(new_row)  
        print(f"Page {(x/25) + 1} scraped")


if __name__ == "__main__":
    url = "http://www.prosportstransactions.com/basketball/Search/SearchResults.php?Player=&Team=&BeginDate=2020-03-11&EndDate=&ILChkBx=yes&InjuriesChkBx=yes&PersonalChkBx=yes&Submit=Search&start="
    start = 0
    end = 3075
    pst = PSTScrape(url, start, end)
    with open('./data/pst_nba_injuries_2020_2021.txt', 'w') as outfile:
        json.dump(pst.all_rows, outfile)
