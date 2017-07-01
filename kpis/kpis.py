#! /usr/bin/env python3

# coding: utf-8

# # KPIs

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

commits = pd.read_csv('kpis.csv')
commits['total']= commits.private + commits.support + commits.jupyter + commits.tableau

total_median = commits['total'].median()
total_xmin = commits['datenum'].min()
total_xmax = commits['datenum'].max()

graphtitle = 'Key Performance Indicator'
graphsubtitle = 'Git Commits'
graphylabel = 'Number of commits'
graphxlabel = 'Day'

ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.tick_params(direction='out')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(commits.datenum, commits.private, marker='o', color="red", linewidth=1.0, markersize=3, linestyle="-", label="private/", )
plt.plot(commits.datenum, commits.support, marker='o', color="blue", linewidth=1.0, markersize=3, linestyle="-", label="support/")
for i, txt in enumerate( commits.supportnote ):
    ax.annotate( txt, ( commits.datenum[i] + .5, commits.support[i] + .5 ), color="blue" )
plt.plot(commits.datenum, commits.jupyter, marker='o', color="green", linewidth=1.0, markersize=3, linestyle="-", label="jupyter/")
plt.plot(commits.datenum, commits.tableau, marker='o', color="yellow", linewidth=1.0, markersize=3, linestyle="-", label="tableau/")
plt.title(graphtitle + '\n' + graphsubtitle)
plt.ylabel(graphylabel)
plt.xlabel(graphxlabel)
ax.legend(loc='upper left', scatterpoints=1, frameon=False)
plt.savefig('kpi_commits.svg', format='svg')
plt.savefig('kpi_commits.pdf', format='pdf')
plt.show()


ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.tick_params(direction='out')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(commits.datenum, commits.total, marker='o', color="blue", linewidth=1.0, markersize=3, linestyle="-", label="total", )
plt.plot([total_xmin, total_xmax], [total_median, total_median], color="red",          linewidth=1.0,          linestyle="-", label="median", )
plt.title(graphtitle + '\n' + graphsubtitle)
plt.ylabel(graphylabel)
plt.xlabel(graphxlabel)
plt.savefig('kpi_commits_total.svg', format='svg')
plt.savefig('kpi_commits_total.pdf', format='pdf')
plt.show()

