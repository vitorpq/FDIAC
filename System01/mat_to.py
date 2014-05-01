# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 15:07:06 2014

@author: Vítor Emmanuel Andrade

Converte o MAT-file para um dictionary com Pandas DataFrames para cada faixa de
Padrão
"""

import pandas as pd
from scipy import io
from scipy import arange

# Carrega os dados do MAT-file
MAT = io.loadmat('Dados_Sist01_train.mat')
dd = {} # Cria um dictionary vazio

for padrao in arange(MAT['Padrao'].size): # Faz a iteração nos padrões
    
    # print MAT['Padrao'][padrao][0][0] # Usado para saber os nomes dos padrões
    name = MAT['Padrao'][padrao][0][0] #
    
    # Cria um dicionário com o nome do Padrão como index e o item é um DataFrame
    # Cada DataFrame usa como Index o tempo e tem 3 colunas - Temperature,
    # Pattern e Class
    dd[name] = pd.DataFrame(MAT['UsedData'][MAT['UsedData'][:, 1]==padrao], \
               columns = ['Temperature', 'Pattern', 'Class'], \
               index = \
               pd.date_range('2008-01-01', \
               periods = \
               MAT['UsedData'][MAT['UsedData'][:, 1]==padrao].shape[0], freq='30s'))

# Após converter os dados para um DF, insere em um único dict
Data = dict(dd)

# Salva os dados no formato Pickle do Python
pd.io.pickle.to_pickle(Data, 'Dados_Sist01_train.pdy')
#store = pd.io.pytables.HDFStore('Dados_Sist01_train.h5')
#store['Dados'] = Data
#store.close()


    
    

# Dados Normais

#NORMAL = MAT['UsedData'][MAT['UsedData'][:, 1]==0]
#
#DATA = pd.DataFrame([pd.DataFrame(NORMAL, columns=['Temperature', 'Pattern', \
#'Class'], index=pd.date_range('2008-01-01', periods=NORMAL[:, 0][NORMAL[:, 1]==0].size, freq='30s'))})

