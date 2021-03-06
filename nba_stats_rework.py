import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from sklearn.utils import check_matplotlib_support

class nbastats:

    def __init__ (self,year):
        self.year = year

    def team_per_game(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_per_game-team'})
        table = div.find('table',{'id':'per_game-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)
        header[4:25] = [i + " Per Game" for i in header[4:25]]

        df_template = []
        
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[24*i:(24*i)+24]))
    
        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
    
        return df

    def opp_per_game(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_per_game-opponent'})
        table = div.find('table',{'id':'per_game-opponent'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header[4:25] = ["Opp " + i + " Per Game" for i in header[4:25]]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[24*i:(24*i)+24]))

        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df



    def team_per_100(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_per_poss-team'})
        table = div.find('table',{'id':'per_poss-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header[4:25] = [i + " Per 100" for i in header[4:25]]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        for i in range(0,len(table.find_all('tr'))-1):
            df_template.append(list(tables[24*i:(24*i)+24]))


        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []
        
        for i in header[1:]:
            df[i] = df[i].astype(float)
            df[i] = df[i].rank(ascending=False)

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df
    

    def opp_per_100(self):
        #Best defensive team each season (by DRtg), required table is Per 100 Poss Stats, Opponent Tab
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_per_poss-opponent'})
        table = div.find('table',{'id':'per_poss-opponent'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header[4:25] = ["Opp " + i + " Per 100" for i in header[4:25]]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        for i in range(0,len(table.find_all('tr'))-1):
            df_template.append(list(tables[24*i:(24*i)+24]))
        
        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []

        for i in header[1:]:
            df[i] = df[i].astype(float)
            df[i] = df[i].rank(ascending=False)

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        
        return df

    def team_advanced(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_advanced-team'})
        table = div.find('table',{'id':'advanced-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header = [i for i in header if i not in ('','Rk','Offense Four Factors','Defense Four Factors','\xa0')]
        header[16] = "Team " + header[16]
        header[17] = "Team " + header[17]
        header[19] = "Team " + header[19]
        header[20] = "Opp " + header[20]
        header[21] = "Opp " + header[21]
        header[23] = "Opp " + header[23]

        for tr in table.find_all('tbody'):
            for td in tr.find_all('td',{'data-stat':'DUMMY'}):
                #row = td(text=True,dummy=False)
                #tables.append(''.join(row) if row else 'blank')
                #tables = [val for val in tables if val not in ('.','')]
                td.decompose()

            for td in tr.find_all('td'):
                row = td(text=True)
                if row:
                    tables.append(''.join(row))
                else:
                    tables.append('N/A')
                tables = [val for val in tables if val not in ('.','')]
        
        df_template = []
        
        for i in range(0,len(table.find_all('tr'))-3):
            df_template.append(list(tables[27*i:(27*i)+27]))
    
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []

        for i in header[1:24]:
            df[i] = df[i].astype(float)
            df[i] = df[i].rank(ascending=False)
        
        df = df.drop(columns=['Arena','Attend.','Attend./G'])

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
    
        return df
        

    def team_shooting(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_shooting-team'})
        table = div.find('table',{'id':'shooting-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header = [i for i in header if i not in ('','\xa0','% of FGA by Distance','FG% by Distance','% of FG Ast\'d','Dunks','Layups','Corner','Heaves','Rk')]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td',{'data-stat':'DUMMY'}):
                #row = td(text=True,dummy=False)
                #tables.append(''.join(row) if row else 'blank')
                #tables = [val for val in tables if val not in ('.','')]
                td.decompose()

            for td in tr.find_all('td'):
                row = td(text=True)
                if row:
                    tables.append(''.join(row))
                else:
                    tables.append('Not reported')
                tables = [val for val in tables if val not in ('.','')]

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[27*i:(27*i)+27]))
    
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        
        return df



    def opp_shooting(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        champ = str(int(self.year)) + " " + champ
        div = soup.find('div',{'id':'div_shooting-opponent'})
        table = div.find('table',{'id':'shooting-opponent'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header = [i for i in header if i not in ('','\xa0','% of FGA by Distance','FG% by Distance','% of FG Ast\'d','Dunks','Layups','Corner','Heaves','Rk')]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td',{'data-stat':'DUMMY'}):
                #row = td(text=True,dummy=False)
                #tables.append(''.join(row) if row else 'blank')
                #tables = [val for val in tables if val not in ('.','')]
                td.decompose()

            for td in tr.find_all('td'):
                row = td(text=True)
                if row:
                    tables.append(''.join(row))
                else:
                    tables.append('Not reported')
                tables = [val for val in tables if val not in ('.','')]

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[27*i:(27*i)+27]))
    
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        df['Team'] = df['Team'].map(lambda y:str(int(self.year)) + " " + y)
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df
