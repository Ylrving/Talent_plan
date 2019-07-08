#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

def draw_relation(data):
    #绘制关系网络图
    author_info = data.iloc[:, [5]]
    #作者发文次数
    info_dic = {}
    for index, row in author_info.iterrows():
        info = row['author_university'].split("::")
        for index in info:
            info_dic[index] = info_dic.get(index, 0) + 1

    #排序
    info_list = sorted(info_dic.items(), key=lambda item: item[1])
    author_list = []
    pan = 0
    print("发表论文数前三作者有为：")
    for author,num in info_list[::-1]:
        if pan <3:
            author_list.append(author)
            pan += 1
            print("{:75}:{}".format(author,num))



    #有向图
    DG = nx.DiGraph()
    #创建节点对应大小列表
    node_size_list = []
    #创建已画节点列表
    nodes = []
    #创建节点颜色列表
    colors =[]
    for index, row in author_info.iterrows():
        #每篇论文的作者信息
        info = row['author_university'].split("::")
        # 判断发表论文最多的三位作者有没有参与这篇论文
        result,aut = decide(author_list,info)
        if result:
            #创建作者节点列表
            short_info_list = []
            for long_info in info:
                short_info = long_info.split("@")[0]
                short_info_list.append(short_info)
                if short_info not in nodes:
                    DG.add_node(short_info)
                    nodes.append(short_info)
                    colors.append(randomcolor())
                    node_size_list.append(info_dic[long_info]*500)

            #创建作者关系列表
            connect_list = []
            for i in short_info_list:
                    if i != aut:
                        connect_list.append((aut,i))
            DG.add_edges_from(connect_list)
    nx.draw(DG, with_labels=True, node_size=node_size_list, node_color=colors)
    plt.show()

def decide(fact_list, test_list):
    # 判断test_list是否在fact_list中
    return_result = False
    for test_author in test_list:
        if test_author in fact_list:
            return_result = True
            break
    short_author = test_author.split("@")[0]
    return return_result, short_author

def randomcolor():
    # 生成随机颜色的RGB值
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0, 14)]
    return "#" + color


if __name__ == '__main__':
    # 读取数据
    data = pd.read_csv('../data/data.csv')
    #绘制合作网络关系图
    draw_relation(data)