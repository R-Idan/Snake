import pygame
import random

pygame.init()
fps =30
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
size = height
if(height>width):
    size=width
size=size/1.5+size/1.5%16
highScore=3
isNewHS=False
# loading the image as python object
apple_img = pygame.image.load("apple.png")
# resizing image
apple_img = pygame.transform.scale(apple_img, (size/16, size/16))
screen = pygame.display.set_mode((size,size))
pygame.display.set_caption('Snake')
rows, cols = (16, 16)
gameBoard = [[0 for i in range(cols)] for j in range(rows)]
#snake class #OOP
class snake(object):
    body = []
    changeDir=False
    def __init__(self):
        self.body =[(size*5/16,size*4/16),(size*4/16,size*4/16),(size*3/16,size*4/16)]
        self.direction='R'

    def move(self,hasEaten):
        global running
    # F - forward, R - right, L - left, D - downward
        count =0
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if count ==0: #incase 2 or more moves in 1 turn
                    if event.key == pygame.K_LEFT:
                        self.body.insert(0,(self.body[0][0]-size/16,self.body[0][1]))
                        self.direction = 'L'
                        self.changeDir=True
                        count = 1
                    elif event.key == pygame.K_RIGHT:
                        self.body.insert(0,(self.body[0][0]+size/16,self.body[0][1]))
                        self.direction = 'R'
                        self.changeDir=True
                        count = 1
                    elif event.key == pygame.K_DOWN:
                        self.body.insert(0,(self.body[0][0],self.body[0][1]+size/16))
                        self.direction = 'D'
                        self.changeDir=True
                        count = 1
                    elif event.key == pygame.K_UP:
                        self.body.insert(0,(self.body[0][0],self.body[0][1]-size/16))
                        self.direction = 'F'
                        self.changeDir=True
                        count = 1
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
                    
        #keep going in the same direction 
        if self.changeDir==False:
            if self.direction=='L':
                self.body.insert(0,(self.body[0][0]-size/16,self.body[0][1]))
            if self.direction=='R':
                self.body.insert(0,(self.body[0][0]+size/16,self.body[0][1]))
            if self.direction=='D':
                self.body.insert(0,(self.body[0][0],self.body[0][1]+size/16))
            if self.direction=='F':
                self.body.insert(0,(self.body[0][0],self.body[0][1]-size/16))
        self.changeDir=False
        if self.body[0]== gameApple.pos[0]:
            hasEaten=True
            gameApple.randomizePos()
        if hasEaten==False:
            self.body.pop()

                
    def drawSnake(self):
        for i in range(len(self.body)):
            pygame.draw.rect(screen, (0,0,255), pygame.Rect(self.body[i][0],self.body[i][1],size/16,size/16))
            if i==0:
                if self.direction=='L':
                    pygame.draw.circle(screen, (255,255,255), (int(self.body[i][0]+size/40),int(self.body[i][1]+size/32)), int(size/80))
                    pygame.draw.circle(screen, (0,0,0), (int(self.body[i][0]+size/49),int(self.body[i][1]+size/32)), int(size/170))
                if self.direction=='R':
                    pygame.draw.circle(screen, (255,255,255), (int(self.body[i][0]+size/40),int(self.body[i][1]+size/32)), int(size/80))
                    pygame.draw.circle(screen, (0,0,0), (int(self.body[i][0]+size/32),int(self.body[i][1]+size/32)), int(size/170))
                if self.direction=='F':
                    pygame.draw.circle(screen, (255,255,255), (int(self.body[i][0]+size/40),int(self.body[i][1]+size/32)), int(size/80))
                    pygame.draw.circle(screen, (0,0,0), (int(self.body[i][0]+size/40),int(self.body[i][1]+size/40)), int(size/170))
                if self.direction=='D':
                    pygame.draw.circle(screen, (255,255,255), (int(self.body[i][0]+size/40),int(self.body[i][1]+size/32)), int(size/80))
                    pygame.draw.circle(screen, (0,0,0), (int(self.body[i][0]+size/40),int(self.body[i][1]+size/27)), int(size/170))
    def checkForLoss(self):
        for index in range(len(self.body)):
            if self.body[index] == self.body[0] and index!=0:
                return True
        if self.body[0][0]<0 or self.body[0][1]<0 or self.body[0][0]>=size or self.body[0][1]>=size:
            return True


#apple class #OOP
class apple(object):
    pos =[]
    def __init__(self):
        self.pos = [(size*12/16,size*4/16)]

    def drawApple(self):
            #pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.pos[0][0],self.pos[0][1],size/16,size/16))
            screen.blit(apple_img, (self.pos[0][0],self.pos[0][1]))
    def randomizePos(self):
            while self.pos[0] in gameSnake.body:
                self.pos.pop()
                self.pos.insert(0,(random.randint(0, 15)*size/16,random.randint(0, 15)*size/16))
            print(gameSnake.body[0], self.pos)
#draw like google snake game board :)
def drawBoard():
    screen.fill((255, 255, 255))
    for i in range(16):
        for j in range(16):
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                pygame.draw.rect(screen, (170, 215, 81), pygame.Rect(size*j/16,size*i/16,size/16,size/16))
            else:
                pygame.draw.rect(screen, (162, 209, 73), pygame.Rect(size*j/16,size*i/16,size/16,size/16))
def reset():
    global gameSnake
    gameSnake=snake()
    global gameApple
    gameApple = apple()
    global isNewHS
    isNewHS=False
my_font = pygame.font.SysFont('arial', int(size/25))
def waitForSpace():
    global highScore
    global isNewHS
    
    running = True
    while running:
        screen.fill((255, 255, 255))
        textScore = my_font.render("Your score is: " + str(len(gameSnake.body)), 1, (0, 0, 0))
        text_rectScore = textScore.get_rect(center=(size/2,size/10))
        screen.blit(textScore, text_rectScore)
        if len(gameSnake.body)>highScore:
            isNewHS=True
        if isNewHS==True:
            highScore=len(gameSnake.body)
            TextHighScore = my_font.render("New high score!", 1, (0, 0, 0))
            text_rectHighScore = TextHighScore.get_rect(center=(size/2,size/5))
            screen.blit(TextHighScore, text_rectHighScore)
        else:
            TextHighScore = my_font.render("Your high score is: " + str(highScore), 1, (0, 0, 0))
            text_rectHighScore = TextHighScore.get_rect(center=(size/2,size/5))
            screen.blit(TextHighScore, text_rectHighScore)
        textPlayAgain = my_font.render("Press space to try again", 1, (0, 0, 0))
        text_rectPlayAgain = textPlayAgain.get_rect(center=(size/2,size/3))
        screen.blit(textPlayAgain, text_rectPlayAgain)
        pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset()
                game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

    
clock = pygame.time.Clock()
gameSnake = snake()
gameApple = apple()
running = True
def game():
    while running:
        clock.tick(7)
        drawBoard()
        gameApple.drawApple()
        gameSnake.drawSnake()
        gameSnake.move(False)
        pygame.display.flip()
        if gameSnake.checkForLoss()==True:
            return
    return 

game()
waitForSpace()
