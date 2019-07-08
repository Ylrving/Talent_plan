#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
# from wordcloud import WordCloud
import jieba



def keywords(data):
    #统计论文关键字词频统计
    keywords = data.iloc[:,[4]]
    keywords = keywords.where(data.notnull(), "don't know keywords")
    words = {}
    words["don't know keywords"] = 0
    for index,row in keywords.iterrows():
        k = row['keywords'].split(',')
        for word in k:
            words[word] = words.get(word,0) + 1
    print("去掉所有论文中没有收集到关键字的论文数：{}".format(words["don't know keywords"]))
    words.pop("don't know keywords")
    words_list = sorted(words.items(), key=lambda item: item[1])
    print("总共出现的关键字有{}种".format(len(words_list)))
    text = ""
    pan = 0
    print("出现次数前五的关键字：")
    for word,num in words_list[::-1]:
        if text == "":
            text += word
        else:
            text += " " + word
        if pan < 5:
            print("{}:{}".format(word,num))
            pan += 1

    return text


def draw_wordcloud(text):
    # 画关键字词云图
    cut_text = jieba.cut(text)
    result = ";".join(cut_text)

    wc = WordCloud(
            background_color='white',
            width=1000,
            height=500,
            max_font_size=100,
            min_font_size=5,
            mode='RGBA'
            )
    wc.generate(result)
    # 保存图片
    wc.to_file("../data/wordcloud.png")
    # 4.显示图片
    # 指定所绘图名称
    plt.figure("jay")
    # 以图片的形式显示词云
    plt.imshow(wc)
    # 关闭图像坐标系
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    #读取数据
    data = pd.read_csv('../data/data.csv')
    #获取所有关键字
    text = keywords(data)
    #画词云图
    draw_wordcloud(text)