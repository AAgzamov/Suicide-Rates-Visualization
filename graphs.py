import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----  ---- Graph 1 ---- ----
# reference: https://ourworldindata.org/causes-of-death
# The share of deaths from injuries, infectious diseases, and non-communicable diseases

# Creating labels and percentage for deaths by cause in 1990.
l_1990 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_1990 = [9, 58, 33]

# Creating labels and percentage for deaths by cause in 2000.
l_2000 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_2000 = [9, 62, 29]

# Creating labels and percentage for deaths by cause in 2010.
l_2010 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_2010 = [9, 67, 24]

# Creating labels and percentage for deaths by cause in 2017.
l_2017 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_2017 = [8, 73, 19]

# Creating a figure with dimension of 2 rows and 2 columns for subplotting.
fig, axs = plt.subplots(2, 2, figsize = (11, 9))

# Creating a bar chart with the label and percentage of 1990 and storing it in variable 'bars_1990'.
bars_1990 = axs[0, 0].bar(l_1990, p_1990, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[0, 0].set_title('Deaths by cause in the world in 1990', fontdict = {'fontweight': 'bold', 'fontsize':13}) # Setting a title for the bar chart.
axs[0, 0].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13}) # Setting xlabel
axs[0, 0].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_1990[0].set_hatch('.') # Setting the hatch for the first bar in the bar chart.

