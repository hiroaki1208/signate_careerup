#! /bin/bash

BASE_DIR=$(dirname ${0})
cd ${BASE_DIR}

# defaultパラメータ設定
EXE_TYPE='validation'
# SUBFOLDER=$(date '+%Y%m%d%H%M')

# パラメータのパース
while getopts e: OPT; do
    case ${OPT} in
        e) EXE_TYPE=${OPTARG} ;;
        *) usage ;;
    esac
done

source ${BASE_DIR}/configs/config.sh
set -euC
# conda activate env2

# python ${BASE_DIR}/run.py -s ${SUBFOLDER} -p ${PARAM}
python ${BASE_DIR}/main.py -e ${EXE_TYPE}