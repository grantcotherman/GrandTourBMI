#Read in relevant Libraries
import pandas as pd
from lxml import html
import requests
import os

# Set working directory
os.chdir('')

# --------------------------------
# -------Giro GC------------------
#---------------------------------

#Get HTML from website
wikiurl = "https://en.wikipedia.org/wiki/List_of_Giro_d%27Italia_general_classification_winners" 
resp = requests.get(wikiurl)
tagtree = html.fromstring(resp.content)

# Year Column
xp_year = "//table[2]/tbody/tr/td[1]/a/text()"
year_list = tagtree.xpath(xp_year)
#Drop the early years that weren't catching on the later scrapes (not needed anyway)
new_years = year_list[28:]

#Country Column part 
xp_country = "//table[2]/tbody/tr/td[2]/a/text()"
country_list = tagtree.xpath(xp_country)

#Rider Column
xp_rider = "//table[2]/tbody/tr/th/span/span/span/a/text()"
rider_list = tagtree.xpath(xp_rider)
new_riders = rider_list[26:]

#Create dataframe
Giro_GC_df = pd.DataFrame(
    {'Year': new_years,
     'Country': country_list,
     'Rider': new_riders})

#export to csv
#Giro_GC_csv = Giro_GC_df.to_csv('Giro_GC.csv', index = False)


# --------------------------------
# -------Giro Points--------------
#---------------------------------

#Get HTML from website
wikiurl2 = "https://en.wikipedia.org/wiki/Points_classification_in_the_Giro_d%27Italia" 
resp2 = requests.get(wikiurl2)
tagtree2 = html.fromstring(resp2.content)

# Year Column
xp_year2 = "//table[3]/tbody/tr/td[1]/a/text()"
year_list2 = tagtree2.xpath(xp_year2)
year_list2.remove('2007')

#Country Column
xp_country2 = "//table[3]/tbody/tr/td[2]/a/text()"
country_list2 = tagtree2.xpath(xp_country2)

#Rider Column
xp_rider2 = "//table[3]/tbody/tr/th/span/span/span/a/text()"
rider_list2 = tagtree2.xpath(xp_rider2)

#Create dataframe
Giro_PC_df = pd.DataFrame(
    {'Year': year_list2,
     'Country': country_list2,
     'Rider': rider_list2})

#export to csv
#Giro_PC_csv = Giro_PC_df.to_csv('Giro_PC.csv', index = False)

# --------------------------------
# -------Giro Mountain------------
#---------------------------------

#Get HTML from website
wikiurl3 = "https://en.wikipedia.org/wiki/Mountains_classification_in_the_Giro_d%27Italia" 
resp3 = requests.get(wikiurl3)
tagtree3 = html.fromstring(resp3.content)

# Year Column
xp_year3 = "//table[3]/tbody/tr/td[1]/a/text()"
year_list3 = tagtree3.xpath(xp_year3)

#Rider Column
xp_rider3 = "//table[3]/tbody/tr/th/span/span/span/a/text()"
rider_list3 = tagtree3.xpath(xp_rider3)

#Create dataframe
Giro_MC_df = pd.DataFrame(
    {'Year': year_list3,
     'Rider': rider_list3})

#export to csv
#Giro_MC_csv = Giro_MC_df.to_csv('Giro_MC.csv', index = False)