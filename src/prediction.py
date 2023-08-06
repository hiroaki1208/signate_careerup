import pandas as pd
import numpy as np
import os, sys

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# import lib.util_func as util_func

DATA_DIR = os.getenv('DATA_DIR')
OUTPUT_DIR = os.getenv('OUTPUT_DIR')
RANDOM_SEED = 2016
TEST_SIZE = 0.25

def _load_cleansed_data(exe_type):
    '''load cleansed data'''
    
    if exe_type == 'validation':
        path = os.path.join(DATA_DIR, 'cleansed', 'cleansed_train.csv')
    elif exe_type == 'configuration':
        path = os.path.join(DATA_DIR, 'cleansed', 'cleansed_test.csv')
    else:
        print('error')
        sys.exit(1)

    # load data
    df = pd.read_csv(path)
    return df

def _prediction(df):
    '''forecast'''

    # # Random Forest Regression
    # y_col = 'price'
    # X_col = [i for i in df.columns if i != y_col]

    # X = df[X_col].copy()
    # y = df[y_col].copy()

    # X_train, y_train, X_test, y_test = train_test_split(
    #     X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED)
    
    # clf = RandomForestRegressor(
    #     verbose=1_000,
    #     max_depth=10,
    # )
    # clf.fit(X_train, X_test)

    # # save model
    path = os.path.join(OUTPUT_DIR, 'model.sav')
    # pickle.dump(clf, open(path, 'wb'))
    # 保存したモデルをロードする
    clf = pickle.load(open(path, 'rb'))

    pred = clf.predict(df)
    sub = df[['id']].copy()
    sub['pred'] = pred
    sub.columns = np.arange(2)
    print(sub.isnull().sum().sum())

    # save submission
    path = os.path.join(OUTPUT_DIR, 'submission.csv')
    sub.to_csv(path)

def main(exe_type):

    df = _load_cleansed_data(exe_type)
    _prediction(df)
