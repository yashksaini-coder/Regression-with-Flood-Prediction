from colorama import Style, Fore  # noqa: F401
import great_tables as GT,style ,exibble, from_column, loc
from preprocess import Statistic
import load

train = load.load_train()

stat = Statistic(train,False)
GT(stat)\
    .tab_header(title='Descriptive Statistic - Train', subtitle='Numeric Fields')\
    .data_color(columns=['min','max','mean'],palette=['lightblue','lightcoral'],alpha=0.5)\
    .fmt_percent(columns=['%unique','%null'])