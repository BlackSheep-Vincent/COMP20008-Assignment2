import pandas as pd
import re
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('mode.chained_assignment', None)

#read the dataset
school_2019 = pd.read_csv("school2019.csv", encoding = 'ISO-8859-1')
school_2015 = pd.read_csv("school2015.csv", encoding = 'ISO-8859-1')

#drop the outlier
school_2019_no_uni = school_2019.drop(school_2019[school_2019['LGA_Name'] == 'Unincorporated Vic'].index).copy()
school_2015_no_uni = school_2015.drop(school_2015[school_2015['LGA_Name'] == 'Unincorporated Vic'].index).copy()

#group the dataframe by the local government area and add an additinal column to get the number of schools in that area
school_2019_new = school_2019_no_uni.groupby(["LGA_Name"]).size().reset_index(name='number_of_schools')
school_2015_new = school_2015_no_uni.groupby(["LGA_Name"]).size().reset_index(name='number_of_schools')

#remove the bracket and the content inside the bracket after the name of the area
def remove_bracket(area):
    new_area=[]
    for i in area:
        i = re.sub('\s\(\w+\)','',i)
        new_area.append(i)
    s_new_area=pd.Series(new_area)
    return s_new_area
school_2019_new.loc[:,'LGA_Name'] = remove_bracket(school_2019_new.loc[:,'LGA_Name'].values)

def remove_bracket(area):
    new_area=[]
    for i in area:
        i = re.sub('\s\(\w+\)','',i)
        new_area.append(i)
    s_new_area=pd.Series(new_area)
    return s_new_area
school_2015_new.loc[:,'LGA_Name'] = remove_bracket(school_2015_new.loc[:,'LGA_Name'].values)


#remove the prefix 'great' of some area to avoid omission
def remove_great(new_area):
    remove_great = []
    for area in school_2019_new['LGA_Name']:
        if re.search(r'[\w|\s]+Ballarat',area):
            remove_great.append('Ballarat')
        elif re.search(r'[\w|\s]+Bendigo',area):
            remove_great.append('Bendigo')
        elif re.search(r'[\w|\s]+Geelong',area):
            remove_great.append('Geelong')
        elif re.search(r'[\w|\s]+Horsham',area):
            remove_great.append('Horsham')
        elif re.search(r'[\w|\s]+Latrobe',area):
            remove_great.append('Latrobe')
        elif re.search(r'[\w|\s]+Mildura',area):
            remove_great.append('Mildura')
        elif re.search(r'[\w|\s]+Shepparton',area):
            remove_great.append('Shepparton')
        elif re.search(r'[\w|\s]+Wangaratta',area):
            remove_great.append('Wangaratta')
        elif re.search(r'[\w|\s]+Warrnambool',area):
            remove_great.append('Warrnambool')
        elif re.search(r'[\w|\s]+Wodonga',area):
            remove_great.append('Wodonga')    
        else:
            remove_great.append(area)
    s_remove_great = pd.Series(remove_great)
    return s_remove_great
school_2019_new.loc[:,'LGA_Name'] = remove_great(school_2019_new.loc[:,'LGA_Name'].values)

def remove_great(new_area):
    remove_great = []
    for area in school_2015_new['LGA_Name']:
        if re.search(r'[\w|\s]+Ballarat',area):
            remove_great.append('Ballarat')
        elif re.search(r'[\w|\s]+Bendigo',area):
            remove_great.append('Bendigo')
        elif re.search(r'[\w|\s]+Geelong',area):
            remove_great.append('Geelong')
        elif re.search(r'[\w|\s]+Horsham',area):
            remove_great.append('Horsham')
        elif re.search(r'[\w|\s]+Latrobe',area):
            remove_great.append('Latrobe')
        elif re.search(r'[\w|\s]+Mildura',area):
            remove_great.append('Mildura')
        elif re.search(r'[\w|\s]+Shepparton',area):
            remove_great.append('Shepparton')
        elif re.search(r'[\w|\s]+Wangaratta',area):
            remove_great.append('Wangaratta')
        elif re.search(r'[\w|\s]+Warrnambool',area):
            remove_great.append('Warrnambool')
        elif re.search(r'[\w|\s]+Wodonga',area):
            remove_great.append('Wodonga')    
        else:
            remove_great.append(area)
    s_remove_great = pd.Series(remove_great)
    return s_remove_great
