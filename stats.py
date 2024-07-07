import matplotlib.pyplot as plt
from collections import Counter

# 示例数据列表
def count_freq(data):

    
    # 统计各数字出现的次数
    counter = Counter(data)

    # 提取标签和相应的计数值
    labels = counter.keys()
    counts = counter.values()

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Number Frequency in List')
    plt.show()

data_dasiming = [4,1,6,2,4,4,5,6,10,11,4,5,3,2,10,2,3,4,6,2,10,3,1,4,1,11,6,5,10,4,11,1,10,1,10,1,1,10,11,27,10,7]
count_freq(data_dasiming)

# 大司命 一局下来主要是 反野（23） 刷野（23）， 打团（17），（带线吃线20） 推塔（10） 开龙（5）围绕反野 带线 推塔 开龙
# 

data_xiahoudun = [2,3,4,4,5,10,5,10,2,5,4,4,10,3,1,10,4,5,2,4,4,10,7,
            10,1,2,3,2,10,7,4,1,1,3,3,2,11,1,7,4,1,4,11,6,7,4,7,10]
count_freq(data_xiahoudun)

# 夏侯惇 一局下来主要是 反野（17） 刷野（17）， 打团（19），（带线吃线23） 推塔（5）开龙（10） 蹲人（10）围绕反野 带线 推塔 开龙

