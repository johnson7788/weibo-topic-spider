from aip import AipNlp
import pandas as pd
import numpy as np
import time, os
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
for i in data['微博内容']:
    mood = isPostive(i)
    moods.append(mood)
    print(f'微博内容:{i}, 情感是: {mood}')

data['情感倾向'] = pd.Series(moods)

# 此处新的excel
new_path = os.path.join(os.path.dirname(FILE_PATH), 'result_' + os.path.basename(FILE_PATH))
data.to_excel(new_path)
print("分析完成，已保存")