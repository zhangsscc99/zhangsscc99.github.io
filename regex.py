import re

text = """第一个20题 平均一天一道题
1，4，15，70
485，495，414，628（这排都是数组）
374(二分） （这里都是二分），34，94(中序遍历），455（greedy algorithm）
135(greedy algorithm)（hard题但也不是很hard，容易错而已），88 merge sorted array（指针），141,142（至少现在有一个方式找到）
独立做出：10道题

第二个20题
76（滑动窗口，太难了）,69（x的平方根，二分，居合斩）,34,24(linked list; swap nodes)
81, 64（动态规划），234(很简单的回文）328(odd even linked list)
704（居合斩）,145后序，前序，中序
101 symmetric Tree（dfs),4(复习了一下；可以把复习也当作是新的一道题 只要覆盖完了）,637(bfs), 226(有dfs也有bfs，也有recursively）
独立做出：8道（提高了这20题的难度）

第三个20题
172(数学题，尾数0的个数）,1791(graph题目），1971(graph， path是否存在）,7(reverse integer, 用了个有点复杂的做法）
46(backtracking), 77(backtracking)，435（greedy），83(链表)
104(树的最大深度）,208字典树, 565 关于图的（array nesting）,21 sorted list（循环和双指针，还有递归方法）
20（valid parentheses，这题得用栈，就是灵活地去用一些栈的属性）, 无序数组（循环加二分或者双指针方法），有序数组（两层循环，或者hashmap法），字符串相加（415）
226(翻转二叉树），160 相交链表，876（middle of the linked list），剑指offer 22（第k个节点，美国站没有）"""
numbers = re.findall(r'\d+', text)
numbers=[int(i) for i in numbers]
numbers=sorted(numbers)
print(numbers)
#lst=[]
#for i in range(len(numbers)):
#    lst.append(str(numbers[i]))


#print(' '.join(sorted(lst)))
lst=[1,2,2,1]
lst.reverse()
print(lst)
print(lst)