school_2015_new.loc[:,'LGA_Name'] = remove_great(school_2015_new.loc[:,'LGA_Name'].values)

#save the dataframe which contains number of schools in 79 areas
school_2015_new.to_csv('school_2015_new.csv', index=False)
school_2019_new.to_csv('school_2019_new.csv', index=False)

#extract the 10 largest regional cities is Victoria
top_10_cities = ['Ballarat','Bendigo','Geelong','Horsham','Latrobe','Mildura','Shepparton','Wangaratta','Warrnambool','Wodonga']
school_2019_new2 = school_2019_new[school_2019_new['LGA_Name'].isin(top_10_cities)]
school_2015_new2 = school_2015_new[school_2015_new['LGA_Name'].isin(top_10_cities)]

#sort the areas by the number of schools
school_2019_new2.sort_values(by=['number_of_schools'], inplace=True)
school_2015_new2.sort_values(by=['number_of_schools'], inplace=True)

#save the dataframe which contains number of schools in the 10 largest regional cities is Victoria
school_2015_new2.to_csv('school_2015_new2.csv', index=False)
school_2019_new2.to_csv('school_2019_new2.csv', index=False)

#get the number of incidents in the 10 largest cities in Victoria
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


#read cvs files of the number of crime incidents in the 10 largest regional cities is Victoria 
crime_2019 = pd.read_csv("10crime2019.csv", encoding = 'ISO-8859-1')
crime_2015 = pd.read_csv("10crime2015.csv", encoding = 'ISO-8859-1')

#sort the cities by the number of crime incidents
crime_2019.sort_values(by=['Incidents Recorded'], inplace=True)
crime_2015.sort_values(by=['Incidents Recorded'], inplace=True)

#save the sorted the dataframe
crime_2019.to_csv('crime_2019_sorted.csv', index=False)
crime_2015.to_csv('crime_2015_sorted.csv', index=False)


#plot the number of schools and number of crime incidents of the year 2019 on the same plot
labels = school_2019_new2.loc[:,'LGA_Name'].values
crime_num = crime_2019.loc[:,'Incidents Recorded'].values
school_num = school_2019_new2.loc[:,'number_of_schools'].values

x = np.arange(len(labels))
width=0.35

fig, ax = plt.subplots()
bar1 = ax.bar(x-width/2, crime_num, width, label='crime_2019')
bar1 = ax.bar(x+width/2, school_num, width, label='school_2019')

plt.title("log of the number of schools & crime incidents of 2019")
plt.xlabel("Local Government Area")
plt.ylabel("quantity")
plt.xticks(rotation=-30)
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.yscale('log')
plt.tight_layout()
plt.savefig("number of schools and number of crime incidents of the year 2019.png")

#plot the number of schools and number of crime incidents of the year 2015 on the same plot
labels = school_2015_new2.loc[:,'LGA_Name'].values
crime_num = crime_2015.loc[:,'Incidents Recorded'].values
school_num = school_2015_new2.loc[:,'number_of_schools'].values

x = np.arange(len(labels))
width=0.35

fig, ax = plt.subplots()
bar1 = ax.bar(x-width/2, crime_num, width, label='crime_2015')
bar1 = ax.bar(x+width/2, school_num, width, label='school_2015')

plt.title("log of the number of schools & crime incidents of 2015")
plt.xlabel("Local Government Area")
plt.ylabel("quantity")
plt.xticks(rotation=-30)
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.yscale('log')
plt.tight_layout()
plt.savefig("number of schools and number of crime incidents of the year 2015.png")

