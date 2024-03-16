
##Revision App

import pygame,sys,random,math,csv
from pygame.locals import*
import colorsys
pygame.init()

infoObject=pygame.display.Info()
screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption("Reynoldson's Revision Program")
iconIMG=pygame.image.load("icon1.png").convert_alpha()
pygame.display.set_icon(iconIMG)
clock=pygame.time.Clock()



font1= pygame.font.Font('freesansbold.ttf', 15)##font
bigfont= pygame.font.Font('freesansbold.ttf', 100)##font
midfont= pygame.font.Font('freesansbold.ttf', 50)##font

def collide(checkx,checky,x,y,w,h):
    if checkx>x and checkx<x+w and checky>y and checky<y+h:
        return True
    else:
        return False


def checkWords():
    list1=[]
    list2=[]
    with open("words.csv","r") as file:
        reader=csv.reader(file)
        for i in reader:
            if i!=[]:
                list1.append(i[0])
                list2.append(i[1])
        return list1,list2

def updateFile():
    with open("words.csv","w",newline="") as file:
        writer=csv.writer(file)
        for i in range(len(questionList)):
            writer.writerow((questionList[i],answerList[i]))

        file.close()



    
def showAllWords():
    text1=font1.render("All Questions/ Definitions",True,(0,0,0))
    screen.blit(text1,(450,20))

    
    pygame.draw.rect(screen,(255,255,255),(80,45,500,800),0)
    pygame.draw.rect(screen,(255,255,255),(595,45,500,800),0)
    
    yPos=50
    count=0
    for i in questionList:
        qText=font1.render(i,True,(0,0,0))
        screen.blit(qText,(90,yPos))
        if collide(mousex,mousey,80,yPos,400,qText.get_height()):
            pygame.draw.rect(screen,(0,0,0),(85,yPos-1,1000,15),2)
            if clicked==True:
                questionList.pop(count)
                answerList.pop(count)
        yPos+=15
        count+=1
        
    yPos=50
    for i in answerList:
        aText=font1.render(i,True,(0,0,0))
        screen.blit(aText,(600,yPos))
        yPos+=15

def addWords():
    global currentNew,questionList,answerList,newQ,newA
    pygame.draw.rect(screen,(255,255,255),(1150,45,400,20),0)
    pygame.draw.rect(screen,(255,255,255),(1150,75,400,20),0)
    textQ=font1.render(newQ,True,(0,0,0))
    textA=font1.render(newA,True,(0,0,0))
    screen.blit(textQ,(1152,47))
    screen.blit(textA,(1152,77))


    
    if collide(mousex,mousey,1150,45,200,20) and clicked==True:
        currentNew="newQ" 
    elif collide(mousex,mousey,1150,75,400,20) and clicked==True:
        currentNew="newA"
        
    if currentNew=="newQ":
        pygame.draw.rect(screen,(0,0,0),(1150,45,400,20),2)
    elif currentNew=="newA":
        pygame.draw.rect(screen,(0,0,0),(1150,75,400,20),2)
        

    pygame.draw.rect(screen,(200,200,200),(1150,105,50,20),0)
    text1=font1.render("Add",True,(0,0,0))
    screen.blit(text1,(1155,108))
    if collide(mousex,mousey,1150,105,50,20):
        pygame.draw.rect(screen,(0,0,0),(1150,105,50,20),2)
        if clicked==True:
            questionList.append(newQ)
            answerList.append(newA)
            newQ=""
            newA=""

def exitButton():
    pygame.draw.rect(screen,(200,200,200),(1300,200,100,50))
    text1=font1.render("Exit",True,(0,0,0))
    screen.blit(text1,(1330,218))
    if collide(mousex,mousey,1300,200,100,50):
        pygame.draw.rect(screen,(0,0,0),(1300,200,100,50),4)
        if clicked==True:
            updateFile()
            pygame.quit()
            sys.exit()
            
def colourButton():
    global colour
    pygame.draw.rect(screen,(200,200,200),(1300,260,100,50))
    text1=font1.render("Colour",True,(0,0,0))
    screen.blit(text1,(1325,278))
    if collide(mousex,mousey,1300,260,100,50):
        pygame.draw.rect(screen,(0,0,0),(1300,260,100,50),4)
        if clicked==True:
            colour=(random.randint(0,255),random.randint(0,255),random.randint(0,255))


