#! /usr/bin/env python3

# coding: utf-8

# # KPIs

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

commits = pd.read_csv('kpis.csv', parse_dates=True, index_col='date')
commits['total']= commits.private + commits.support + commits.jupyter + commits.tableau
commits['total_median'] = commits['total'].median()

title = 'Key Performance Indicator'
subtitle = 'Git Commits'
ylabel = 'Commits'
xlabel = 'Date'

ax1 = plt.subplot(111)
commits.plot.line(y='private', ax=ax1, color='red', \
                  marker='o', markersize='3', label='Private')
commits.plot.line(y='support', ax=ax1, color='blue', \
                  marker='o', markersize='3', label='Support')
commits.plot.line(y='jupyter', ax=ax1, color='green', \
                  marker='o', markersize='3', label='Jupyter')
commits.plot.line(y='tableau', ax=ax1, color='yellow', \
                  marker='o', markersize='3', label='Tableau')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.tick_params(direction='out')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title(title + '\n' + subtitle)
ax1.set_ylabel(ylabel)
ax1.set_xlabel(xlabel)
ax1.axis('auto')
ax1.legend(frameon=False)
ax1.figure.savefig('kpi_commits.svg', format='svg')
ax1.figure.savefig('kpi_commits.pdf', format='pdf')

ax2 = plt.subplot(111)
commits.plot.line(y='total', ax=ax2, color='blue', \
                  marker='o', markersize='3', label='Total commits')
commits.plot.line(y='total_median', ax=ax2, color="red", \
         linewidth=1.0, linestyle="-", label='Median')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.tick_params(direction='out')
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')
ax2.set_title(title + '\n' + subtitle)
ax2.set_ylabel(ylabel)
ax2.set_xlabel(xlabel)
ax2.axis('auto')
ax2.legend(frameon=False)
ax2.figure.savefig('kpi_commits_total.svg', format='svg')
ax2.figure.savefig('kpi_commits_total.pdf', format='pdf')
