import pandas as pd 
import numpy as np
import os
import shutil
import math

'''
基于TF-IDF的关键词提取
'''
def readtxt(path):
    with open(path, 'r') as f:#, encoding = 'utf-8'
        content = f.read().strip()
    f.close()
    return content
# 统计词频
def word_count(content):
    word_dict = {}
    word_list = content.strip().split(' ')
    for word in word_list:
        del_word = ["\r\n","/s"," ","/n"]
        if word not in del_word:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    return word_dict

def funfolder(path):
    filesArray = []
    for root,dirs,files in os.walk(path):
        for file in files:
            each_file = str(root+"//"+file)
            filesArray.append(each_file)
    return filesArray

# 计算tf-idf
def count_tfidf(word_dict, words_dict, files_Array):
    word_idf = {}
    word_tfidf = {}
    num_files = len(files_Array)
    for word in word_dict:
        for words in words_dict:
            if word in words:
                if word in word_idf:
                    word_idf[word] += 1
                else:
                    word_idf[word] = 1
    for key,value in word_dict.items():
        if key != ' ':
            word_tfidf[key] = value * math.log(num_files/(word_idf[key]+1))
            
    values_list = sorted(word_tfidf.items(),key = lambda item:item[1],reverse=True)  
    return values_list

#新建文件夹
def buildfolder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    print("成功创建文件夹！")
    
# 写入文件
def out_file(path,content_list):
    with open(path,"a",encoding="utf-8") as f:
        for content in content_list:
            f.write(str(content[0]) + ":" + str(content[1])+"\r\n")
    f.close()
    print("well done!")

# 语料的清洗、生成、及分词
def text_process(path, stop_word_path):#初始语料的文件位置
    texts_path = funfolder(path)
    stopwords = [w.strip() for w in open(stop_word_path, 'r',encoding='utf-8-sig') if w.strip().strip('\n')]
    for path in texts_path:
        content = readtxt(path)
        document_cut = [w.strip() for w in jieba.cut(content) if w.strip() not in stopwords ]
        result = ' '.join(document_cut)
        with open(path, 'w') as f2:
            f2.write(result)
        f2.close()

# 语料库的生成
def files_text(path):
    # path 为文件夹的路径
    files_array = funfolder(path)
    files_dict = []
    for file_path in files_array:
        file = readtxt(file_path)
        word_dict = word_count(file)
        files_dict.append(word_dict)
    return files_dict, files_array

# 计算tf-idf 存入txt
def files_tfidf(newfolder, path, stopword_path):
    text_process(path, stopword_path)
    files_dict, files_array = files_text(path)
    buildfolder(newfolder)
    i = 0
    for file in files_dict:
        tf_idf = count_tfidf(file, files_dict, files_array)
        files_path = files_array[i].split("//")
        #print(files_path)
        outfile_name = files_path[1]
        #print(outfile_name)
        out_path = r"%s//%s_tfidf.txt"%(newfolder,outfile_name)
        out_file(out_path,tf_idf) 
        i += 1

if __name__ == '__main__':
    # 提供各文件路径
    files_tfidf(newfolder, path, stopword_path)