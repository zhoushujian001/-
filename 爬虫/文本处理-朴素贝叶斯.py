 #-*- coding:utf-8 -*-
from numpy import *

# 文本数据集
def loadDataList():
    postingList = [
        ['my','dog','has','flea','problems','help','please'],
        ['maybe','not','take','him','to','dog','park','stupid'],
        ['my','dalmation','is','so','cute','I','love','him'],
        ['stop','posting','stupid','worthless','garbage'],
        ['mr','licks','ate','my','steak','how','to','stop','him'],
        ['quit','buying','worthless','dog','food','stupid']]

    classVec = [0,1,0,1,0,1]
    #print(postingList ,classVec)
    return postingList,classVec

 # 提取训练集中的所有词,这里利用集合的性质对数据集提取不同的单词，函数 createVocabList() 返回值是列表类型
def createVocabList(dataSet): ##dataSet 为 postingList
    vocabSet = set([])
    for document in dataSet :
        vocabSet = vocabSet | set(document)  # 两个集合的并集
    return list(vocabSet)

# 根据类别对词进行划分数值型的类别；此处可以理解为在检验某一个词汇是否存在于样本词汇库中
### 因为单词的字符串类型无法参与到数值的计算，因此把一个对象的数据由词汇集中的哪些单词组成表示成：0 该对象没有这个词，1 该对象有这个词。
### 参数 vocabList 是词汇集，inputSet 是对象的数据，而返回值是由词汇集的转换成 0 和 1 组成的对象单词在词汇集的标记
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)##returnVec为生成与词汇列表维度相一致的列表
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1 ##将该词所对应returnVec位置的数置1
            #print(returnVec)
        else:
            print("the word : %s is not in my Vocabulary!" % word)
    return returnVec

# 文档词袋模型，可以对重复的单词计数
##此处若inputSet为listOposts列表中的列表元素，则returnVec表示所有样本集中含有词汇所对应出现的频率
def bagOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)##生成与词汇列表维度相一致的列表
    for word in inputSet:
        if word in vocabList:
           returnVec[vocabList.index(word)] += 1
    return returnVec

'''
求贝叶斯公式中的先验概率 pAbusive ,条件概率 p0Vect、p1Vect；函数中所求的概率值
是变形值，不影响贝叶斯的核心思想：选择具有最高概率的决策
'''
#sum(trainCategory)为总的分类数（要分为几类）
#float(numTrainDocs)样本的个数，样本中文本的个数
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)  # 样本中对象的个数
    numWords = len(trainMatrix[0]) # 样本中所有词的集合个数
    pAbusive = sum(trainCategory) / float(numTrainDocs) # 对类别只有两种的先验概率计算,每种类别的出现的先验概率做平均分配0.5

    # 对所有词在不同的类别下出现次数的初始化为1，为了防止计算条件概率出现为0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    # 对不同类别出现次数的初始化为2，词的出现数初始数为1的情况下，增加分母值避免概率值大于1
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):  # 遍历所有对象
        if trainCategory[i] == 1: # 类别类型的判断
            p1Num += trainMatrix[i]  # 对所有词在不同的类别下出现次数的计算
            p1Denom += sum(trainMatrix[i]) # 对不同类别出现次数的计算
        else:
            p0Num += trainMatrix[i] # 对所有词在不同的类别下出现次数的计算
            p0Denom += sum(trainMatrix[i]) # 对不同类别出现次数的计算
    p1Vect = log(p1Num / p1Denom)  # 条件概率,用对数的形式计算是为避免概率值太小造成下溢出
    p0Vect = log(p0Num / p0Denom)   # 条件概率,用对数的形式计算是为避免概率值太小造成下溢出
    #print('p0Vect',p0Vect,'p1Vect',p1Vect,'pAbusive',pAbusive)
    return p0Vect,p1Vect,pAbusive

# 计算后验概率，并选择最高概率作为预测类别
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec ) + log(pClass1) # 对未知对象的单词的每一项的条件概率相加（对数相加为条件概率的相乘）
    p0 = sum(vec2Classify * p0Vec ) + log(1.0-pClass1 ) # 后面加上的一项是先验概率
    if p1 > p0:
        return 1
    else:
        return 0

 # 对侮辱性语言的测试
#def testingNB():
listOposts, listClasses = loadDataList() # 训练样本的数据，listOposts 为样本，listClasses 为样本的类别
myVocabList = createVocabList(listOposts ) # 样本的词汇集
trainMat = [] # 对样本的所有对象相关的单词转化为数值
for postinDoc in listOposts:
    trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
print('trainMat',trainMat)
p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))## 样本的先验概率和条件概率


testEntry = ['love','my','dalmation','love'] # 未知类别的对象
thisDoc = array(setOfWords2Vec(myVocabList,testEntry))##对未知对象的单词转化为数值
#print('thisDoc',thisDoc)
print(testEntry ,'classified as :',classifyNB(thisDoc, p0V,p1V,pAb) )# 对未知对象的预测其类别

testEntry = ['stupid','garbage'] # 未知类别的对象
thisDoc = array(setOfWords2Vec(myVocabList,testEntry )) # 对未知对象的单词转化为数值
print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))# 对未知对象的预测其类别

