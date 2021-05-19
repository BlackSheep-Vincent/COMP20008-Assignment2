import pandas as pd
import re
import matplotlib.pyplot as plt

ch = pd.read_csv("crime.csv", encoding='ISO-8859-1')
ch.rename(columns={"ï»¿Year":"Year"}, inplace=True)

Top10city = ['Ballarat','Bendigo','Geelong','Horsham','Latrobe','Mildura','Shepparton','Wangaratta','Warrnambool','Wodonga']

ch2015 = ch.drop(ch[ch["Year"]!=2015].index).copy()
ch2019 = ch.drop(ch[ch["Year"]!=2019].index).copy()

new_area_2015 = []
new_area_2019 = []
for area in ch2015['Local Government Area']:
    if re.search(r'[\w|\s]+Ballarat',area):
        new_area_2015.append('Ballarat')
    elif re.search(r'[\w|\s]+Bendigo',area):
        new_area_2015.append('Bendigo')
    elif re.search(r'[\w|\s]+Geelong',area):
        new_area_2015.append('Geelong')
    elif re.search(r'[\w|\s]+Horsham',area):
        new_area_2015.append('Horsham')
    elif re.search(r'[\w|\s]+Latrobe',area):
        new_area_2015.append('Latrobe')
    elif re.search(r'[\w|\s]+Mildura',area):
        new_area_2015.append('Mildura')
    elif re.search(r'[\w|\s]+Shepparton',area):
        new_area_2015.append('Shepparton')
    elif re.search(r'[\w|\s]+Wangaratta',area):
        new_area_2015.append('Wangaratta')
    elif re.search(r'[\w|\s]+Warrnambool',area):
        new_area_2015.append('Warrnambool')
    elif re.search(r'[\w|\s]+Wodonga',area):
        new_area_2015.append('Wodonga')    
    else:
        new_area_2015.append(area)        
ch2015['Local Government Area'] = new_area_2015

for area in ch2019['Local Government Area']:
    if re.search(r'[\w|\s]+Ballarat',area):
        new_area_2019.append('Ballarat')
    elif re.search(r'[\w|\s]+Bendigo',area):
        new_area_2019.append('Bendigo')
    elif re.search(r'[\w|\s]+Geelong',area):
        new_area_2019.append('Geelong')
    elif re.search(r'[\w|\s]+Horsham',area):
        new_area_2019.append('Horsham')
    elif re.search(r'[\w|\s]+Latrobe',area):
        new_area_2019.append('Latrobe')
    elif re.search(r'[\w|\s]+Mildura',area):
        new_area_2019.append('Mildura')
    elif re.search(r'[\w|\s]+Shepparton',area):
        new_area_2019.append('Shepparton')
    elif re.search(r'[\w|\s]+Wangaratta',area):
        new_area_2019.append('Wangaratta')
    elif re.search(r'[\w|\s]+Warrnambool',area):
        new_area_2019.append('Warrnambool')
    elif re.search(r'[\w|\s]+Wodonga',area):
        new_area_2019.append('Wodonga')    
    else:
        new_area_2019.append(area)        
ch2019['Local Government Area'] = new_area_2019

ch2015 = ch2015[ch2015['Local Government Area'].isin(Top10city)]     
ch2019 = ch2019[ch2019['Local Government Area'].isin(Top10city)]
new_crime_count2015 = []
new_crime_count2019 = []
pattern = r'(\d+),(\d+)'

for num in ch2015['Incidents Recorded']:
    if re.search(pattern,num):
        new_crime_count2015.append(re.sub(pattern,r'\1\2',num))
    else:
        new_crime_count2015.append(num)
        
for num in ch2019['Incidents Recorded']:
    if re.search(pattern,num):
        new_crime_count2019.append(re.sub(pattern,r'\1\2',num))
    else:
        new_crime_count2019.append(num)
ch2015['Incidents Recorded'] = new_crime_count2015
ch2019['Incidents Recorded'] = new_crime_count2019
ch2015[['Incidents Recorded']] = ch2015[['Incidents Recorded']].astype(int)
ch2019[['Incidents Recorded']] = ch2019[['Incidents Recorded']].astype(int)

crime2015 = ch2015.groupby("Local Government Area").agg({'Incidents Recorded':'sum'})
crime2019 = ch2019.groupby("Local Government Area").agg({'Incidents Recorded':'sum'})

crime2015.to_csv('10crime2015.csv')
crime2019.to_csv('10crime2019.csv')
