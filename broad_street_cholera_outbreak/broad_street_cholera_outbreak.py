#! /usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
deaths = pd.read_csv('snow_cholera_deaths.csv')
pumps = pd.read_csv('snow_cholera_pumps.csv')
graphtitle = 'Broad Street Cholera Outbreak of 1854'
graphsubtitle = 'Soho, London, UK'
graphylabel = 'Distance from datum (m)'
graphxlabel = 'Distance from datum (m)'
plt.figure(figsize=(8,6), dpi=100)
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.tick_params(direction='out')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.scatter(deaths['x'], deaths['y'], color="blue", \
           linewidth=0, linestyle="-", s=10, label="Deaths")
ax.scatter(pumps['x'], pumps['y'], color="red", \
           linewidth=0, linestyle="-", s=10, label="Pumps")
plt.title(graphtitle + '\n' + graphsubtitle)
plt.ylabel(graphylabel)
plt.xlabel(graphxlabel)
ax.legend(scatterpoints=1, frameon=False)
plt.ylim(ymin=4, ymax=20)
plt.xlim(xmin=8, xmax=19)
plt.savefig('broad_street_cholera_outbreak.svg', format='svg');
plt.savefig('broad_street_cholera_outbreak.pdf', format='pdf');
plt.show()
