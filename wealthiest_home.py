"""
题目描述
在一颗树中，每个节点代表一个家庭成员，节点的数字表示其个人的财富值，一个节点及其直接相连的子节点被定义为一个小家庭。

现给你一颗树，请计算出最富裕的小家庭的财富和。

输入描述
第一行为一个数 N，表示成员总数，成员编号 1~N。1 ≤ N ≤ 1000

第二行为 N 个空格分隔的数，表示编号 1~N 的成员的财富值。0 ≤ 财富值 ≤ 1000000

接下来 N -1 行，每行两个空格分隔的整数（N1, N2），表示 N1 是 N2 的父节点。

输出描述
最富裕的小家庭的财富和

用例1
输入
4
100 200 300 500
1 2
1 3
2 4
输出
700
"""
node = int(input())
wealth = list(map(int, input().split()))
print(wealth)
node_map = dict()
for i in range(node - 1):
    node_parent, node_child = map(int, input().split())
    if node_parent not in node_map:

        node_map[node_parent] = {node_parent, node_child}
    else:
        node_map[node_parent].add(node_child)
max_wealth = 0
for nodes in node_map.values():
    if sum(wealth[i - 1] for i in nodes) > max_wealth:
        max_wealth = sum(wealth[i - 1] for i in nodes)
print(max_wealth)
