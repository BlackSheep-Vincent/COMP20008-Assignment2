import pandas as pd
import re
import matplotlib.pyplot as plt

ch = pd.read_csv("crime.csv", encoding='ISO-8859-1')
ch.rename(columns={"ï»¿Year":"Year"}, inplace=True)

ch2015 = ch.drop(ch[ch["Year"]!=2015].index).copy()
ch2019 = ch.drop(ch[ch["Year"]!=2019].index).copy()

new_crime_count2015 = []
new_crime_count2019 = []
pattern = r'(\d+),(\d+)'

for num in ch2015['Incidents Recorded']:
    if re.search(pattern,num):
        new_crime_count2015.append(re.sub(pattern,r'\1\2',num))
    else:
        new_crime_count2015.append(num)
        
for nums in ch2019['Incidents Recorded']:
    if re.search(pattern,nums):
        new_crime_count2019.append(re.sub(pattern,r'\1\2',nums))
    else:
        new_crime_count2019.append(nums)

ch2015['Incidents Recorded'] = new_crime_count2015
ch2019['Incidents Recorded'] = new_crime_count2019

ch2015[['Incidents Recorded']] = ch2015[['Incidents Recorded']].astype(int)
ch2019[['Incidents Recorded']] = ch2019[['Incidents Recorded']].astype(int)

crime2015 = ch2015.groupby("Local Government Area").agg({'Incidents Recorded':'sum'})
crime2019 = ch2019.groupby("Local Government Area").agg({'Incidents Recorded':'sum'})

crime2015.to_csv('crime2015.csv')
crime2019.to_csv('crime2019.csv')

ccrime2015 = pd.read_csv("crime2015.csv", encoding='ISO-8859-1')
ccrime2019 = pd.read_csv("crime2019.csv", encoding='ISO-8859-1')
school2015 = pd.read_csv("school_2015_new.csv", encoding='ISO-8859-1')
school2019 = pd.read_csv("school_2019_new.csv", encoding='ISO-8859-1')

plt.scatter(school2015.loc[:,'number_of_schools'],ccrime2015.loc[:,'Incidents Recorded'], label = 2015)
plt.scatter(school2019.loc[:,'number_of_schools'],ccrime2019.loc[:,'Incidents Recorded'], label = 2019)
plt.xlabel("#schools/LGA")
plt.ylabel("#CrimeIncidents/LGA")
plt.legend()
plt.grid(True)
plt.savefig("scatter plot of number of schools and crime incidents of 2015 and 2019.png")