"""
题目描述
某个产品当前迭代周期内有 N 个特性（F1,F2,......FN）需要进行覆盖测试，每个特性都被评估了对应的优先级，特性使用其 ID 作为下标进行标识。
设计了 M 个测试用例（T1,T2,......,TM），每个测试用例对应一个覆盖特性的集合，测试用例使用其 ID 作为下标进行标识，测试用例的优先级定义为其覆盖的特性的优先级之和。
在开展测试之前，需要制定测试用例的执行顺序，规则为：优先级大的用例先执行，如果存在优先级相同的用例，用例 ID 小的先执行。
输入描述
第一行输入为 N 和 M，
N 表示特性的数量，0 < N ≤ 100
M 表示测试用例的数量，0 < M ≤ 100
之后 N 行表示特性 ID=1 到特性 ID=N 的优先级，
再接下来 M 行表示测试用例 ID=1 到测试用例 ID=M 关联的特性的 ID 的列表。
输出描述
按照执行顺序（优先级从大到小）输出测试用例的 ID，每行一个ID。
测试用例覆盖的 ID 不重复。


用例
输入：
5 4
1
1
2
3
5
1 2 3
1 4
3 4 5
2 3 4
输出
3
4
1
2
测试用例的优先级计算如下:
T1 =Pf1 + Pf2 + Pf3= 1+1+2=4
T2=Pf1 + Pf4=1 +3=4
说明
T3= Pf3+ Pf4+Pf5=2+3+5= 10
T4=Pf2 + Pf3+ Pf4=1 +2+3=6
按照优先级从小到大，以及相同优先级，ID小的先执行
的规则，执行顺序为T3,T4,T1,T2

题目解读：一个用例对应多个特性，每个特性都有优先级，按照优先级从高到底输出用例下标
"""

n, m = map(int, input().split())
features = [0] * n
for i in range(n):
    features[i] = int(input())
cases = []
for i in range(m):
    priority = sum(features[int(x) - 1] for x in input().split())
    cases.append([priority, i])
cases.sort(key=lambda x: (x[0], x[1]))
print(cases)
for _, idx in cases:
    print(idx)
