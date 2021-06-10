import matplotlib.pyplot as plt
import pandas as pd

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

#plt.savefig('intro.png')
plt.show()

