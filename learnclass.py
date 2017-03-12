# coding:utf-8

# 一：定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]

# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
class student:
    def __init__(self, name, age, *course):
        self.name = name
        self.age = age
        self.course = course
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.course)
zm = student('zhangming',20,[69,88,100])
lq = student('liqiang',23,[82,60,99])