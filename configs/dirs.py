# *_*coding:utf-8 *_*
'''
Descri：
'''
from os.path import dirname, abspath, join

# 获取项目根目录
ROOT = dirname(dirname(abspath(__file__)))

# 数据文件存放路径
DATASETS = join(ROOT, "datasets")

# 结果文件路径
RESULTS = join(DATASETS, "results")

# log文件路径
LOGS = join(DATASETS, "logs")
