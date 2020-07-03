import turtle as t
import random
import time

#시작 화면
def KeysetMenu():    
    bg2=t.Screen()
    bg2.bgpic("keyset.gif")

    userfire.st()
    useraqua.st()
    userstorm.st()

    userfire.goto(-200,-300)
    useraqua.goto(0,-300)
    userstorm.goto(200,-300)
    
#오른쪽으로 움직이기
def moving_go():
    if user.shape()=="uf.gif":
        user.shape("uf2.gif")
    if user.shape()=="ua.gif":
        user.shape("ua2.gif")
    if user.shape()=="us.gif":
        user.shape("us2.gif")
    user.seth(0)
    user.forward(30)
    
#왼쪽으로 움직이기    
def moving_back():
    if user.shape()=="uf2.gif":
        user.shape("uf.gif")
    if user.shape()=="ua2.gif":
        user.shape("ua.gif")
    if user.shape()=="us2.gif":
        user.shape("us.gif")
    user.seth(180)
    user.forward(30)
    
#위로 움직이기    
def moving_up():
    user.seth(90)
    user.forward(30)
    
#아래로 움직이기
def moving_down():
    user.seth(270)
    user.forward(30)

    
#게임시작
def GameStart():
    userfire.ht()
    useraqua.ht()
    userstorm.ht()
    
    HP.up()
    point.up()
    HP.goto(-300,300)
    point.goto(300,300)
    backgroundtime = time.time()
    bg3=t.Screen()
    HP1=10
    
    point1=0
    
    user.goto(200,-200)
    king.goto(0,-123)    
    king.st()    

    KFset1=0
    KFset2=0 
    KF1C=0
    KF2C=0
    KF3C=0

    KAset=0
    KA1C=0
    KA2C=0

    KSset=0
    KS2C=0
    KS3C=0
    KS1C=0
    
    soul_spawnX=random.randint(-350,350)
    soul_spawnY=random.randint(-350,350)
    soul.goto(soul_spawnX,soul_spawnY)
    soul.st()

    KSskill1_2.goto(800,0)
    KFskill2.goto(800,0)
    KAskill1_2.goto(800,0)
    KAskill2_2.goto(800,0)
    KSskill2_2.goto(800,0)
    KSskill1_2.goto(800,0)

    #체력, 점수
    point.color("green")
    point.clear()
    point.write(point1, False, "center", ("", 70))
    HP.color("black")
    HP.clear()
    HP.write(HP1, False, "center", ("", 70))  

    while True:
        
        #게임 클리어
        if point1 >= 15:
            gameclear1.st()
            time.sleep(2)
            gameclear1.shape("gameclear.gif")
            time.sleep(2)
            gameclear1.ht()
            gameclear2.st()
            break
        
        #게임 오버
        if HP1 <= 0:
            bg4 = t.Screen()
            bg4.bgpic("gameover.gif")
            king.ht()
            user.ht()
            soul.ht()
            break
            
        
        
        #위치값
        #유저 위치값
        UX=user.xcor()
        UY=user.ycor()

        #불기둥 위치값
        KF1_2X=KFskill1_2.xcor()
        KF1_2Y=KFskill1_2.ycor()
        #불공 위치값
        KF2X=KFskill2.xcor()
        KF2Y=KFskill2.ycor()
        
        #물공 위치값
        KA1_2X=KAskill1_2.xcor()
        KA1_2Y=KAskill1_2.ycor()
        #파도 위치값
        KA2_2X=KAskill2_2.xcor()
        KA2_2Y=KAskill2_2.ycor()
        
        #번개 위치값        
        KS1_2X=KSskill1_2.xcor()
        KS1_2Y=KSskill1_2.ycor()
        #사자 위치값
        KS2_2X=KSskill2_1.xcor()
        KS2_2Y=KSskill2_2.ycor()

        #소울 위치값
        soulX=soul.xcor()
        soulY=soul.ycor()

        #닿는 거리
        KF1=user.distance(KF1_2X,KF1_2Y)
        KF2=user.distance(KF2X,KF2Y)

        KA1=user.distance(KA1_2X,KA1_2Y)
        KA2=user.distance(KA2_2X,KA2_2Y)

        KS1=user.distance(KS1_2X,KS1_2Y)
        KS2=user.distance(KS2_2X,KS2_2Y)

        soulD=user.distance(soulX,soulY)

        HP.ht()
        point.ht()

        #닿았을 때
        if soulD<=50:            
            point1=point1+1            
            point.color("green")
            point.clear()
            point.write(point1, False, "center", ("", 70))           
            soul.ht()
            soul_spawnX=random.randint(-350,350)
            soul_spawnY=random.randint(-350,350)
            soul.goto(soul_spawnX,soul_spawnY)
            soul.st()
        if KF1<=85:
            HP1=HP1-1
            HP.color("black")
            HP.clear()
            HP.write(HP1, False, "center", ("", 70))            
        if KF2<=85:
            HP1=HP1-1
            HP.color("black")
            HP.clear()
            HP.write(HP1, False, "center", ("", 70))            
        if KA1<=85:
            HP1=HP1-1
            HP.color("black")
            HP.clear()
            HP.write(HP1, False, "center", ("", 70))            
        if KA2<=85:
            HP1=HP1-1
            HP.color("black")
            HP.clear()
            HP.write(HP1, False, "center", ("", 70))            
        if KS1<=85:
            HP1=HP1-1
            HP.color("black")            
            HP.write(HP1, False, "center", ("", 70))            
        if KS2<=85:
            HP1=HP1-1
            HP.color("black")
            HP.clear()
            HP.write(HP1, False, "center", ("", 70))            
        if HP1<=0:
            user.ht()
            king.ht()
            break
        
        KFset1=KFset1+1
        #패턴      
        #불 패턴
        if KFset1==1:
            user.shape("uf.gif")
            king.shape("kf.gif")
            bg3.bgpic("background.gif")
            soul.shape("soul_fire.gif")
            KFset2=KFset2+1
            
        if KFset2==1:
            KFset1=KFset1+1
            spawnX1=random.randint(-300,300)
            spawnY1=random.randint(-300,300)
            KFskill1_1.goto(spawnX1,spawnY1)
            KFskill1_2.goto(spawnX1,spawnY1)
            KFskill1_1.st()
            time.sleep(2)
            KFskill1_1.ht()
            KFskill1_2.st()
            time.sleep(0.5)
            KFskill1_2.ht()
            KSskill1_2.goto(800,0)
    
            KF1C=KF1C+1

        if KF1C==5:
            KFset2=KFset2+1
            spawnY2=random.randint(-300,300)                
            KFskill2.goto(-500,spawnY2)
            KFskill2.st()            

            KF2C=KF2C+1
            KF1C=KF1C+1
                        
        if KF2C==1:
            KFskill2.forward(10)

            KF3C=KF3C+1                
        if KF3C==100:
            KF2C=KF2C+1
            KFskill2.ht()
            KFskill2.goto(800,0)
                
            bg3.bgpic("background3.gif")
            user.shape("ua.gif")
            king.shape("ka.gif")
            soul.shape("soul_aqua.gif")

            
            KAset=KAset+1
        if KAset==1:
            KF3C=KF3C+1
            spawnX1=random.randint(-300,300)
            spawnY1=random.randint(-300,300)
            KAskill1_1.goto(spawnX1,spawnY1)
            KAskill1_2.goto(spawnX1,spawnY1)
            KAskill1_1.st()
            time.sleep(3)
            KAskill1_1.ht()
            KAskill1_2.st()
            time.sleep(0.5)
            KAskill1_2.ht()
            KAskill1_2.goto(800,0)
            
            
            KA1C=KA1C+1
    
        if KA1C==5:
            KAset=KAset+1
            spawnY2=random.randint(-300,300)                
            KAskill2_1.goto(0,spawnY2)
            KAskill2_2.goto(0,spawnY2)            
            KAskill2_1.st()
            time.sleep(2)
            KAskill2_1.ht()
            KAskill2_2.st()
            time.sleep(0.5)
            KAskill2_2.ht()
            KAskill2_2.goto(800,0)
            
            
            KA2C=KA2C+1

        if KA2C==3:
            KA1C=KA1C+1
            bg3.bgpic("background2.gif")
            user.shape("us.gif")
            king.shape("ks.gif")
            soul.shape("soul_storm.gif")

            
            KSset=KSset+1
    
        if KSset==1:
            KA2C=KA2C+1
            spawnX5=random.randint(-300,300)
            spawnY5=random.randint(-400,400)
            KSskill2_1.goto(spawnX5,0)
            KSskill2_2.goto(spawnX5,0)
            KSskill2_1.st()
            time.sleep(1)
            KSskill2_1.ht()
            KSskill2_2.st()
            time.sleep(0.5)
            KSskill2_2.ht()
            KSskill2_2.goto(800,0)

            
            KS2C=KS2C+1

        if KS2C==5:
            KSset=KSset+1
            spawn10=random.randint(-100,100)
            KSskill1_1.goto(-500,spawn10)
            KSskill1_2.goto(-500,spawn10)
            KSskill1_1.st()
            time.sleep(1.5)
            KSskill1_1.ht()
            KSskill1_2.st()
            
            
            KS3C=KS3C+1

        if KS3C==1:
            KS2C=KS2C+1
            KSskill1_2.forward(20)
            
                                           
            KS1C=KS1C+1
            
        if KS1C==100:
            KS3C=KS3C+1 
            KSskill1_2.ht()
            KSskill1_2.goto(800,0)            
            
            KFset1=0
            KFset2=0
            KF1C=0
            KF2C=0
            KF3C=0

            KAset=0
            KA1C=0
            KA2C=0

            KSset=0
            KS2C=0
            KS3C=0
            KS1C=0
            
        
        

        
        
                                                        
        

            
