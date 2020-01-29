2020/1/29 已修复爬取错误，测试正常，更新武汉肺炎超话爬取数据，愿武汉一切安好。
# weibo-topic-spyder
微博超级话题爬虫，微博词频统计+情感分析+简单分类

### 使用方法
在weibo-topic-spyder.py的主函数中输入账号、密码和想要爬取的超话名称即可开始爬取，需要提前安装所需的python库和chromedriver驱动

爬取结束后数据会自动保存在当前目录下的excel文件中，每行为一个微博数据。

### 超级话题爬虫

使用了selenium模拟浏览器登陆进行爬取，具体话题爬取数量受微博限制，目前单个话题最大获取微博数量为8000条左右，选择了使用手机网页模式爬取，以获得最佳的爬取效果。

账号与IP数量对单个超话的爬取帮助不大，就只设置了单账号和ip模式，若需多超话同时爬取可以自行添加。

如需爬取多个超话，可以选择使用cookie登陆，最为方便

### 词频统计
使用了jieba库进行分词，最后对分词结果进行简单统计并且存储到txt中

### 情感分析 
调用了百度大脑的api接口，可以自行注册获取key，平台不限调用次数，详细接口见[百度大脑](https://ai.baidu.com/tech/nlp_apply/sentiment_classify) 


爬取数据展示
![](img/fy.png)
![](img/weibo.png)

词频统计展示

![](img/seg.png)

如有其他问题，欢迎提交issue
