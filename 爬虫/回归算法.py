from sklearn.datasets import load_boston
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 加载数据
boston=load_boston()

# data:表示数据
# target:标签
# 特征名称:feature_names
# 描述信息:DESCR

# 取标签
y=boston['target']
# 取特征名称
name=boston['feature_names']
#获取数据集数据
X=boston['data']
# print(name)
#
# ##########导入到.xls文件中
# #创建文件名及其路径
# outputfile=r'boston.xls'
# #将数据表和标签表两张表合并为一整个数据大表:
# df=pd.DataFrame(X,index=range(len(y)),columns=name,)
# pf=pd.DataFrame(y,index=range(len(y)),columns=['outcome'],)
# j=df.join(pf,how='outer')
# #将数据表存入文件中
# j.to_excel(outputfile)

########第一步:分割样本:0.2表示测试集在总样本中的占比
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
##第二步:构造线性回归模型:
clf=LinearRegression().fit(X_train,y_train)

##查看模型:
print('截距:',clf.intercept_)
print('回归系数:',clf.coef_)

##预测训练集结果:
y_predict=clf.predict(X_test)
#画图与原先对比
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure(figsize=(10,6))
plt.plot(range(y_test.shape[0]),y_test,color='b',linewidth=1,linestyle='-',marker='*')
plt.plot(range(y_test.shape[0]),y_predict,color='r',linewidth=1.5,linestyle='-.')
plt.legend(['真实房价','预测房价'])
plt.show()

