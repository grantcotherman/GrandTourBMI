# Did the Introduction of Biological Passports Result in Lower BMIs in GC Winners?

In this project, I wanted to investigate the question of whether or not the more stringent testing protocols brought on by the biological passport resulted in GC competitors that had a lower BMI. If so, this could mean that the drugs used by GC winners allowed them to carry more mass than what would be otherwise optimal.

## Note for the reader

In professional cycling there are three grand tours that last three weeks. The Giro d'Italia, the Tour de France, and the Vuelta a Espana. For each of these races there are three primary competitions - the Grand Contender (GC) Classification, the Mountains Classification, and the Points Classification. While I retrieved data for each of these, the project focuses on the GC classification which is won by having the lowest combined time for all stages. 

As with all sports with money involved, professional cycling has had problems with riders using performance enhanding drugs (PEDs) to gain an unfair advantage over their competition. While testing was commonplace throughout the 90s and early 2000s, it wasn't until 2008 that a system came along that made testing significantly harder to work around as a cheater, thereby making the sport much cleaner overall. This system is known as the Biological Passport and allows officials to look at testing results over time to check for abnormalities or inconsistencies in the results and markers. 


## Scraping and Visualization

First, I scraped the necessary data from wikipedia for each grand tour and then added in height and weight from procyclingstats.com before calculating BMI. Afterwards, I gave each csv two rows showing what competition and race it was from. Then, I combined the csvs using pandas.

Using Tableau, I created the dashboard below.

![GC_BMI_Dahsboard](https://github.com/grantcotherman/GrandTourBMI/assets/94634170/c5689dc4-0136-465f-a367-5ee4a19a1548)

In summary, there certainly appears to be a correlation between the implementation of biological passports and a decrease in the average BMI for GC winners. While I believe there is some causation, enhances in exercise science and nutrition is as likely a cause as the increase in more rigorous testing.
