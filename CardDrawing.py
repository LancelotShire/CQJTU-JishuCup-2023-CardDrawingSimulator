import random
import sys
def CardDrawing():
    stars=[3,4,5,6]
    six_stars_1=['假日威龙陈','缄默德克萨斯','能天使','玛恩纳','鸿雪','号角','伊内斯','焰影苇草','史尔特尔','麒麟X夜刀','凯尔希','百炼加维尔','耀骑士临光','菲亚梅塔','令','浊心斯卡蒂','灵知','艾雅法拉','澄闪','温蒂','仇白','风笛','缪尔塞斯','夜莺','铃兰']
    six_stars_2=['伺夜','斥罪','林','异客','棘刺','Ash','黑键','泥岩','山','艾丽妮','琴柳','白铁']
    five_stars_1=['羽毛笔','海沫','拉普兰德','巫恋','寒芒克洛丝','火哨','白面鸮','巫恋','风丸','华法琳']
    five_stars_2=['白金','埃拉托','崖心','食铁兽','乌有','晓歌','极境']
    weight_of_six_stars_1=0.4
    weight_of_six_stars_2=0.2
    weight_of_five_stars_1=0.3
    weight_of_five_stars_2=0.1
    i=random.randint(1,8)
    r=random.choices(stars,[weight_of_six_stars_1,weight_of_six_stars_2,weight_of_five_stars_1,weight_of_five_stars_2],k=i)
    c=0
    d=0
    e=0
    f=0
    for j in range (0,i):
        if r[j]==3:
            c=c+1
        elif r[j]==4:
            d=d+1
        elif r[j]==5:
            e=e+1
        else:
            f=f+1
    result_of_six_stars_1=random.sample(six_stars_1,k=c)
    result_of_six_stars_2=random.sample(six_stars_2,k=d)
    result_of_five_stars_1=random.sample(five_stars_1,k=e)
    result_of_five_stars_2=random.sample(five_stars_2,k=f)
    print('被ban掉的人物:\n')
    for j in range (0,c):
        print(result_of_six_stars_1[j],'\n')
    for j in range (0,d):
        print(result_of_six_stars_2[j],'\n')
    for j in range (0,e):
        print(result_of_five_stars_1[j],'\n')
    for j in range (0,f):
        print(result_of_five_stars_2[j],'\n')

    team=[1,2]
    team_1=['心胜于物','物尽其用','以人为本','破坏战术分队','指挥分队','突击战术分队']
    team_2=['集群分队','后勤分队','矛头分队','堡垒战术分队','远程战术分队','研究分队','高规格分队']
    weight_of_team_1=0.6
    weight_of_team_2=0.4
    m=random.randint(1,4)
    n=random.choices(team,[weight_of_team_1,weight_of_team_2],k=m)
    x=0
    y=0
    for j in range (0,m):
        if n[j]==1:
            x=x+1
        else:
            y=y+1
    result_of_team_1=random.sample(team_1,k=x)
    result_of_team_2=random.sample(team_2,k=y)
    print('被ban掉的队伍:\n')
    for j in range (0,x):
        print(result_of_team_1[j],'\n')
    for j in range (0,y):
        print(result_of_team_2[j],'\n')
    ask = input("Restart? Press enter to restart the program.\nIf you want to exit, input n and then press enter.").lower()
    if ask == "":
        CardDrawing()
    if ask == "n":
        sys.exit()

CardDrawing() 
