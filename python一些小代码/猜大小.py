import random
print('欢迎参加猜大小游戏，现在我有三个色子\n每个骰子最大六点，随机生成三个骰子数\n三个骰子数之和大于9为大，否则为小\n现在你有100金币，猜中金币数+10，猜错金币数-10 金币为0时结束游戏')
money = 100
while True:
    a=input('请你猜一猜，现在3个骰子摇出的数是大还是小(退出请输入退出)')
    b1= random.randint(1, 6)
    b2 = random.randint(1, 6)
    b3 = random.randint(1, 6)
    b4=b1+b2+b3
    if a=='大':
        if b4>9:
            money+=10
            print('恭喜你猜对，骰子数是%d ，大，您现在金币数为：%d'%(b4,money))
        else:
            money -= 10
            print('很遗憾你猜错了，骰子%d 点，小，您现在金币数为：%d' % (b4, money))
    elif a=='小':
        if b4 <= 9:
            money += 10
            print('恭喜你猜对，骰子数是%d ，小，您现在金币数为：%d' % (b4, money))
        else:
            money -= 10
            print('很遗憾你猜错了，骰子%d 点，大，您现在金币数为：%d' % (b4, money))
    else:
        break