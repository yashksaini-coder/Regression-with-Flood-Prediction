# Importing the basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from colorama import Style, Fore  # noqa: F401
from great_tables import GT, style ,exibble, from_column, loc
from preprocess import Statistic, min_max_unique
import load

train = load.load_train()
test = load.load_test()
TARGET = 'FloodProbability'

# Train statistics
stat = Statistic(train,False)

GT(stat)\
    .tab_header(title='Descriptive Statistic - Train', subtitle='Numeric Fields')\
    .data_color(columns=['min','max','mean'],palette=['lightblue','lightcoral'],alpha=0.5)\
    .fmt_percent(columns=['%unique','%null'])

# Test statistics    
stat = Statistic(test,False)

GT(stat)\
    .tab_header(title='Descriptive Statistic - Test', subtitle='Numeric Fields')\
    .data_color(columns=['min','max','mean'],palette=['lightblue','lightcoral'],alpha=0.5)\
    .fmt_percent(columns=['%unique','%null'])

# Min-Max statistics

s = min_max_unique(train.drop(TARGET,axis=1),test)

GT(s)\
    .tab_header(title='Min Max Uniques', subtitle='Train and Test datasets')\
    .data_color(columns=['columns'],palette=['lightgray','lightgray'])
    
# Correlation Plot
def plot_correlation(df,label=''):
    corr = df._get_numeric_data().corr(method='spearman')
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)]=True
    fig, ax = plt.subplots(figsize=(25,17))
    sns.heatmap(data=corr, 
                mask=mask,annot=True,
                cmap='icefire',annot_kws={'size': 12, 'rotation': 45},
                ax=ax,linewidths=.5
                )
    ax.set_title(f'Correlation {label}',fontsize=25, fontweight='bold')
