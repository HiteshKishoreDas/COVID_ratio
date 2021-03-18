#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:40:44 2020

@author: hitesh
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def plot_fig (cases_data,deaths_data,N,txt,logflag=False):
    
    cases_avg = pd.Series(cases_data[:,1]).rolling(window=N).mean().iloc[N-1:].values
    deaths_avg = pd.Series(deaths_data[:,1]).rolling(window=N).mean().iloc[N-1:].values
    
    plt.figure(figsize=(10,10))
    
    if logflag:
        plt.yscale('log')
    
    zero_arr = np.zeros_like(cases_data[:,0])+1.
    
    plt.plot(cases_data[:,0],zero_arr,linestyle='dashed',c='k')
    
    plt.plot(cases_data[:,0],cases_data[:,1],color='r',linestyle=':',label='New cases ratio')
    plt.plot(cases_data[int(N/2):-int(N/2),0],cases_avg,color='r',linewidth=2,label='Rolling mean of new cases \nratio over 7 days')
    
    plt.plot(deaths_data[:,0],deaths_data[:,1],color='b',linestyle=':',label='New deaths ratio')
    plt.plot(deaths_data[int(N/2):-int(N/2),0],deaths_avg,color='b',linewidth=2,label='Rolling mean of new deaths \nratio over 7 days')
    
    plt.xlabel('Number of days from 04-03-2020',fontsize=15)
    plt.ylabel('Ratio of new cases(or deaths) in Nth and (N-1)th day',fontsize=15)
    
    plt.tick_params(labelsize=15)
    
    plt.legend(fontsize=15)
    plt.savefig(txt+'.png')
    

cases_data = np.loadtxt('cases_data.csv')
deaths_data = np.loadtxt('deaths_data.csv')

plot_fig (cases_data,deaths_data,7,'Ratio_plot_full',True)

cases_data = cases_data[40:]
deaths_data = deaths_data[40-22:]

plot_fig (cases_data,deaths_data,7,'Ratio_plot_recent')
