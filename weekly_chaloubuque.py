# 1 阿里面试题查漏补缺笔记 

#

# 1通配符匹配
# 2  146可以了解原生写法
# 3 队列实现栈一个栈比较熟悉，两个栈写法巩固一下
# 4 合并二叉树，多做点二叉树题目熟悉一下 bfs可以巩固强化一下 多找几道好题做
#  5 括号生成 回溯暴力解法
# 6 合并有序链表可以拓展一下力扣23 hard写法
# 7 


# 多ak几遍3道题
# if i - open < open 要注意的
'''
22 生成括号这里很难
237 思路迥异  
子序列一般不是动态规划就是滑动窗口
152 绝对是难题 还是很有难度的  
279 做错就想 初始化 递推公式 递推条件  确认状态 容量 物品
93 多做几道回溯题 强化一下 
88 这些都是好题目 值得反复做 
44 星号匹配不确定 s的前i个字符 p的前j个字符 
顺便做一下第十题 


146插入的时候不需要makeRecent

疯狂重复看错题本 3-5分钟 每个下课
一周上百遍的重复 重复刷题 看题 100遍 一周
60 70 85+ 就不做了
歼灭战
45套卷里记得要做思维导图和分析 解析 顺便找类似题进行延展训练 联系新题 测试解题能力（刷题从属于学习方法）




17 18题专门刷就行了 然后 压轴题做个四五遍 也不一定能够做全对 不强求
语文和英语甚至需要老师评判 作文 而计算机貌似不需要

45套卷 刷5遍 45套面经 就可以达成大量重复  


从早到晚 12套文综卷 估计就是12h。 
估计可以做10套面经。10场周赛。

'''

'''
OOD Design Reservation system(Restaurant)
考虑what，how，

1Clarifications:
1lobby 2 paid 3no capacity limit 4all tables are the same 5no reservation
6 no takeout
2Core Objects: Restaurant, Table, Order, Meal, Party

Use Cases 
Restaurant: find table, take order, clear table, checkout

3Classes: 
Restaurant
-List<Table> tables, -List<Meal> menu, -Map<Table, List<Order> orders>
+Table findTable()
+void takeOrder(Order o)
+void checkout(Order o)

Table -bool available
+bool isAvailable()
+void markUnavailable()
+void markAvailable()

Order
-List<Meal> meals
-Table+
-PartyP
+float getPrice()
Meal -float price +float getPrice()
NoTable Available Exception

4Reservation System
Search Criteria-> Search-> List<Result> - Select() Receipt
# of people
date
time 

List<Result> - 1list of available datetime or 2confirm/throw exception





'''

'''

'''



