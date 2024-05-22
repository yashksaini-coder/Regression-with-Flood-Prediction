# Importing the basic libraries
import pandas as pd
import seaborn as sns

from pandas.plotting import register_matplotlib_converters
import warnings

pal = sns.color_palette('colorblind')

pd.set_option('display.max_rows', 100)
pd.set_option('plotting.backend', 'matplotlib')
register_matplotlib_converters()
pd.options.mode.chained_assignment = None
warnings.simplefilter(action='ignore', category=FutureWarning)