bars_2000 = axs[0, 1].bar(l_2000, p_2000, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[0, 1].set_title('Deaths by cause in the world in 2000', fontdict = {'fontweight': 'bold', 'fontsize':13})
axs[0, 1].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
axs[0, 1].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_2000[0].set_hatch('.')

bars_2010 = axs[1, 0].bar(l_2010, p_2010, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[1, 0].set_title('Deaths by cause in the world in 2010', fontdict = {'fontweight': 'bold', 'fontsize':13})
axs[1, 0].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
axs[1, 0].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_2010[0].set_hatch('.')

bars_2017 = axs[1, 1].bar(l_2017, p_2017, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[1, 1].set_title('Deaths by cause in the world in 2017', fontdict = {'fontweight': 'bold', 'fontsize':13})
axs[1, 1].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
axs[1, 1].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_2017[0].set_hatch('.')


# Setting yticks for the bar charts.
for ax in axs.flat:
    ax.set(yticks = [10, 20, 30, 40, 50, 60, 70])
    
# Removing xlabels and y labels between the bar charts.
#for ax in axs.flat:
#    ax.label_outer()

# Setting the space between each bar chart.
fig.tight_layout(pad = 4.0)

#plt.savefig('intro.png', dpi = 150)
plt.show()


# ----  ---- Graph 2 ---- ----
# reference: https://ourworldindata.org/suicide
# Share of deaths from suicide

# Importing information from .csv file to a variable 'data'.
data = pd.read_csv('share-deaths-suicide.csv')

# Creating new column 'Death' and removing long column of 'Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)'.
data['Deaths'] = data['Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)']
data = data.drop(columns=['Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)'])

# Removing data rows of countries which are not Greenland, the USA, Russia, Sri Lanka, South Korea, or Uzbekistan. 
data = data.drop(index=data[(data['Entity'] != 'Greenland') & (data['Entity'] != 'United States') & (data['Entity'] != 'Russia') & (data['Entity'] != 'Grenada') & (data['Entity'] != 'South Korea') & (data['Entity'] != 'Uzbekistan')].index)

data = data.sort_values('Entity')

# Locating data year by year. (If loop method is available, it is welcome)
year_1990 = data.loc[data['Year'] == 1990]
year_1991 = data.loc[data['Year'] == 1991]
year_1992 = data.loc[data['Year'] == 1992]
year_1993 = data.loc[data['Year'] == 1993]
year_1994 = data.loc[data['Year'] == 1994]
year_1995 = data.loc[data['Year'] == 1995]
year_1996 = data.loc[data['Year'] == 1996]
year_1997 = data.loc[data['Year'] == 1997]
year_1998 = data.loc[data['Year'] == 1998]
year_1999 = data.loc[data['Year'] == 1999]
year_2000 = data.loc[data['Year'] == 2000]
year_2001 = data.loc[data['Year'] == 2001]
year_2002 = data.loc[data['Year'] == 2002]
year_2003 = data.loc[data['Year'] == 2003]
year_2004 = data.loc[data['Year'] == 2004]
year_2005 = data.loc[data['Year'] == 2005]
year_2006 = data.loc[data['Year'] == 2006]
year_2007 = data.loc[data['Year'] == 2007]
year_2008 = data.loc[data['Year'] == 2008]
year_2009 = data.loc[data['Year'] == 2009]
year_2010 = data.loc[data['Year'] == 2010]
year_2011 = data.loc[data['Year'] == 2011]
year_2012 = data.loc[data['Year'] == 2012]
year_2013 = data.loc[data['Year'] == 2013]
year_2014 = data.loc[data['Year'] == 2014]
year_2015 = data.loc[data['Year'] == 2015]
year_2016 = data.loc[data['Year'] == 2016]
year_2017 = data.loc[data['Year'] == 2017]

# Start plotting a graph.
x = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
y = [year_1990.Deaths, year_1991.Deaths, year_1992.Deaths, year_1993.Deaths, year_1994.Deaths, year_1995.Deaths, year_1996.Deaths, year_1997.Deaths, year_1998.Deaths, year_1999.Deaths, year_2000.Deaths, year_2001.Deaths, year_2002.Deaths, year_2003.Deaths, year_2004.Deaths, year_2005.Deaths, year_2006.Deaths, year_2007.Deaths, year_2008.Deaths, year_2009.Deaths, year_2010.Deaths, year_2011.Deaths, year_2012.Deaths, year_2013.Deaths, year_2014.Deaths, year_2015.Deaths, year_2016.Deaths, year_2017.Deaths]

plt.figure(figsize = (10, 6))
plt.title('Share of deaths from suicide, 1990 to 2017', fontdict = {'size': 15, 'weight': 'bold'})
plt.ylabel('Percentage of deaths from suicide', fontdict = {'size': 12})
plt.xticks([1990, 1995, 2000, 2005, 2010, 2015, 2017])
plt.yticks([2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 8, 10, 12, 13, 14])
plt.plot(x, y, '.-', label=['Greenland', 'Grenada', 'Russia', 'South Korea', 'United States', 'Uzbekistan'])
plt.legend()
#plt.savefig('deaths-from-suicide.png', dpi = 150)
plt.show()


# ----  ---- Graph 3 ---- ----
# reference: https://ourworldindata.org/suicide
# Share of deaths from suicide in Uzbekistan, United States, and Kazakhstan

# Altering the data structure in the .csv file and storing it in 'info' variable.
info = pd.read_csv('share-deaths-suicide.csv')
info['Deaths'] = info['Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)']
info = info.drop(columns=['Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)'])
info = info.drop(index=info[(info['Entity'] != 'United States') & (info['Entity'] != 'Uzbekistan') & (info['Entity'] != 'Kazakhstan')].index)
info = info.sort_values('Entity')

# Locating data by country and removing redundant data rows in accordance with the year.
kz = info.loc[info['Entity'] == 'Kazakhstan']
kz = kz.sort_values('Year')
kz = kz.drop(index=kz[(kz['Year'] != 1990) & (kz['Year'] != 2000) & (kz['Year'] != 2010) & (kz['Year'] != 2017)].index)

usa = info.loc[info['Entity'] == 'United States']
usa = usa.sort_values('Year')
usa = usa.drop(index=usa[(usa['Year'] != 1990) & (usa['Year'] != 2000) & (usa['Year'] != 2010) & (usa['Year'] != 2017)].index)

uzb = info.loc[info['Entity'] == 'Uzbekistan']
uzb = uzb.sort_values('Year')
uzb = uzb.drop(index=uzb[(uzb['Year'] != 1990) & (uzb['Year'] != 2000) & (uzb['Year'] != 2010) & (uzb['Year'] != 2017)].index)

# Setting 'x' values for a bar chart and a 'width' value.
years = [1990, 2000, 2010, 2017]
x_indexes = np.arange(len(years))
width = 0.25

# Configuring a bar chart
plt.figure(figsize = (8.5, 5))
plt.title('Deaths from suicide in Uzbekistan, United States, and Kazakhstan, 1990 to 2017')
plt.xticks(ticks = x_indexes, labels = years)
plt.ylabel('Percentage')

plt.bar(x_indexes, usa.Deaths, width = width, label = 'the USA')
plt.bar(x_indexes - width, uzb.Deaths, width = width, label = 'Uzbekistan')
plt.bar(x_indexes + width, kz.Deaths, width = width, label = 'Kazakhstan')

plt.legend()
#plt.savefig('uzb-us-kz-deaths.png')
plt.show()


# ----  ---- Graph 4 ---- ----
# reference: https://ourworldindata.org/causes-of-death
# Suicide rates by age in Uzbekistan, 1990 and 2017

# Reading a data set from .csv file and storing it in 'data' variable.
data = pd.read_csv('suicide-rates-by-age-detailed.csv')

# Configuring columns of the data set.
data['5-14 years'] = data['Deaths - Self-harm - Sex: Both - Age: 5-14 years (Rate)']
data['15-49 years'] = data['Deaths - Self-harm - Sex: Both - Age: 15-49 years (Rate)']
data['50-69 years'] = data['Deaths - Self-harm - Sex: Both - Age: 50-69 years (Rate)']
data['70+ years'] = data['Deaths - Self-harm - Sex: Both - Age: 70+ years (Rate)']

data = data.drop(columns = ['Deaths - Self-harm - Sex: Both - Age: 15-49 years (Rate)', 'Deaths - Self-harm - Sex: Both - Age: 70+ years (Rate)', 'Deaths - Self-harm - Sex: Both - Age: 50-69 years (Rate)', 'Deaths - Self-harm - Sex: Both - Age: 5-14 years (Rate)'])
data = data.drop(columns = ['Deaths - Self-harm - Sex: Both - Age: All Ages (Rate)', 'Code'])

data = data.drop(index=data[data['Entity'] != 'Uzbekistan'].index)
y_1990 = data.drop(index=data[data['Year'] != 1990].index)
y_2017 = data.drop(index=data[data['Year'] != 2017].index)

# Creating a subplot of horizontal bar charts with the dimension of 2 rows and 1 column.
# Suicide rates are the number of deaths per suicide measured per 100,000 individuals in a given demographic.
fig, axs = plt.subplots(2, 1, figsize=(13, 6), sharex=True) # 'sharex=True' is responsible for sharing 'xticks'

objects = ['5-14 years', '15-49 years', '50-69 years', '70+ years']
rate_1990 = [float(y_1990['5-14 years']), float(y_1990['15-49 years']), float(y_1990['50-69 years']), float(y_1990['70+ years'])]
rate_2017 = [float(y_2017['5-14 years']), float(y_2017['15-49 years']), float(y_2017['50-69 years']), float(y_2017['70+ years'])]

# The first bar chart
axs[0].set_title('Suicide rates by age in Uzbekistan, 1990')
axs[0].set_xticks(np.array(range(16)))
axs[0].barh(objects, rate_1990)

# The second bar chart
axs[1].set_title('Suicide rates by age in Uzbekistan, 2017')
axs[1].barh(objects, rate_2017)

#plt.savefig('suicide-rates-by-age-uzb.png')
plt.show()
