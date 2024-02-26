"""
题目描述
小明来到某学校当老师，需要将学生按考试总分或单科分数进行排名，你能帮帮他吗？

输入描述
第 1 行输入两个整数，学生人数 n 和科目数量 m。

0 < n < 100
0 < m < 10
第 2 行输入 m 个科目名称，彼此之间用空格隔开。

科目名称只由英文字母构成，单个长度不超过10个字符。
科目的出现顺序和后续输入的学生成绩一一对应。
不会出现重复的科目名称。
第 3 行开始的 n 行，每行包含一个学生的姓名和该生 m 个科目的成绩（空格隔开）

学生不会重名。
学生姓名只由英文字母构成，长度不超过10个字符。
成绩是0~100的整数，依次对应第2行种输入的科目。
第n+2行，输入用作排名的科目名称。若科目不存在，则按总分进行排序。

输出描述
输出一行，按成绩排序后的学生名字，空格隔开。成绩相同的按照学生姓名字典顺序排序。

用例1
输入
3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 95
minmin 100 82
shuxue
输出
xiaohua fangfang minmin

"""


class Grade:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


student_nums, subject_num = map(int, input().split())
subjects = input().split()
student_grades = []
for i in range(student_nums):
    l = input().split()
    name = l[0]
    grades = list(map(int, l[1:]))
    grades.append(sum(grades))
    student_grades.append(Grade(name, grades))
k = input()
if k in subjects:
    student_grades.sort(key=lambda x: x.grades[subjects.index(k)], reverse=True)
else:
    student_grades.sort(key=lambda x: x.grades[-1], reverse=True)
print(" ".join(map(lambda x: x.name, student_grades)))
