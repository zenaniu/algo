"""
题目描述
机器人搬砖，一共有 N 堆砖存放在 N 个不同的仓库中，第 i 堆砖中有 bricks[i] 块砖头，要求在 8 小时内搬完。

机器人每小时能搬砖的数量取决于有多少能量格，机器人一个小时中只能在一个仓库中搬砖，机器人的能量格只在这一个小时有效，为使得机器人损耗最小化，应尽量减小每次补充的能量格数。

为了保障在 8 小时内能完成搬砖任务，请计算每小时给机器人充能的最小能量格数。

无需考虑机器人补充能力格的耗时；
无需考虑机器人搬砖的耗时；
机器人每小时补充能量格只在这一个小时中有效；
输入描述
第一行为一行数字，空格分隔

输出描述
机器人每小时最少需要充的能量格，若无法完成任务，输出 -1

用例1
输入
30 12 25 8 19
输出
15
"""
import math

bricks = list(map(int, input().split()))


def check(energy, limit):
    days = 0
    for i in bricks:
        days += math.ceil(i / energy)
        if days > limit:
            return False
    return True

def getResult():
    n = len(bricks)

    if n > 8:
        return -1

    max_bricks = max(bricks)
    if n == 8:
        return max_bricks

    ans = max_bricks
    min_bricks = 1
    while min_bricks < max_bricks:
        mid_bricks = (min_bricks + max_bricks) >> 1
        if check(mid_bricks, 8):
            ans = mid_bricks
            max_bricks = mid_bricks - 1
        else:
            min_bricks = mid_bricks + 1
    return ans
