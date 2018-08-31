#空心三角
num=int(input('输入你需要几行'))
for i in range(1,num+1):
    if i==1:
        for j in range(1,num+1-i):
            print(' ',end='')
        print('*',end='')
    elif i==num:
        for k in range(1,num+1):
            print('* ',end='')
    else:
        for j in range(1,num+1-i):
            print(' ',end='')
        print('*',end='')
        for k in range(1,i*2-2):
            print(' ',end='')
        print('*',end='')
    print()
def hsj():
    for i in range(1,8):
        for j in range(1,(7-i + 1)):
            print(' ',end='')
        for j in range(1,2*i-1+ 1):
            if j==1 or j==2*i-1 or i==7:
                print('*',end='')
            else:
                print(' ',end='')
        print()
hsj()

#a=[1,3,5,7] b=[11,22,33,44,55,66] c=[1,11,3,22,5,33,7,44,55,66]
# a=[1,3,5,7]
# b=[11,22,33,44,55,66]
# c=[]
# for i in range(0,len(b)):
#     if i<len(a):
#         c.append(a[i])
#         c.append(b[i])
#     else:
#         c.append(b[i])
# print(c)

#字典的增删改查
# s={'001':{'姓名':'张三','年龄':18,'籍贯':'北京'},
#     '002':{'姓名':'李四','年龄':18,'籍贯':'山东'},
#     '003':{'姓名':'王五','年龄':18,'籍贯':'河北'},
#     '004':{'姓名':'赵六','年龄':18,'籍贯':'北京'}}
# while True:
#     x=input('欢迎使用学生管理系统\n增加学生请输入a,修改学生资料请输入b\n删除学生资料请输入c，退出程序请输入d')
#     if x=='a':
#         a1=input('请输入你要增加的学生的学号')
#         a2=input('请输入你要增加的学生的姓名')
#         a3= input('请输入你要增加的学生的年龄')
#         a4= input('请输入你要增加的学生的籍贯')
#         s[a1]={'姓名':a2,'年龄':a3,'籍贯':a4}
#         print('已添加成功',s)
#     elif x=='b':
#         b1 = input('请输入你要修改的学生的学号')
#         print('该同学信息为：',s[b1])
#         b2=input('请问要修改学生什么信息？')
#         b3=input('请问要修改为？')
#         s[b1][b2]=b3
#         print('已修改成功', s)
#     elif x=='c':
#         c1=input('请输入你要删除的学生学号')
#         del s[c1]
#         print('已删除成功', s)
#     else:
#         break