# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:15:24 2018

@author: Chirag
"""

#To explore GDP timeseries

#Python Libraries
import os
import pandas as pd

##########################################################################
#Constants
#########################################################################

INPUT_DIR=os.getcwd()

Inputfilename = 'USA_GDP_data.csv'

##########################################################################
#Input
#########################################################################

path = os.path.join(INPUT_DIR,Inputfilename)
gdp_data = pd.read_csv(path,index_col=0)

##########################################################################
#Data preprocessing
#########################################################################

# Converting the index as date
gdp_data.index = pd.to_datetime(gdp_data.index)
gdp_data.rename(columns={'Value':'USA'},inplace=True)

#plotting data
gdp_data.plot()