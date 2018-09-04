"""
Different plotting utilities are defined in this file. 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def barplot_survived_rate(df:pd.DataFrame,x:str,title:str,y:str = 'Survived',color='Blues_d'):
    total = df.groupby(x).count()
    percentage = df[df[y]==1][[x,y]].groupby(x).count()/total
    percentage = percentage.reset_index()
    barplot = sns.barplot(data=percentage,x=x,y=y,palette=color)
    barplot.set_ylabel('Survival Rate')
    barplot.set_title(f'Survival Rate Based on {title}')
    return barplot