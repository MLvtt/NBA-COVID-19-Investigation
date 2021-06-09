import requests, re, copy
from bs4 import BeautifulSoup


class BBRefScraper:
    def __init__(self, bbref_id):
        self.id = bbref_id
        url = f'https://www.basketball-reference.com/players/{self.id[0]}/{self.id}.html'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html')
        self.name   = re.search(">(.+?)<", str(soup.find("h1",   {'itemprop':"name"}))).group(1)
        self.height = re.search(">(.+?)<", str(soup.find("span", {'itemprop':"height"}))).group(1)
        self.weight = re.search(">(.+?)<", str(soup.find("span", {'itemprop':"weight"}))).group(1)
        self.bday = re.search(r"[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]", str(soup.find('span', {'itemprop': 'birthDate'}))).group(0)

    def game_log_scraper(self, year):
        url = f'https://www.basketball-reference.com/players/{self.id[0]}/{self.id}/gamelog/{year}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html')
        div = soup.find("div", {"class": "table_container"})
        table = div.find("table", {"class": "row_summable"})
        rows = table.find_all('tr')[1:]
        player_stats = [[td.getText() 
                         for td in rows[i].find_all('td')]
                         for i in range(len(rows))]
        column_headers = [th.getText() 
                          for th in table.find_all('tr', limit=2)[0].find_all('th')]
        column_headers[5], column_headers[7] = 'Home/Away', 'Result'
        empty_row = {x: None for x in column_headers}
        game_log = []
        for i_r, row in enumerate(player_stats):
            if row != []:
                new_row = empty_row.copy()
                for i_c, col in enumerate(column_headers):
                    if i_c == 0:
                        new_row[col] = i_r+1
                    elif row[7][0].isalpha():
                        if i_c == 8:
                            new_row[col] = row[7]
                        elif i_c > 8:
                            pass
                        else:
                            new_row[col] = row[i_c-1]
                    else:
                        new_row[col] = row[i_c-1]
            game_log.append(new_row)
        return game_log

            




if __name__ == "__main__":
    from pprint import pprint
    import pandas as pd
    kd = BBRefScraper('diallha01')
    df = pd.DataFrame(kd.game_log_scraper(2021))
    print(df[['Date','GmSc']])