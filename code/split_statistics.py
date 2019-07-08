import pandas as pd

#读取数据
data = pd.read_csv("../data/data.csv")

#根据出版社将数据分开
data1=data.iloc[[x for x in range(127)], :] #出版社：ANNALS OF STATISTICS
data2=data.iloc[[x for x in range(127,174)], :]  #出版社：ROYAL
data3=data.iloc[[x for x in range(174,318)], :]  #出版社：AMERICAN
data4=data.iloc[[x for x in range(318,393)], :]  #出版社：BIOMETRIKA
data_list = [data1,data2,data3,data4]

#不同出版社关键字统计
from keywords import keywords
for i in data_list:
    keywords(i)
    print("\n")

#不同出版社作者信息统计
from author_info import authorInfo
for i in data_list:
    authorInfo(i)
    print("\n")

# 不同出版社作者网络关系
from author_relation import draw_relation
for i in data_list:
    draw_relation (i)
    print("\n")