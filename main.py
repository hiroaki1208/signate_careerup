import pandas as pd
import numpy as np

import os, sys, yaml
import argparse
import logging.config

import lib.util_func as util_func
# import models.create_covisit
import src.cleansing as cleansing
import src.model as model

DATA_DIR = os.getenv('DATA_DIR')
OUTPUT_DIR = os.getenv('OUTPUT_DIR')
CONFIG_DIR = os.getenv('CONFIG_DIR')
LOG_DIR = os.getenv('LOG_DIR')

# def create_result_config(result_dir, args):
#     '''計算設定を保存
#     '''

#     result_path = os.path.join(result_dir, 'result_config.yaml')
#     with open(result_path, 'w') as rp:
#         yaml.dump(vars(args), rp, default_flow_style=False)

# def _load_config_file(fname):
#     '''parameter設定ファイルを読み込み
#     '''
#     logging.info(f'start loading parameter configuration')
#     with open(os.path.join(CONFIG_DIR, 'parameter', f'{fname}.yml'), encoding='utf-8') as file:
#         config = yaml.safe_load(file.read())      
#     logging.info(f'end loading parameter configuration')

#     return config

def main():

    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__))
    )
    util_func.print_log(f'start: {base_dir}')    

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--execution_type', default='validation', choices=['validation', 'configuration'])
    # parser.add_argument('-p', '--param_idx', default='param0'
    #                     , help= 'parameter index', type=str
    #                     )
    args = parser.parse_args()
    util_func.print_log(f'execution_type: {args.execution_type}')    

    # # parameter設定yml読み込み
    # param = _load_config_file(args.param_idx)
    # param_config['type_label'] = TYPE_LABEL

    try:
        # logging.basicConfig(level=logging.INFO)   
        # logging.config.fileConfig(os.path.join(base_dir, 'logs', 'logging.ini')
        #                           , defaults={'logdir': LOG_DIR})
        
        # # 計算設定保存
        # result_config_dir = os.path.join(OUTPUT_DIR, 'result', args.subfolder)
        # os.mkdir(result_config_dir)
        # create_result_config(result_config_dir, args)

        # logging.info(f'start: {base_dir}')
        # logging.info(f'(param)target: {args.target}')
        # logging.info(f'(param)is_partial: {args.is_partial}')
        # logging.info(f'(param)covisitation setting: {args.covisit}')

        # cleansing
        cleansing.main(args.execution_type)

        # create model or prediction
        if args.execution_type == 'validateion':
            model.main(args.execution_type)


        util_func.print_log(f'end: {base_dir}')    
    except Exception as e:
        # logging.exception(e)
        util_func.print_log(e)
        sys.exit(1)

if __name__ == '__main__':
    # print('Hello')
    main()

