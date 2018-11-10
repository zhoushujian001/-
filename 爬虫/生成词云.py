from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
##背景图
backgroup=plt.imread(r'C:\Users\IBM\Desktop\timg.jpg')
##读生成词云的文档
f=open('bili.txt','r',encoding='utf-8').read()

wordcloud=WordCloud(
    # background_color='white',##设置背景颜色,默认黑色
    mask=backgroup,##背景图
    font_path=r'C:\Windows\Fonts\simfang.ttf',##字体路径
    width=1000,
    height=100,
    margin=2,#####3边缘宽度

).generate(f)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()