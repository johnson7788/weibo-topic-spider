from aip import AipNlp
import pandas as pd
import numpy as np
import time
from config import APP_ID, API_KEY, SECRET_KEY, FILE_PATH

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def isPostive(text):
    try:
        if client.sentimentClassify(text)['items'][0]['positive_prob']>0.5:
            return "积极"
        else:
            return "消极"
    except:
        return "积极"

data = pd.read_excel(FILE_PATH, encoding='utf-8')

moods = []
count = 1
for i in data['微博内容']:
    moods.append(isPostive(i))
    count+=1
    print("目前分析到："+count)

data['情感倾向'] = pd.Series(moods)

# 此处新的excel
data.to_excel('new_'+ FILE_PATH)
print("分析完成，已保存")


'''
# 此处为简单分类:P
def fenlei(text):
    xf = ['抽奖',"抽一个","抽一位","买","通贩"]
    cz = ["画","实物","返图","合集","摸鱼","漫","自制","攻略","授权","草稿","绘"]
    gj = ["hz","狗粉丝","狗女儿"]
    for j in cz:
        if j in text:
            return "创作"
    for i in xf:
        if i in text:
            return "消费"
    for k in gj:
        if k in text:
            return "攻击"
    return "其他"        
''' 
