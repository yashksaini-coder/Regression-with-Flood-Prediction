import pandas as pd

def load_train():
    train = pd.read_csv('./data/train.csv')
    return train

def load_test():
    test = pd.read_csv('./data/test.csv')
    return test

def load_original():
    original = pd.read_csv('./data/origianl.csv')
    return original

def load_submission():
    submission = pd.read_csv('./data/sample_submission.csv')
    return submission