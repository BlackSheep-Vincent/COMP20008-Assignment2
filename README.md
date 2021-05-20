# assignment2
group members:
Junyan Li 1048394, Ziyi Wang 1166087, Xiangyi He 1166146, Zongchao Xie 1174047

operation order:

1. save_crime_data_of_10_cities.py

This file does the prepocessing of the crime dataset including extracting the data in the year of 2015 and 2019 and adding up the total number of crime incidents in each area, and produce two csv files which contains the number of crime incidents in the 10 largest regional cities in Victoria of the year 2015 and 2019 named "10crime2015" and "10crime2019". This csv file will be used in the visualisation of the data.

2. plot_bar_chart_of_10_cities.py

This file does the preprocessing of the school dataset including adding up the total number of schools in each local government area(LGA) and removing the braket and the contents inside after the name of the local government area. This file produce two csv files which contains the number of schools in all the 79 LGA for the year 2015 and 2019 named "school_2015_new" and "school_2019_new" and two csv files which contains the number of schools in the 10 largest regional cities in Victoria named "school_2015_new2" and "school_2019_new2". This four csv files will be used in the visualisation of the data.

Also, this file produce bar chars of the number schools and number of crime incidents in 2015 and 2019. Blue represents the number of crime incidents and orange represents the number of schools.

3. scatter_plot_of_79_areas.py

This file produce two csv files which contains the number of crime incidents of the all 79 LGA in 2015 and 2019 and also plot the scatter plot of the the number schools and number of crime incidents in 2015 and 2019 on the same plot.