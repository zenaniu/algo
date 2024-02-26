"""
题目描述
某学校举行运动会，学生们按编号(1、2、3…n)进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列；对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。

输入描述
两个序列，每个序列由n个正整数组成（0 < n <= 100）。第一个序列中的数值代表身高，第二个序列中的数值代表体重。

输出描述
排列结果，每个数值都是原始序列中的学生编号，编号从1开始

用例1
输入
5
100 100 120 130 120
40 30 60 50 60
输出
2 1 3 4
说明
输出的第一个数字2表示此人原始编号为2，即身高为100，体重为30的这个人。
由于他和编号为1的人身高一样，但体重更轻，因此要排在1前面。
"""
result = []
num_peoples = int(input())
height = input().split()
weight = input().split()
for i in range(num_peoples):
    result.append([i + 1, height[i], weight[i]])
result.sort(key=lambda x: (x[1], x[2], x[0]))
for i in result:
    print(i[0], end=' ')