user=t.Turtle()
user.up()

    
#불 장애물
t.addshape("kf.gif")
t.addshape("KFskill1_1.gif")
t.addshape("KFskill1_2.gif")
t.addshape("KFskill2.gif")

king=t.Turtle()    
king.shape("kf.gif")
king.up()
king.ht()

KFskill1_1=t.Turtle()
KFskill1_1.shape("KFskill1_1.gif")    
KFskill1_2=t.Turtle()
KFskill1_2.shape("KFskill1_2.gif")
KFskill1_1.up()
KFskill1_2.up()
KFskill1_1.ht()
KFskill1_2.ht()

KFskill2=t.Turtle()
KFskill2.shape("KFskill2.gif")
KFskill2.up()
KFskill2.ht()

#물 장애물
t.addshape("ka.gif")
t.addshape("KAskill1_1.gif")
t.addshape("KAskill1_2.gif")
t.addshape("KAskill2_1.gif")
t.addshape("KAskill2_2.gif")   

KAskill1_1=t.Turtle()
KAskill1_1.shape("KAskill1_1.gif")    
KAskill1_2=t.Turtle()
KAskill1_2.shape("KAskill1_2.gif")
KAskill1_1.up()
KAskill1_2.up()
KAskill1_1.ht()
KAskill1_2.ht()

