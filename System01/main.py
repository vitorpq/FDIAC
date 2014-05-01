# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 19:21:39 2014

@author: Vítor Emmanuel Andrade
@email: vitor.e.a@gmail.com

FDIAC data analysis

Patterns Plots
"""

import scipy as sp
import numpy as np
import pandas as pd
from pylab import *

dados = np.load('/home/vitor/Dropbox/Pos-Graduacao/Codigo/Datasets/FDIAC/Dados_Sist01.pdy')
fig = {}
ax = {}
for padrao in dados.keys():
    '''Patterns plots'''
    fig[padrao] = figure(num=None, figsize=(12,5), dpi=500, facecolor='w', edgecolor='k', frameon=True)
    ax[padrao] = axes()
    fig[padrao].patch.set_alpha(0) # Sets the figure transparent
    ax[padrao].patch.set_alpha(0) # Sets the axis transparent
    #title(padrao)
    xlabel(r'$Time (h)$', fontsize=18)
    ylabel(r'$Temperature ^{\circ}C$', fontsize=18)
    ax[padrao].spines['left'].set_color('gray')
    ax[padrao].spines['right'].set_color('gray')
    ax[padrao].spines['top'].set_color('gray')
    ax[padrao].spines['bottom'].set_color('gray')
    ax[padrao].spines['left'].set_linewidth(2)
    ax[padrao].spines['right'].set_linewidth(2)
    ax[padrao].spines['top'].set_linewidth(2)
    ax[padrao].spines['bottom'].set_linewidth(2)
    ax[padrao].yaxis.tick_left()
    ax[padrao].xaxis.tick_bottom()
    ax[padrao].tick_params(direction='inout', length=8, width=1.5, colors='gray', labelsize=14, pad=7)
    grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
    plot(dados[padrao].index, dados[padrao].Temperature, lw=1.5)
	show()
    savefig('images/'+padrao+'.eps', type='eps', dpi=500)
    savefig('images/'+padrao+'.png', format='png', dpi=500)
