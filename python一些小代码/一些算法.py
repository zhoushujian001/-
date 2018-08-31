import time
# 选择排序
# def findsmallest(arr):
# 	smellest=arr[0]
# 	smellest_index=0
# 	for i in range(1,len(arr)):
# 		if arr[i]<smellest:
# 			smellest=arr[i]
# 			smellest_index=i
# 	return smellest_index
# def sel(arr):
# 	newarr=[]
# 	for i in range(len(arr)):
# 		smallest=findsmallest(arr)
# 		newarr.append(arr.pop(smallest))
# 	return newarr
# print(sel([5,10,20,6,8]))
# 冒泡排序
# def bubble_sort(alist):
#     for j in range(len(alist)-1,0,-1):
#         # j表示每次遍历需要比较的次数，是逐渐减小的
#         for i in range(j):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
# li = [54,26,93,17,77,31,44,55,20]
# bubble_sort(li)
# print(li)
# 鸡尾酒排序
a=[13,67,432,6865,342,3,4,5,21]
def cocktail_sort(l):
    size = len(l)
    sign = 1
    for i in range(int(size/2)):
        if sign:
            sign = 0
            for j in range(i, size - 1 - i):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
            for k in range(size - 2 - i, i, -1):
                if l[k] < l[k - 1]:
                    l[k], l[k - 1] = l[k - 1], l[k]
                    sign = 1
        else:
            break
cocktail_sort(a)
print(a)
# # 快速排序
# def quicksort(array):
# 	if len(array)<2:
# 		return array
# 	else:
# 		pivot=array[0]
# 		less=[i for i in array[1:] if i<=pivot]
# 		greater=[i for i in array[1:] if i>pivot]
# 		print(array)
# 		print(less)
# 		print(greater)
# 		return quicksort(less)+[pivot]+quicksort(greater)
# print(quicksort([10,222,46,77,32,3]))
#二分法
# def bin(list,item):
#     low=0
#     high=len(list)-1
#     while high>=low:
#         mid=(high+low)//2
#         guess=list[mid]
#         if guess==item:
#             return mid
#         if guess>item:
#             high = mid - 1
#         else:
#             low = mid + 1
# list=[1,2,3,4,5,6,7,8,9]
# print(bin(list,8))
# 汉诺塔
# def move(n, a, b, c):
#     if n == 1:  # 如果a只有1盘子
#         print(a, '-->', c);  # 直接把盘子从a移到c
#     else:  # 如果a有n个盘子(n > 1)，那么分三步
#         move(n - 1, a, c, b)  # 先把上面n-1个盘子，借助c，从a移到b
#         move(1, a, b, c)  # 再把最下面的1个盘子，借助b，从a移到c
#         move(n - 1, b, a, c)  # 最后把n-1个盘子，借助a，从b移到c
# move(4, 'A', 'B', 'C')  # 测试
# 约舍夫环
# def monkey(n,m):
#     l=[]
#     i = 0
#     for j in range(1,n+1):
#         l.append(j)
#     while len(l)>1:
#         k=l.pop(0)
#         i += 1
#         if i%m!=0:
#             l.append(k)
#         if len(l)==m-1:
#             return k
# print(monkey(16,3))
# start_time=time.time()
# for a in range(0,1001):
#     for b in range(0, 1001):
#         c=1000-a-b
#         if a+b+c==1000 and a**2+b**2==c**2:
#             print(a,b,c)
# end_time=time.time()
# print('time:%d'%(end_time-start_time))
# print('结束')
# start_time=time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         if 2000*(a+b) - 2*a*b == 1000**2:
#             print(a,b,1000-a-b)
# end_time=time.time()
# print('time:%d'%(end_time-start_time))
# print('结束')
# for a in range(1, a_range):
#     b_high =b_range
#     b_low = a + 1
#     while True:
#         b = (b_low + b_high) // 2
#         c = 1000000 - a - b
#         if a ** 2 + b ** 2 == c ** 2:
#             print("a=%d, b=%d, c=%d" % (a, b, c))
#             break
#         elif a ** 2 + b ** 2 > c ** 2:
#             b_high = b
#         elif a ** 2 + b ** 2 < c ** 2:
#             b_low = b + 1
#         if b_low == b_high :
#             break
# end_time=time.time()
# print('time:%d'%(end_time-start_time))
# print('结束')