fullscreen=False
def screenButton():
    global screen,fullscreen
    pygame.draw.rect(screen,(200,200,200),(1450,260,100,50))
    text1=font1.render("Fullscreen",True,(0,0,0))
    screen.blit(text1,(1460,278))
    if collide(mousex,mousey,1450,260,100,50):
        pygame.draw.rect(screen,(0,0,0),(1450,260,100,50),4)
        if clicked==True:
            if fullscreen==False:
                screen=pygame.display.set_mode((1600,900),FULLSCREEN)
                fullscreen=True
            else:
                screen=pygame.display.set_mode((1600,900))
                fullscreen=False
            
helpText=[
          
        font1.render("Revision Program",True,(0,0,0)),
        font1.render("1. Enter questions/words in the top box",True,(0,0,0)),
        font1.render("2. Enter answers/definitions in the bottom box",True,(0,0,0)),
        font1.render("3. Click Add to add question to save file",True,(0,0,0)),
        font1.render("4. Click item in left column to delete",True,(0,0,0)),
        font1.render("-----------------------------------------------------",True,(0,0,0)),
        font1.render("Quiz: Go though each question and type exact answer",True,(0,0,0)),
        font1.render("Pairs: Click corresponding text to get rid of them",True,(0,0,0))
        ]

def showInfo():
    yPos=400
    for i in helpText:
        screen.blit(i,(1150,yPos))
        yPos+=30
            
def playButton():
    global menu,currentQuestion,clicked,attempts,score,currentAnswer,showAnswer,askedList,pairs,pairList,selected,selectText
    pygame.draw.rect(screen,(200,200,200),(1150,200,100,50))
    text1=font1.render("Quiz",True,(0,0,0))
    screen.blit(text1,(1180,218))

    pygame.draw.rect(screen,(200,200,200),(1150,260,100,50))
    text1=font1.render("Pair",True,(0,0,0))
    screen.blit(text1,(1180,278))
    
    if collide(mousex,mousey,1150,260,100,50):
        pygame.draw.rect(screen,(0,0,0),(1150,260,100,50),4)
        if clicked==True:
            pairs=True
            menu=False
            clicked=False
            pairList=[]
            selected=""
            selectText=""
    
    if collide(mousex,mousey,1150,200,100,50):
        pygame.draw.rect(screen,(0,0,0),(1150,200,100,50),4)
        if clicked==True:
            menu=False
            currentQuestion=random.randint(0,len(questionList)-1)
            clicked=False
            score=0
            attempts=0
            currentAnswer=""
            showAnswer=False
            askedList=[]

            
def showQuestion():
    global currentQuestion

    pygame.draw.rect(screen,(255,255,255),(50,50,1500,400))
    pygame.draw.rect(screen,(255,255,255),(50,500,1500,100))
    
    qText=bigfont.render(questionList[currentQuestion],True,(0,0,0))
    if qText.get_width()>1400:
        qText=midfont.render(questionList[currentQuestion],True,(0,0,0))
    screen.blit(qText,(100,200))
    
    aText=midfont.render(currentAnswer,True,(0,0,0))
    screen.blit(aText,(60,520))

    pygame.draw.rect(screen,(0,0,0),(60+aText.get_width(),520,2,50))

    scoreText=bigfont.render(str(score)+"/"+str(attempts),True,(0,0,0))
    screen.blit(scoreText,(100,800))

def menuButton():
    global menu,clicked,endScreen,pairs
    ##Menu Button
    pygame.draw.rect(screen,(200,200,200),(1350,750,200,100))
    subText=midfont.render("Menu",True,(0,0,0))
    screen.blit(subText,(1380,770))
    if collide(mousex,mousey,1350,750,200,100):
        pygame.draw.rect(screen,(0,0,0),(1350,750,200,100),4)
        if clicked==True:
            menu=True
            clicked=False
            endScreen=False
            pairs=False

def submit():
    global showAnswer,clicked,score,attempts
    pygame.draw.rect(screen,(200,200,200),(700,750,200,100))
    subText=midfont.render("Sumbit",True,(0,0,0))
    screen.blit(subText,(710,770))
    if collide(mousex,mousey,700,750,200,100):
        pygame.draw.rect(screen,(0,0,0),(700,750,200,100),4)
        if clicked==True:
            showAnswer=True
            clicked=False
            attempts+=1
            if currentAnswer.upper()==answerList[currentQuestion].upper():
                score+=1

