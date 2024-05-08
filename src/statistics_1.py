from colorama import Style, Fore  # noqa: F401
import great_tables as GT
from preprocess import Statistic



stat = Statistic(train,False)
GT(stat)\
    .tab_header(title='Descriptive Statistic - Train', subtitle='Numeric Fields')\
    .data_color(columns=['min','max','mean'],palette=['lightblue','lightcoral'],alpha=0.5)\
    .fmt_percent(columns=['%unique','%null'])