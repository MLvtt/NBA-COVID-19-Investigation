import requests, re
from bs4 import BeautifulSoup
from unidecode import unidecode

def id_generator(player_name):
    player = unidecode(player_name)
    if '.' in player_name:
        player = player.replace('.', '')
    if 'ö' in player_name:
        player = player.replace('ö', 'o')
    if 'Bam Adebayo' in player:
        player = 'Bam Adebayo'
    
    player_split = player.lower().split()

    if player_split[1] == 'kleber':
        return 'klebima01'
    elif player_split[1] == 'ntilikina':
        return 'ntilila01'
    else:
        bbref_id = player_split[1][:5] + player_split[0][:2] + '01'
        # print(player_name)
        url = f'https://www.basketball-reference.com/players/{bbref_id[0]}/{bbref_id}.html'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html')
        name_check = re.search(">(.+?)<", str(soup.find("h1",   {'itemprop':"name"}))).group(1)
        if unidecode(name_check.lower()) in unidecode(player_name.lower()):
            return bbref_id
        elif unidecode(name_check.lower()) in unidecode(player.lower()):
            return bbref_id
        else:
            for i in range(2,10):
                bbref_id = bbref_id[:-1] + str(i)
                url = f'https://www.basketball-reference.com/players/{bbref_id[0]}/{bbref_id}.html'
                r = requests.get(url)
                # print(player_name, r.status_code)
                if r.status_code != 200:
                    return False, player
                else:
                    soup = BeautifulSoup(r.content, 'html')
                    name_check = re.search(">(.+?)<", str(soup.find("h1",   {'itemprop':"name"}))).group(1)
                    if name_check.lower() in player_name.lower():
                        return bbref_id
            return False, player



if __name__ == "__main__":
    players = ['Nassir Little',
            'Rajon Rondo',
            'Kenyon Martin Jr. / K.J. Martin',
            'Mamadi Diakite',
            'Ben McLemore',
            'DeMarcus Cousins',
            'Eric Gordon',
            'John Wall (Hildred)',
            "De'Anthony Melton",
            'Alex Caruso',
            'Javonte Green',
            'Chandler Hutchison',
            'Lauri Markkanen',
            'Ryan Arcidiacono',
            'Tomas Satoransky',
            'Michael Porter Jr.',
            'Sindarius Thornwell',
            'Kevin Durant',
            'Juwan Morgan',
            'Nick Richards',
            'Jabari Parker',
            'Tyler Johnson',
            'Drew Eubanks',
            'Jalen Smith',
            'Seth Curry',
            'Grant Williams',
            'Robert Williams III',
            'Tristan Thompson',
            'Taj Gibson',
            'Dorian Finney-Smith',
            'Jalen Brunson',
            'Josh Richardson',
            'Matisse Thybulle',
            'Shake Milton',
            'Tobias Harris',
            'Vincent Poirier',
            'Bradley Beal',
            'Jaylen Brown',
            'Jayson Tatum',
            'Semi Ojeleye',
            'Avery Bradley',
            'Maximilian Kleber / Maxi Kleber',
            'Edrice Adebayo / Bam Adebayo',
            'Goran Dragic',
            'Jimmy Butler',
            'K.Z. Okpala',
            'Kendrick Nunn',
            'Maurice Harkless / Moe Harkless',
            'Udonis Haslem',
            'Danuel House',
            'Terrance Ferguson',
            'Dwight Powell',
            'Eric Paschall',
            'Moritz Wagner / Moe Wagner',
            'Rui Hachimura',
            'Zion Williamson',
            'Devon Dotson',
            'Luke Kornet',
            'Carsen Edwards',
            'Mohamed Bamba / Mo Bamba',
            'Victor Oladipo',
            'Juancho Hernangomez / Juan Hernangomez',
            'Ricky Rubio',
            'Karl-Anthony Towns',
            'Jonas Valanciunas',
            'Alex Len',
            'Damian Jones',
            'Dario Saric',
            'Davis Bertans',
            'Deni Avdija',
            'Ishmael Smith / Ish Smith',
            'Troy Brown Jr.',
            'Josh Hall',
            'Trent Forrest',
            'Grant Riller',
            'Nate Darling',
            'Kawhi Leonard',
            'Paul George',
            'Grayson Allen',
            'Norvel Pelle',
            'Iman Shumpert',
            'Adam Mokoka',
            'Theo Maledon',
            'Jrue Holiday',
            'Frank Ntilikina',
            'Dennis Smith Jr.',
            'Tyler Herro',
            'Caleb Martin',
            'Cody Martin',
            'Jalen McDaniels',
            'P.J. Washington',
            'Quinndary Weatherspoon',
            'Dennis Schröder',
            'Jaylen Adams',
            'Derrick White',
            'Devin Vassell',
            'Keldon Johnson',
            'Rudy Gay',
            'Hassan Whiteside',
            'JaKarr Sampson',
            'Pascal Siakam',
            'R.J. Hampton',
            'Facundo Campazzo',
            'Markus Howard',
            'Derrick Rose',
            'Marc Gasol',
            'Fred VanVleet',
            'Malachi Flynn',
            'Ogugua Anunoby / O.G. Anunoby',
            'Patrick McCaw',
            'Cameron Johnson',
            'LaMarcus Aldridge',
            'Jordan McLaughlin',
            'Ben Simmons',
            'Joel Embiid',
            'Romeo Langford',
            'Kostas Antetokounmpo',
            'P.J. Tucker',
            'Mfiondu Kabengele',
            'Sviatoslav Mykhailiuk / Svi Mykhailiuk',
            'Jaden McDaniels',
            'Axel Toupane',
            'James Johnson',
            'James Wiseman',
            'Meyers Leonard',
            'Willie Cauley-Stein',
            'Kevon Looney',
            'Anfernee Simons',
            'Alize Johnson',
            'Josh Okogie',
            'Ignas Brazdeikis / Iggy Brazdeikis',
            'Louis Williams / Lou Williams',
            'Bobby Portis',
            'Isaiah Hartenstein',
            'Evan Fournier',
            'Nemanja Bjelica',
            'Matt Thomas',
            'Jeff Teague',
            'Otto Porter Jr.',
            'Wendell Carter Jr.',
            'Nicolo Melli',
            'Aaron Gordon',
            'Gary Clark Jr.',
            'JaVale McGee',
            'Wesley Iwundu / Wes Iwundu',
            "DeAndre' Bembry / DeAndre Bembry",
            'Paul Watson',
            'Kelly Olynyk',
            'Tony Bradley',
            'Frank Kaminsky',
            'Aleksej Pokusevski',
            'Tyrese Maxey',
            'Coby White',
            'Isaiah Thomas',
            'Armoni Brooks',
            'Daniel Theis',
            'Shaquille Harrison',
            'Alfonzo McKinnie',
            'Gabriel Deck',
            'Anthony Tolliver',
            'Zach LaVine',
            'Alec Burks',
            'Nicolas Claxton',
            'Reggie Perry',
            'Keljin Blevins',
            'Kevin Porter Jr.',
            'Damion Lee',
            "De'Aaron Fox",
            'Kent Bazemore',
            'Paul Reed',
            'Myles Powell',
            'Marcos Louzada Silva / Didi Louzada Silva',
            'Amir Coffey',
            'Jahlil Okafor',
            'D.J. Wilson',
            'Miles Bridges',
            "Jae'Sean Tate",
            'Luca Vildoza',
            'Hamidou Diallo',
            'Omer Yurtseven',
            'DaQuan Jeffries',
            'Caris LeVert']


    for player in players:
        print(id_generator(player))