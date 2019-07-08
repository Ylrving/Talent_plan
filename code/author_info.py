#coding:utf-8
import pandas as pd

def authorInfo(data):
    #作者信息统计
    author_info = data.iloc[:,[5]]
    info_dic = {}
    for index,row in author_info.iterrows():
        info = row['author_university'].split("::")
        for index in info:
            info_dic[index] = info_dic.get(index,0) + 1
    #所有作者信息列表
    info_list = sorted(info_dic.items(), key=lambda item: item[1])

    # print(info_list[::-1])
    print("总共有{}名作者的论文发表".format(len(info_list)))
    #作者和机构信息
    au = {}
    uni = {}
    for author in info_dic.keys():
        au_info = author.split("@")
        au[au_info[0]] = au.get(au_info[0],0) + 1
        for university in au_info[1:]:
            uni[university] = uni.get(university,0) + 1
    uni.pop("Unknow")
    uni_list = sorted(uni.items(), key=lambda item: item[1])
    print("不同名字的作者有{}，他们分别来自{}所机构".format(len(au),len(uni)))
    print("参与度最高的五个机构：")
    pan = 0
    for university,num in uni_list[::-1]:
        if pan <5:
            print("{:60} {:}".format(university,num))
            pan += 1

if __name__ == '__main__':
    #读取数据
    data = pd.read_csv('../data/data.csv')
    #作者信息统计
    authorInfo(data)