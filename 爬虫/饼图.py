import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data=np.load('国民经济核算季度数据.npz')
name=data['columns']
values=data['values']

plt.figure(figsize=(8,8))#将画布设成正方形
label=['第一产业','第二产业','第三产业']
explode=[0.02,0.02,0.02]#设定各项距离圆心n个半径
plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%.1f%%')
plt.show()
