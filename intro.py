import matplotlib.pyplot as plt
import pandas as pd


print("Suicide is the act of intentionally causing one's own death.")

x = [5, 10, 15, 20, 25]
y = [30, 35, 10, 5, 20]

plt.figure(figsize = (4, 4), dpi = 150)
plt.plot(x, y, '#0be341')

plt.title('Example graph')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()