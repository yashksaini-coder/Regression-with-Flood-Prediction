# Importing the basic libraries
import pandas as pd
from colorama import Style, Fore
TARGET = 'FloodProbability'

def printInfo(df,train,test):
    print(f'{Style.BRIGHT}{Fore.YELLOW}SHAPE{Style.RESET_ALL}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {train.shape}')
    print(f'{Style.BRIGHT}{Fore.BLUE} test:  {test.shape}')
    print(f'{Style.BRIGHT}{Fore.GREEN} original:  {df.shape}')
    print(f'{Style.BRIGHT}{Fore.YELLOW}\nNULL VALUES{Style.RESET_ALL}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {train.isnull().any().any()}')
    print(f'{Style.BRIGHT}{Fore.BLUE} test: {test.isnull().any().any()}')
    print(f'{Style.BRIGHT}{Fore.GREEN} original: {df.isnull().any().any()}')    
    print(f'{Style.BRIGHT}{Fore.YELLOW}\nDUPLICATES{Style.RESET_ALL}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {train.duplicated().any().any()}')
    print(f'{Style.BRIGHT}{Fore.BLUE} test: {test.duplicated().any().any()}')
    print(f'{Style.BRIGHT}{Fore.GREEN} original: {df.duplicated().any().any()}')
    

def Statistic(df: pd.DataFrame(), categoric = False):  # type: ignore
    num_cols = list(df._get_numeric_data())
    cat_cols = list(df.drop(num_cols,axis=1))
    if categoric:
        desc = pd.DataFrame(index = list(df[cat_cols]))
        df = df[cat_cols]
    else:
        desc = pd.DataFrame(index = list(df[num_cols]))
        df = df[num_cols]
        desc['skew'] = df[num_cols].skew()
        
    desc['type'] = df.dtypes
    desc['count'] = df.count()
    desc['nunique'] = df.nunique()
    desc['%unique'] = desc['nunique'] /len(df) * 100 
    desc['null'] = df.isnull().sum()
    desc['%null'] = desc['null'] / len(df) * 100
    desc = pd.concat([desc,df.describe().T.drop('count',axis=1)],axis=1)    

    desc = desc.round(2)
    return desc.reset_index().rename(columns={'index':'Column'}).sort_values(by=['type'])


def min_max_unique(data_train, data_test):
    df = pd.DataFrame(index=data_train.columns)
    summary = {}
    
    for col in data_train.columns:
        if col in data_train and col in data_test:  # Check if column exists in both dataframes
            if pd.api.types.is_numeric_dtype(data_train[col]):  
                min_train = min(data_train[col])
                min_test = min(data_test[col])
                max_train = max(data_train[col])
                max_test = max(data_test[col])
                unique_train = len(data_train[col].unique())
                unique_test = len(data_test[col].unique())
                top5_train = sorted(data_train[col])[:5]
                top5_test = sorted(data_test[col])[:5]
            else:  
                min_train = min_test = max_train = max_test = None
                unique_train = len(data_train[col].unique())
                unique_test = len(data_test[col].unique())
                top5_train = top5_test = None  # noqa: F841
            summary[col] = [min_train, min_test, max_train, max_test, 
                            unique_train, unique_test]
        else:
            print(f"Column '{col}' not found in both data_train and data_test.")

    df = pd.DataFrame.from_dict(summary, orient='index', columns=['min_train', 'min_test', 'max_train', 'max_test', 
                                                                  'unique_train', 'unique_test'])\
        .reset_index().rename(columns={'index': 'columns'})
    return df


def Number_of_columns(df):
    NUMERIC_COLS = [f for f in df._get_numeric_data() if f not in TARGET]
    CAT_COLS = list(df.drop(NUMERIC_COLS,axis=1))
    print(f'Numerical cols: {len(NUMERIC_COLS)}')
    print(f'Categorical cols: {len(CAT_COLS)}')