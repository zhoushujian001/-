import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data=np.load('国民经济核算季度数据.npz')
name=data['columns']
values=data['values']

plt.figure()
plt.bar(range(3),values[-1,3:6])
label=['第一产业','第二产业','第三产业']
plt.xlabel('产业')
plt.ylabel('生产产值(亿元)')
plt.title('2017年第一季度各产业国民生产总值直方图')
plt.xticks(range(3),label)

for x,y in zip(range(3),values[-1,3:6]):
    plt.text(x,y,y,ha='center',fontsize=10)

plt.show()