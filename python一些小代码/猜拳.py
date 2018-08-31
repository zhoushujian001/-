import random
while True:
    num = int(input('欢迎参加 剪刀，石头，布 猜拳游戏\n您的对手已准备，剪刀输入1，石头输入2，布输入3\n请问您要出什么（退出请输入4）'))
    if num in [1,2,3]:
        answer=random.randint(1,3)
        if num==answer:
            print('两边猜的一样呢，真遗憾，对方出的是%d'%answer)
        elif (num==3 and answer==2) or (num==2 and answer==1) or(num==1 and answer==3):
            print('真厉害，您赢了这一局，对方出的是%d'%answer)
        else:
            print('sorry，您输了，下次再继续努力，对方出的是%d'%answer)
    elif num==4:
        break
    else:
        print('输入错误，只能输入1234哟')