KAskill2_1=t.Turtle()
KAskill2_1.shape("KAskill2_1.gif")    
KAskill2_2=t.Turtle()
KAskill2_2.shape("KAskill2_2.gif")
KAskill2_1.up()
KAskill2_2.up()
KAskill2_1.ht()
KAskill2_2.ht()

#번개 장애물
t.addshape("ks.gif")
t.addshape("KSskill1_1.gif")
t.addshape("KSskill1_2.gif")
t.addshape("KSskill2_1.gif")
t.addshape("KSskill2_2.gif")

KSskill1_1=t.Turtle()
KSskill1_1.shape("KSskill1_1.gif")    
KSskill1_2=t.Turtle()
KSskill1_2.shape("KSskill1_2.gif")
KSskill1_1.up()
KSskill1_2.up()
KSskill1_1.ht()
KSskill1_2.ht()

KSskill2_1=t.Turtle()
KSskill2_1.shape("KSskill2_1.gif")    
KSskill2_2=t.Turtle()
KSskill2_2.shape("KSskill2_2.gif")
KSskill2_1.up()
KSskill2_2.up()
KSskill2_1.ht()
KSskill2_2.ht()

#소울
t.addshape("soul_fire.gif")
t.addshape("soul_aqua.gif")
t.addshape("soul_storm.gif")

soul=t.Turtle()
soul.up()
soul.ht()

#점수, 체력
HP=t.Turtle()
point=t.Turtle()


#게임 시작 화면
t.addshape("uf.gif")
t.addshape("uf2.gif")

userfire=t.Turtle()
userfire.shape("uf.gif")
userfire.up()
userfire.ht()

t.addshape("ua.gif")
t.addshape("ua2.gif")

useraqua=t.Turtle()
useraqua.shape("ua.gif")
useraqua.up()
useraqua.ht()
    
t.addshape("us.gif")
t.addshape("us2.gif")

userstorm=t.Turtle()
userstorm.shape("us.gif")
userstorm.up()
userstorm.ht()

#게임 클리어
t.addshape("gameclear2.gif")
t.addshape("gameclear.gif")
t.addshape("gameclear1.gif")

gameclear1 = t.Turtle()
gameclear1.shape("gameclear2.gif")
gameclear1.ht()
gameclear1.up()
gameclear1.goto(160, 160)

gameclear2 = t.Turtle()
gameclear2.shape("gameclear1.gif")
gameclear2.up()
gameclear2.ht()
gameclear2.goto(0, 50)


#키셋
bg1=t.Screen()
bg1.bgpic("StartMenu.gif")

t.onkeypress(KeysetMenu, "space")
t.onkeypress(GameStart, "p")
t.onkeypress(moving_go, "Right")
t.onkeypress(moving_back, "Left")
t.onkeypress(moving_up, "Up")
t.onkeypress(moving_down, "Down")
t.listen()
