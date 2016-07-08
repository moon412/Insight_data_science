# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 19:40:43 2016

@author: yzhao03
Insight data science fellowship
"""
import os
os.getcwd()
#os.chdir('D:\courses\insight_data_science')
os.chdir('D:\Yue\DATA\Healthy_AD_ADRCAG\AD_ADRCAG_Healthy_Rdata')
import pandas as pd
import numpy as np
import scipy.stats 
import matplotlib.pyplot as plt
R2s_AD = pd.read_csv('data\R2s_mean.csv', na_values=['NA'], 
                     index_col=['subject'])
R2s_AD.head(n=5)
SUVR_all = pd.read_table('data\suvr.txt', index_col=['subject'])
SUVR_AD = SUVR_all.loc['AD4':'ADRCAG-99',]
mask= ~(SUVR_AD['amyloid'] == 'unknow')
R2s = R2s_AD.ix[mask, ]
SUVR = SUVR_AD.ix[mask, ]

R2s_data = R2s.ix[:, 'ctx-bankssts':'amygdala']
SUVR_data = SUVR.ix[:, 'ctx-bankssts':'amygdala']
paircorr = R2s_data.corrwith(SUVR_data)
paircorr.plot(kind='bar')
#from pandas.tools.plotting import scatter_matrix
#axes = scatter_matrix(SUVR.ix[:,8:11])
fig, axes = plt.subplots(6, 7, sharex=False, sharey=True)
counter = 1
for i in range(6):
    for j in range(7):
        axes[i, j].scatter(R2s_data.icol(counter), SUVR_data.icol(counter))
        counter += 1

import bokeh.plotting
fig = bokeh.plotting.figure()
fig.line(R2s_data['ctx-parahippocampal'], SUVR_data['ctx-parahippocampal'],
         legend='ctx-parahippocampal')
bokeh.plotting.show(fig)  

       