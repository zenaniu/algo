"""
题目描述
疫情期间，小明隔离在家，百无聊赖，在纸上写数字玩。他发明了一种写法：

给出数字个数 n （0 < n ≤ 999）和行数 m（0 < m ≤ 999），从左上角的 1 开始，按照顺时针螺旋向内写方式，依次写出2,3,....,n，最终形成一个 m 行矩阵。

小明对这个矩阵有些要求：

每行数字的个数一样多
列的数量尽可能少
填充数字时优先填充外部
数字不够时，使用单个 * 号占位
输入描述
两个整数，空格隔开，依次表示 n、m

输出描述
符合要求的唯一矩阵

用例1
输入
9 4
输出
1 2 3
* * 4
9 * 5
8 7 6
"""
import math

n, m = map(int, input().split())
# 螺旋矩阵列数
k = int(math.ceil(n / m))
# 初始化螺旋矩阵数据
matrix = [['*'] * k for _ in range(m)]
# 当前要填入的值
step = 1
# 当前值填入的位置
x = 0
y = 0

while step <= n:
    while y < k and matrix[x][y] == '*' and step <= n:
        matrix[x][y] = str(step)
        step += 1
        y += 1
    # 向右填完后，y处于末尾越界位置，因此y需要后退一步
    y -= 1
    # x需要定位到下一行
    x += 1
    while x < m and matrix[x][y] == '*' and step <= n:
        matrix[x][y] = str(step)
        step += 1
        x += 1
    x -= 1
    y -= 1
    while y >= 0 and matrix[x][y] == '*' and step <= n:
        matrix[x][y] = str(step)
        step += 1
        y -= 1
    y += 1
    x -= 1
    while x >= 0 and matrix[x][y] == '*' and step <= n:
        matrix[x][y] = str(step)
        step += 1
        x -= 1
    x += 1
    y += 1
for i in range(m):
    print(" ".join(matrix[i]))
