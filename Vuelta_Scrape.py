#Read in relevant Libraries
import pandas as pd
from lxml import html
import requests
import os

# Set working directory
os.chdir('')


# --------------------------------
# -------Vuelta GC----------------
#---------------------------------

#Get HTML from website
wikiurl = "https://en.wikipedia.org/wiki/List_of_Vuelta_a_Espa%C3%B1a_general_classification_winners" 
resp = requests.get(wikiurl)
tagtree = html.fromstring(resp.content)

# Year Column
xp_year = "//table[2]/tbody/tr/td[1]/a/text()"
year_list = tagtree.xpath(xp_year)

#Country Column
xp_country = "//table[2]/tbody/tr/td[2]/a/text()"
country_list = tagtree.xpath(xp_country)

#Rider Column
xp_rider = "//table[2]/tbody/tr/th/span/span/span/a/text()"
rider_list = tagtree.xpath(xp_rider)
#Simon Yates is missing, add back in
rider_list.insert(-4, 'Simon Yates')

#Create dataframe
Vuelta_GC_df = pd.DataFrame(
    {'Year': year_list,
     'Country': country_list,
     'Rider': rider_list})

#export to csv
#Vuelta_GC_csv = Vuelta_GC_df.to_csv('Vuelta_GC.csv', index = False)

# --------------------------------
# -------Vuelta Points------------
#---------------------------------

#Get HTML from website
wikiurl2 = "https://en.wikipedia.org/wiki/Points_classification_in_the_Vuelta_a_Espa%C3%B1a" 
resp2 = requests.get(wikiurl2)
tagtree2 = html.fromstring(resp2.content)

# Year Column
xp_year2 = "//table[5]/tbody/tr/td[1]/a/text()"
year_list2 = tagtree2.xpath(xp_year2)

#Rider Column
xp_rider2 = "//table[5]/tbody/tr/td[2]/a/text()"
rider_list2 = tagtree2.xpath(xp_rider2)

#Create a dataframe
Vuelta_PC_df = pd.DataFrame(
    {'Year': year_list2,
     'Rider': rider_list2})

#Export to CSV
#Vuelta_PC_csv = Vuelta_PC_df.to_csv('Vuelta_PC.csv', index = False)

# --------------------------------
# -------Vuelta Mountains---------
#---------------------------------

#Get HTML from website
wikiurl3 = "https://en.wikipedia.org/wiki/Mountains_classification_in_the_Vuelta_a_Espa%C3%B1a" 
resp3 = requests.get(wikiurl3)
tagtree3 = html.fromstring(resp3.content)

# Year Column
xp_year3 = "//table[4]/tbody/tr/td[1]/a/text()"
year_list3 = tagtree3.xpath(xp_year3)

#Rider Column
xp_rider3 = "//table[4]/tbody/tr/td[2]/a/text()"
rider_list3 = tagtree3.xpath(xp_rider3)

#Create a dataframe
Vuelta_MC_df = pd.DataFrame(
    {'Year': year_list3,
     'Rider': rider_list3})

#Export to CSV
Vuelta_MC_csv = Vuelta_MC_df.to_csv('Vuelta_MC.csv', index = False)
