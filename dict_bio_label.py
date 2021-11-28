# -*- coding: utf-8 -*-
'''
基于外部词典对数据进行标注  BIO方式
'''
from os.path import join
from configs.dirs import DATASETS, RESULTS

WORD_DICT_FILE = join(DATASETS, 'word_dict.txt')
UNLABELED_FILE = join(DATASETS, 'unlabel.txt')
ERROR_FILE = join(RESULTS, 'error.txt')
LABELED_FILE = join(RESULTS, 'labeled.txt')

features_list = []
with open(WORD_DICT_FILE, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        features_list.append(line.strip().split(' ')[0])
        #print(features_list[0])
'''
创建特征词列表、特征词+tag字典（特征词作为key，tag作为value）
'''

#将features_dict中的特征词和tag存入字典  特征词为key，tag为value
dict = {}
with open(WORD_DICT_FILE, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        item = line.split(' ')
        #print(item)
        if len(item) > 1:
            dict[item[0]] = item[1]
        else:
            with open(ERROR_FILE, 'a', encoding='utf-8') as f:
                f.write(line + "\n")
'''
根据字典中的word和tag进行自动标注，用字典中的key作为关键词去未标注的文本中匹配，匹配到之后即标注上value中的tag
'''

index_log = 0
with open(UNLABELED_FILE, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
        word_list = list(line.strip())
        tag_list = ["O" for i in range(len(word_list))]

        for keyword in features_list:
            print(keyword)
            while 1:
                index_start_tag = line.find(keyword, index_log)
                #当前关键词查找不到就将index_log=0,跳出循环进入下一个关键词
                if index_start_tag == -1:
                    index_log = 0
                    break
                index_log = index_start_tag + 1
                print(keyword, ":", index_start_tag)
                #只对未标注过的数据进行标注，防止出现嵌套标注
                for i in range(index_start_tag,
                               index_start_tag + len(keyword)):
                    if index_start_tag == i:
                        if tag_list[i] == 'O':
                            tag_list[i] = "B-" + dict[keyword].replace(
                                "\n", '')  # 首字
                    else:
                        if tag_list[i] == 'O':
                            tag_list[i] = "I-" + dict[keyword].replace(
                                "\n", '')  # 非首字

        with open(LABELED_FILE, 'a', encoding='utf-8') as output_f:
            for w, t in zip(word_list, tag_list):
                print(w + " " + t)
                if w != '	' and w != ' ':
                    output_f.write(w + " " + t + '\n')
                    #output_f.write(w + " "+t)
            output_f.write('\n')
