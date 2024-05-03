import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
# Disable all warnings
warnings.filterwarnings ('ignore')


from great_tables import GT, style ,exibble, from_column, loc  # noqa: E402, F401
from colorama import Style, Fore  # noqa: E402, F401

palette = ["d9ed92","b5e48c","99d98c","76c893","52b69a","34a0a4","168aad","1a759f","1e6091","184e77"]

config = {
    'SEED' : 42,
    'N_SPLITS': 5,
    'SUBMIT' : True,
    'USE_ORIGINAL': False
    
}

sns.set_theme(style = 'white', palette = 'colorblind')
pal = sns.color_palette('colorblind')

pd.set_option('display.max_rows', 100) 
pd.options.mode.chained_assignment = None
warnings.simplefilter(action='ignore', category=FutureWarning)