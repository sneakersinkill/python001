# !/usr/bin/env python3
'''this is BMW M760i
xDrive搭载顺畅动力的双涡轮增压6.6升V12发动机，功率为601马力，
扭矩为590磅英尺'''
print("this is BMW M760i 双涡轮增压6.6升V12发动机，601马力")
m = 5

def damage(skill1, skill2):
    damage_skill1 = skill1 * 3
    damage_skill2 = skill2 * 3 + 10
    return damage_skill1, damage_skill2

#序列解包
a , b = damage(4, 6)   #用a,b两个变量去接收返回值  设定函数参数
print(a, b)            #输出返回值


#序列解包与链式赋值
a = 1
b = 2
c = 3

a, b, c = 1, 2, 3

d = 1, 2, 3
print(type(d))

a, b, c = d
print(a, b, c)