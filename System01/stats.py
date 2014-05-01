# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 01:13:33 2014

@author: vitor
"""

import scipy as sp
from scipy.stats import normaltest, norm, ttest_ind, mannwhitneyu, \
 ks_2samp, skewtest
import pandas as pd
import pylab as pl

pl.figure(num=None, figsize=(15, 8), dpi=500, facecolor='w', edgecolor='k', \
    frameon=True)

MAT = sp.io.loadmat('/home/vitor/Dropbox/Pos-Graduacao/Codigo/Datasets/FDIAC/\
Dados_Sist01_train.mat')
VAL = sp.io.loadmat('/home/vitor/Dropbox/Pos-Graduacao/Codigo/Datasets/FDIAC/\
Dados_Sist01_val.mat')

DADOS = pd.DataFrame(MAT['UsedData'], columns = ['Temperature', 'Pattern', \
'Class'])

VAL_DATA = pd.DataFrame(VAL['UsedVal'], columns = ['Temperature', 'Pattern', \
'Class'])

DR = pd.date_range('2008-01-01', \
periods=DADOS['Temperature'][DADOS['Pattern']==0].size, freq='30s')
NORMAL = pd.Series(DADOS['Temperature'][DADOS['Pattern']==0].values, index=DR)

DR_VAL = pd.date_range('2008-01-01', \
periods=VAL_DATA['Temperature'][VAL_DATA['Pattern']==0].size, freq='30s')
NVAL = pd.Series(VAL_DATA['Temperature'][VAL_DATA['Pattern']==0].values, \
 index=DR_VAL)

print 'normal skewtest teststat = %6.3f p-value = %6.4f' \
% normaltest(NORMAL.values)
print 'normal skewtest teststat = %6.3f p-value = %6.4f' \
% normaltest(NVAL.values)
# Como o p-value é muito pequeno, os dados não são normais.

print 'normal skewtest teststat = %6.3f p-value = %6.4f' \
% normaltest(norm.rvs(size=1000))
pl.plot(norm.rvs(size=1000))
skewtest(norm.rvs(size=1000))

# Compare two samples
ttest_ind(NORMAL.values, NVAL.values)
mannwhitneyu(NORMAL.values, NVAL.values)
ks_2samp(NORMAL.values, NVAL.values)

pl.plot(NORMAL.index.values, NORMAL.values, '--r', NVAL.index.values, \
NVAL.values, '-b')