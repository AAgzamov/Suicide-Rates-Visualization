import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize = (7, 7), dpi = 100)

labels = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
percentage = [9, 58, 33]

bars = plt.bar(labels, percentage, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)

bars[0].set_hatch('o')

plt.title('Deaths by cause in world in 1990', fontdict = {'fontsize': 17, 'fontweight': 'bold'})
plt.xlabel('Deaths causes', fontdict = {'fontsize': 15, 'fontstyle': 'italic'})
plt.ylabel('Percentage of deaths', fontdict = {'fontsize': 14, 'fontstyle': 'italic'})
#plt.yticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

plt.show()

#plt.savefig('pic_01.png', dpi = 100)
