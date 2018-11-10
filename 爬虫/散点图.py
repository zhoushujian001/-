import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data=np.load('国民经济核算季度数据.npz')
name=data['columns']
values=data['values']

# plt.figure()
# # scatter散点图
# x=values[:,0]
# y=values[:,3]
# y1=values[:,4]
# y2=values[:,5]
# plt.scatter(x,y,marker='o',color='r')
# plt.scatter(x,y1,marker='o',color='b')
# plt.scatter(x,y2,marker='o',color='y')
# plt.xlabel('季度')
# plt.ylabel('生产总值(亿元)')
# plt.title('2000-2017年各季度各产业生产总值散点图')
# plt.legend(['第一产业','第二产业','第三产业'])
# # xticks给定需要放刻度名称的位置,名称,rotation倾斜度
# plt.xticks(values[::4,0],values[::4,1],rotation=65)
# plt.show()

plt.figure(figsize=(16,9),dpi=100)
x=values[::4,0]
y=values[::4,9]
y1=values[::4,8]

plt.scatter(x,y,color='r')
plt.scatter(x,y1,color='b')
plt.xlabel('季度')
plt.ylabel('生产总值(亿元)')
plt.title('2000-2017年各季度批与发业建筑业对比图')
plt.legend(['批发业','建筑业'])
# xticks给定需要放刻度名称的位置,名称,rotation倾斜度
plt.xticks(values[::4,0],values[::4,1],rotation=15)
plt.show()