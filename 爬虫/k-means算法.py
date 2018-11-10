# import pandas as pd
# import numpy as np
# import random
# import matplotlib.pyplot as plt
#
# def k_choise(list1,list2,pos1):#取第一个分类点
#     k1 = np.array([random.randint(np.min(list1), np.max(list1)), random.randint(np.min(list2), np.max(list2))])
#     k2 = np.array([random.randint(np.min(list1), np.max(list1)), random.randint(np.min(list2), np.max(list2))])
#     k3 = np.array([random.randint(np.min(list1), np.max(list1)), random.randint(np.min(list2), np.max(list2))])
#     k = [k1, k2, k3]
#     count_k(k,pos1)
#
# def count_k(k,pos1):
#     k_list=[0,0]
#     while True:
#         k_list[0] = k_list[1]
#         index(k,pos1)
#         k_list[1]=k
#         print(k_list)
#         if check_drc(k_list):
#             print('结束')
#             break
#
#     plt.rcParams['font.sans-serif'] = 'SimHei'
#     plt.rcParams['axes.unicode_minus'] = False
#     data = pos1
#     name = data['平均每次消费金额']
#     values = data['平均消费周期（天）']
#     plt.figure()
#     x=name
#     y=values
#     x1,y1=k_list[0][0]
#     x2,y2=k_list[0][1]
#     x3,y3=k_list[0][2]
#     plt.scatter(x, y)
#     plt.scatter(x1,y1,marker='*',color='r')
#     plt.scatter(x2,y2,marker='*',color='g')
#     plt.scatter(x3,y3,marker='*',color='y')
#     plt.xlabel('平均每次消费金额')
#     plt.ylabel('平均消费周期（天）')
#     plt.show()
#
#
# def check_drc(k):
#     if np.all(k[0] == k[1]):
#         return True
#     else:
#         return False
#
# def index(k,pos1):
#     arr=np.array([])
#     k_num={}
#     k_nun={}
#     k1_arr={}
#     k2_arr={}
#     k3_arr={}
#     for i in k:
#         index = np.array(np.sqrt(np.sum((i - pos1) ** 2, axis=1)))
#         nun=0
#         for num in index:
#             k_num[num] = i
#             k_nun[num] = nun
#             nun+=1
#         arr=np.hstack((arr,index))
#     arr1=arr.reshape(3,int(len(arr)/3)).min(axis=0)
#     # print(k_num)
#     # print(k_nun)
#     for j in arr1:
#         a=k_num[j]
#         b=k_nun[j]
#         if np.all(a==k[0]):
#             k1_arr[j] = b
#         elif np.all(a==k[1]):
#             k2_arr[j] = b
#         elif np.all(a==k[2]):
#             k3_arr[j] = b
#     arrk1 = np.array([0,0])
#     for k1 in k1_arr.keys():
#         c=k1_arr[k1]
#         arrk1=arrk1+pos1.loc[c,['平均每次消费金额','平均消费周期（天）']]
#     k1_xy=np.array(arrk1/len(k1_arr.keys()))
#     arrk2 = np.array([0,0])
#     for k2 in k2_arr.keys():
#         c=k2_arr[k2]
#         arrk2=arrk2+pos1.loc[c,['平均每次消费金额','平均消费周期（天）']]
#     k2_xy=np.array(arrk2/len(k2_arr.keys()))
#     arrk3 = np.array([0,0])
#     for k3 in k3_arr.keys():
#         c=k3_arr[k3]
#         arrk3=arrk3+pos1.loc[c,['平均每次消费金额','平均消费周期（天）']]
#     k3_xy=np.array(arrk3/len(k3_arr.keys()))
#     k[0] = k1_xy
#     k[1] = k2_xy
#     k[2] = k3_xy
#     return k,
#
#
# if __name__=='__main__':
#     detail = pd.read_excel(r'C:\Users\IBM\Desktop\company.xlsx')
#     print(detail)
#     pos1 = detail.loc[:, detail.columns[1:3]]
#     # print(pos1)
#     list1 = detail['平均每次消费金额']
#     list2 = detail['平均消费周期（天）']
#     k_choise(list1,list2,pos1)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataf=pd.read_excel(r'C:\Users\IBM\Desktop\company.xlsx')

x=dataf[['平均每次消费金额','平均消费周期（天）']].as_matrix()

from sklearn.cluster import KMeans
kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)

