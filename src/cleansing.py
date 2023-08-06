import pandas as pd
import os, sys

# import lib.util_func as util_func

DATA_DIR = os.getenv('DATA_DIR')
# OUTPUT_DIR = os.getenv('OUTPUT_DIR')

def _load_data(exe_type):
    '''load data'''
    
    if exe_type == 'validation':
        path = os.path.join(DATA_DIR, 'input', 'train.csv')
    elif exe_type == 'configuration':
        path = os.path.join(DATA_DIR, 'input', 'test.csv')
    else:
        print('error')
        sys.exit(1)

    # load data
    df = pd.read_csv(path)
    return df

def _fill_nan(df):
    '''fill na'''

    # 中央値で補間
    df = df.fillna( df.mode().iloc[0] )
    return df

def _one_hot_encoding(df):
    '''One Hot Encoding'''
    adds = []
    for c in df.columns:
        if df[c].dtype == 'object':
            add = pd.get_dummies(df[c])
            add.columns = [f'{c}_{i}' for i in add.columns]
        else:
            add = df[[c]]

        adds.append(add)
    return pd.concat(adds, axis=1)

def _save_data(exe_type, df):
    '''save cleansed data'''

    if exe_type == 'validation':
        fname = 'cleansed_train.csv'
    elif exe_type == 'configuration':
        fname = 'cleansed_test.csv'
    else:
        print('error')
        sys.exit(1)

    data_dir = os.path.join(DATA_DIR, 'cleansed')
    output_path = os.path.join( os.path.join(data_dir, fname) )
    df.to_csv(output_path, index=False)

def main(exe_type):

    df = _load_data(exe_type)
    df = _fill_nan(df)
    df = _one_hot_encoding(df)
    _save_data(exe_type, df)
