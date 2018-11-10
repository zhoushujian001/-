import pandas as pd
import numpy as np
movie=pd.read_excel(r'G:\Day3——分类算法—kNN算法+决策树算法（CLS算法）\KNN算法及程序\电影分类数据.xlsx')
print(movie.columns)

# # 取出需要预测的名字，坐标
pos2=np.array(movie.columns[-3:])
print(pos2)

##取出训练集样本坐标
pos1=movie.loc[:,movie.columns[2:5]]
#
# ##KNN算法：K==5
index=np.array(np.sqrt(np.sum((pos1-pos2)**2,axis=1))).argsort()
print(index)
labels=movie.loc[index[:5],'电影类型']
#

print(labels.mode()[0])








