"""

题目描述
从前有个村庄，村民们喜欢在各种田地上插上小旗子，旗子上标识了各种不同的数字。

某天集体村民决定将覆盖相同数字的最小矩阵形的土地分配给村里做出巨大贡献的村民，请问此次分配土地，做出贡献的村民种最大会分配多大面积?

输入描述
第一行输入 m 和 n，

m 代表村子的土地的长
n 代表土地的宽
第二行开始输入地图上的具体标识

输出描述
此次分配土地，做出贡献的村民种最大会分配多大面积

备注
旗子上的数字为1~500，土地边长不超过500
未插旗子的土地用0标识
用例1
输入
3 3
1 0 1
0 0 0
0 1 0
输出
9
说明
土地上的旗子为1，其坐标分别为(0,0)，(2,1)以及(0,2)，为了覆盖所有旗子，矩阵需要覆盖的横坐标为0和2，纵坐标为0和2，所以面积为9，即（2-0+1）*（2-0+1）= 9
"""
import sys


class Rect:
    def __init__(self):
        self.minRow = sys.maxsize
        self.maxRow = -sys.maxsize
        self.minCol = sys.maxsize
        self.maxCol = -sys.maxsize

    def setRow(self, row):
        self.minRow = min(self.minRow, row)
        self.maxRow = max(self.maxRow, row)

    def setCol(self, col):
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)


n, m = map(int, input().split())
rects = {}
for i in range(n):
    numbers = list(map(int, input().split()))
    for j in range(m):
        num = numbers[j]
        if num > 0:
            rects.setdefault(num, Rect())
            rects[num].setRow(i)
            rects[num].setCol(j)
maxArea = 0
for num in rects:
    rect = rects[num]
    maxArea = max(maxArea, (rect.maxCol - rect.minCol + 1) * (rect.maxRow - rect.minRow + 1))
print(maxArea)
