import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False

red_wine=pd.read_csv(r'C:\Users\IBM\Desktop\winequality.csv',sep=';')
# print(red_wine)
x=np.array(red_wine.columns[:-1])
X=red_wine[x]
# print(X)
y=red_wine.columns[-1]
y=red_wine[y]
index=np.array(red_wine['quality']).argsort()
lab=np.mean(red_wine.loc[index[:-100:-1],('fixed acidity',"volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol")],axis=0)
# print(red_wine.loc[index[-100:-1]])
lab=np.around(lab, decimals=2)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1)
clf=LinearRegression().fit(X_train,y_train)
# print('回归系数:',clf.coef_)
y_predict=clf.predict(X_test)

fig=plt.figure(figsize=(10,10))
fig.add_subplot(2,2,1)
plt.plot(range(y_test.shape[0]),y_test,color='b',linewidth=1,linestyle='-',marker='*')
plt.plot(range(y_test.shape[0]),y_predict,color='r',linewidth=1.5,linestyle='-.')
plt.legend(['真实评分','预测评分'])
plt.title('真实红酒评分与预测红酒评分对比')
plt.xlabel('样本数量')
plt.ylabel('评分')
fig.add_subplot(2,2,2)
plt.plot(range(y_test.shape[0]),(y_test-y_predict))
plt.legend('差值')
plt.title('真实红酒评分与预测红酒差值起伏')
fig.add_subplot(2,2,3)
label=['固定酸度','挥发性酸','柠檬酸','糖分','氯化物','自由二氧化硫','总二氧化硫','密度','酸碱平衡度','硫酸盐','酒精含量']
explode=[0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]
plt.pie(abs(clf.coef_),labels=label,explode=explode,autopct='%.1f%%')
plt.title('红酒成分占比重要性比较')
fig.add_subplot(2,2,4)
plt.bar(range(11),lab)
label=['固定酸度','挥发性酸','柠檬酸','剩余糖分','氯化物','自由二氧化硫','总二氧化硫','密度','酸碱平衡度','硫酸盐','酒精含量']
plt.xlabel('名称')
plt.ylabel('回归系数')
plt.title('红酒成分含量推荐')
plt.xticks(range(11),label,rotation=65)
for x,y in zip(range(11),lab):
    plt.text(x,y,y,ha='center',fontsize=10)
plt.savefig('绘图.png')
plt.show()