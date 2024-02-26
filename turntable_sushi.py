"""
题目描述
寿司店周年庆，正在举办优惠活动回馈新老客户。

寿司转盘上总共有 n 盘寿司，prices[i] 是第 i 盘寿司的价格，

如果客户选择了第 i 盘寿司，寿司店免费赠送客户距离第 i 盘寿司最近的下一盘寿司 j，前提是 prices[j] < prices[i]，如果没有满足条件的 j，则不赠送寿司。

每个价格的寿司都可无限供应。

输入描述
输入的每一个数字代表每盘寿司的价格，每盘寿司的价格之间使用空格分隔，例如:

3 15 6 14

表示：

第 0 盘寿司价格 prices[0] 为 3
第 1 盘寿司价格 prices[1] 为 15
第 2 盘寿司价格 prices[2] 为 6
第 3 盘寿司价格 prices[3] 为 14
寿司的盘数 n 范围为：1 ≤ n ≤ 500

每盘寿司的价格 price 范围为：1 ≤ price ≤ 1000

输出描述
输出享受优惠后的一组数据，每个值表示客户选择第 i 盘寿司时实际得到的寿司的总价格。使用空格进行分隔，例如：

3 21 9 17

用例1
输入
3 15 6 14
输出
3 21 9 17
"""
# 输入获取
prices = list(map(int, input().split()))


# 算法入口
def getResult():
    res = []
    res.extend(prices)

    # 单调栈，单调递增，存储prices下标
    stack = []
    n = len(prices)
    for j in range(n * 2):
        price = prices[j % n]
        while len(stack) > 0:
            i = stack[-1]
            if price < prices[i]:
                stack.pop()
                res[i] += price
            else:
                break
        # 第一轮循环加入栈内对比,第二轮不加入
        if j < n:
            stack.append(j)
    return res


# 算法调用
print(" ".join(map(str, getResult())))
