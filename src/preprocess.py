# Importing the basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Style, Fore

def printInfo(df,train,test):
    print(f'{Style.BRIGHT}{Fore.YELLOW}SHAPE{Style.RESET_ALL}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {train.shape}')
    print(f'{Style.BRIGHT}{Fore.GREEN} test:  {test.shape}')
    print(f'{Style.BRIGHT}{Fore.GREEN} original:  {df.shape}')
    print(f'{Style.BRIGHT}{Fore.YELLOW}\nNULL VALUES{Style.RESET_ALL}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {train.isnull().any().any()}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {test.isnull().any().any()}')
    print(f'{Style.BRIGHT}{Fore.GREEN} original: {df.isnull().any().any()}')    
    print(f'{Style.BRIGHT}{Fore.YELLOW}\nDUPLICATES{Style.RESET_ALL}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {train.duplicated().any().any()}')
    print(f'{Style.BRIGHT}{Fore.GREEN} train: {test.duplicated().any().any()}')
    print(f'{Style.BRIGHT}{Fore.GREEN} original: {df.duplicated().any().any()}')
    
    