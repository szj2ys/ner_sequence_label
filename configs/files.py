# *_*coding:utf-8 *_*
'''
Descri：
'''

try:
    from .dirs import *
except:
    from configs.dirs import *

# 错误日志文件
LOGS_ERRORS = join(LOGS, "errors.log")

# 日志文件
LOGS = join(LOGS, "everythings.log")
