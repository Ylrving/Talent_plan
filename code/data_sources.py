#coding:utf-8
import pandas as pd
import  matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('../data/data.csv')

#获取数据第二列
publisher = data.iloc[:,[1]]

#数据统计
publisher_dic = {}
for index,row in publisher.iterrows():
    publisher_dic[row['publisher']] = publisher_dic.get(row['publisher'],0) + 1
for key,num in publisher_dic.items():
    print("{}:{}".format(key,num))

#设置绘图变量
labels = ['BIOMETRIKA','ANNALS OF STATISTICS','AMERICAN','ROYAL']
# labels=['生物统计杂志','统计年鉴','美国统计学会杂志','英国统计学会杂志']
values = [75,127,144,47]
explode=[0,0.1,0]

# 绘制扇形图
plt.pie(values,labels = labels,
        startangle = 180,
        shadow=True,autopct='%1.1f%%')
plt.axis('equal')
plt.show()

#直方图
# plt.rcParams['font.sans-serif'] = ['SimHei']#正常显示中文
# plt.rcParams['axes.unicode_minus'] = False#正常显示负号
# rects = plt.bar(labels,values)
# plt.ylabel('论文数量/(篇)')
# plt.xlabel('所属杂志')
# for rect in rects:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
# plt.show()

#网页直方图
# from pyecharts import Bar
# bar =Bar("")
# bar.add("论文分布", labels, values)
# bar.show_config()
# bar.render()