def answer():
    global currentQuestion,currentAnswer,clicked,showAnswer,colour,askedList,endScreen
    
    pygame.draw.rect(screen,(255,255,255),(50,620,1500,100))
    aText=midfont.render(answerList[currentQuestion],True,(0,0,0))
    screen.blit(aText,(60,640))

    pygame.draw.rect(screen,(200,200,200),(700,750,200,100))
    subText=midfont.render("Next",True,(0,0,0))
    screen.blit(subText,(710,770))
    if collide(mousex,mousey,700,750,200,100):
        pygame.draw.rect(screen,(0,0,0),(700,750,200,100),4)
        if clicked==True:
            askedList.append(currentQuestion)
            if len(askedList)<len(questionList):
                while currentQuestion in askedList:
                    currentQuestion=random.randint(0,len(questionList)-1)
            else:
                endScreen=True
            currentAnswer=""
            clicked=False
            showAnswer=False
            colour=(random.randint(0,255),random.randint(0,255),random.randint(0,255))




def showScore():
    scoreText=bigfont.render(str(score)+"/"+str(attempts)+" Correct",True,(0,0,0))
    screen.blit(scoreText,(550,400))   

class Pair():
    def __init__(self,text,number):
        self.text=text
        self.show=font1.render(text,True,(0,0,0))
        self.number=number

        self.x,self.y=1200,800
        while not self.x<1000 and not self.y<700:
            self.x=random.randint(10,1600-self.show.get_width())
            self.y=random.randint(10,880)
        
    def draw(self):
        global clicked,selected,pairList,selectText,remove
        screen.blit(self.show,(self.x,self.y))
        
        if selectText==self.text:
            pygame.draw.rect(screen,(0,0,0),(self.x-2,self.y-2,self.show.get_width(),20),2)
            
        if collide(mousex,mousey,self.x,self.y,self.show.get_width(),20):
            pygame.draw.rect(screen,(0,0,0),(self.x-2,self.y-2,self.show.get_width(),20),2)

            
            if clicked==True:
                if selected!="":
                    if self.number==selected and self.text!=selectText:
                        remove=True
                    else:
                        selected=""
                        selectText=""                      
                else:
                    selected=self.number
                    selectText=self.text
                clicked=False




    def getNumber(self):
        return self.number


def removePair():
    global pairList,selected,selectText

    count2=0
    while count2<len(pairList):
        if pairList[count2].getNumber()==selected:
            pairList.pop(count2)
            count2=-1
        count2+=1


    selected=""
    selectText=""



def showPairs():
    global pairList,remove
    if pairList==[]:
        for i in range(len(questionList)-1):
            newQ=Pair(questionList[i],i)
            newA=Pair(answerList[i],i)
            pairList.append(newQ)
            pairList.append(newA)


    for i in pairList:
        i.draw()
    if remove==True:
        removePair()
        remove=False



remove=False
newQ=""
newA=""
currentNew="newQ"

score=0
attempts=0
currentQuestion=""
currentAnswer=""
showAnswer=False
colour=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

askedList=[]
questionList=[]
answerList=[]

pairList=[]
selected=""
selectText=None

mousex,mousey=0,0
endScreen=False
menu=True
pairs=False
clicked=False
questionList,answerList=checkWords()
while True:
    
    if menu==True:
        screen.fill(colour)
        showAllWords()
        addWords()
        playButton()
        exitButton()
        colourButton()
        screenButton()
        showInfo()
    
    elif endScreen==True:
        screen.fill(colour)
        showScore()
        menuButton()
    elif pairs==True:
        screen.fill(colour)
        showPairs()
        menuButton()
    else:
        screen.fill(colour)
        showQuestion()
        if showAnswer==False:
            submit()
        if showAnswer==True:
            answer()
        menuButton()
        
    clicked=False
    for event in pygame.event.get():
        if event.type==QUIT:
            updateFile()
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEMOTION:
            mousex,mousey=event.pos
        elif event.type==pygame.MOUSEBUTTONUP:
            mousex,mousey=event.pos
            clicked=True
        elif event.type==pygame.KEYDOWN:
            if menu==True:
                if currentNew=="newQ":
                    if event.key==pygame.K_BACKSPACE:
                        newQ=newQ[:-1]
                    else:
                        newQ+=event.unicode
                elif currentNew=="newA":
                    if event.key==pygame.K_BACKSPACE:
                        newA=newA[:-1]
                    else:
                        newA+=event.unicode

            if event.key==pygame.K_BACKSPACE:
                currentAnswer=currentAnswer[:-1]
            else:
                currentAnswer+=event.unicode











##Add multiple saves



         


    pygame.display.update()
    clock.tick(60)
