"""
This is a 2D-space shooting game created using pygame. The game demonstrates object oriented paradigm to create 
the game props. The game has 5 levels and the player movement is controlled using arrow keys and the player fire is
controlled using 'z' key. Inorder to win in the game the user has to defeat all the aliens of all the levels.

"""
import pygame
import random
from pygame import mixer

pygame.init()

#SETTINGS
height = 500
width = 400
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font(None,32)
screen = pygame.display.set_mode((width,height))
running = True
score = 0
level = 1
num_of_enemies = 2

#Audio
mixer.music.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Audio\background.wav')
mixer.music.play(-1)
explosion_sound=mixer.Sound(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Audio\explosion.wav')
fire_sound=mixer.Sound(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Audio\laser.wav')

#Title and caption
pygame.display.set_caption('Alien Invaders')
icon = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\icon.png')
pygame.display.set_icon(icon)

#Backgrounds

b1 = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Background\1.png')
b2 = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Background\2.png')
b3 = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Background\3.png')
b4 = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Background\4.png')
b5 = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Background\5.png')

#Player
pimage = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\Hero.png')
pimage = pygame.transform.scale(pimage,(32,32))

#Enemy
eimage = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\Soldier.png')
efire = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\laser.png')
commander = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\Commander.png')
cfire = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\cfire.png')
boss = pygame.image.load((r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\Boss.png'))
bfire1 = pygame.image.load((r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\bfire1.png'))
bfire2 = pygame.image.load((r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\bfire2.png'))
main_boss = pygame.image.load((r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\MainBoss.png'))
mfire1 = pygame.image.load((r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\mfire1.png'))
mfire2 = pygame.image.load((r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\mfire2.png'))

#Power
power_img = pygame.image.load(r'C:\Users\LENOVO\Desktop\Projects\Pygame\Images\fire.png')
power_img = pygame.transform.scale(power_img,(16,16))

#Final Boss class
class main_boss_class():
    def __init__(self): #Initialising
        self.x = 184
        self.y = 100        
        self.firex = self.x+16
        self.firey = self.y+64
        self.health = 250
        self.change = 0
        self.firechange = 0.3
        self.firechangex = 0.15
        self.count = 0
        self.f = 0
    
    def draw(self,screen):  #Drawing object on screen
        screen.blit(main_boss,(self.x,self.y))
        
    
    def move(self): #Object Movement
        
        if self.health>0:            
            self.x += self.change
            if self.x < 0:
                self.x = 0
                self.change = -self.change
            if self.x >= 336:
                self.x = 336
                self.change = -self.change
        
        if self.health < 100 and self.f == 0:
                self.f = 1
                self.change = 0.2

    def fire(self): #Object fire
        if self.count % 3 != 1:
            screen.blit(mfire1,(self.firex,self.firey))
            self.firey += self.firechange
            self.firex += (-1)**self.count*self.firechangex
            
        else:
            screen.blit(mfire2,(self.firex,self.firey))
            self.firey += (self.firechange+0.1)
        
        if self.firey > 468:
            self.firey = self.y+64
            self.firex = self.x+16            
            self.count += 1
 
#Enemy class
class enemy():

    def __init__(self,type): #Initialising
        self.x = 184
        self.x = random.randint(1,368)
        self.y = 100
        self.firex = self.x+16
        self.firey = self.y+64        
        self.type = type

        if type == 1:
            self.health = 50
            self.firechange = 0.1
            self.change = 0.1
        elif type == 2:
            self.health = 100
            self.firechange = 0.2
            self.change = 0.15
        elif type == 3:
            self.health = 150
            self.firechange1 = 0.25
            self.firechange2 = 0.4
            self.count = 0
            self.change = 0.15
        

    def draw(self,screen): #Drawing object on screen
        if self.health>0:
            if self.type == 1:
                screen.blit(eimage,(self.x,self.y))
            elif self.type == 2:
                screen.blit(commander,(self.x,self.y))
            elif self.type == 3:
                screen.blit(boss,(self.x,self.y))

    def move(self): #Object Movement
        if self.health > 0:            
            self.x += self.change
            if self.x < 0:
                self.x = 0
                self.change =- self.change
            if self.x > 336:
                self.x = 336
                self.change =- self.change

    def fire(self): #Object Fire
        if self.health > 0:
            if self.type == 1:
                screen.blit(efire,(self.firex,self.firey))
                self.firey += self.firechange
            elif self.type == 2:
                screen.blit(cfire,(self.firex,self.firey))
                self.firey += self.firechange
            elif self.type == 3:
                if self.count%3 == 2:
                    screen.blit(bfire2,(self.firex,self.firey))                    
                    self.firey += self.firechange2
                else:
                    screen.blit(bfire1,(self.firex,self.firey))
                    self.firey += self.firechange1         
                
            if self.firey > 468:
                self.firey = self.y+64
                self.firex = self.x+16
                if self.type == 3:
                    self.count += 1

#Player class
class player():

    def __init__(self): #Initialising
        self.x = 184
        self.x = 184
        self.y = 460
        self.changex = 0
        self.changey = 0

    def draw(self,screen): #Drawing object on screen
        screen.blit(pimage,(self.x,self.y))

    def move(self): #Object Movement
        self.x += self.changex
        if self.x < 0:
            self.x = 0            
        if self.x > 368:
            self.x = 368
            
        self.y += self.changey
        if self.y < 0:
            self.y = 0            
        if self.y > 468:
            self.y = 468

# Player power
class power():

    def __init__(self): #Initialising
        self.x = 184
        self.x = 0
        self.y = 460
        self.state = False
        self.change = 0.33

    def draw(self,screen):        
        screen.blit(power_img,(self.x+16,self.y-16))

    def fire(self,player):
        if self.state:
            self.y -= self.change
            if self.y <= 16:
                self.y = player.y
                self.state = False
            self.draw(screen)

#Collision detection function
def collision(x1,y1,x2,y2):    
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    if distance < 27:

        return True
    else:
        return False
#Score display 
def display_score():
    global score
    img = font.render('Score = ' + str(score),True,white)       
    screen.blit(img,(10,10))

#Level display 
def display_level():
    global level
    img = font.render('Level = ' + str(level),True,white)       
    screen.blit(img,(300,10))

#Running objects on screen
def start(x):
    x.draw(screen)
    x.move()
    x.fire()

#End Game
def game_over():
    explosion_sound.play()
    screen.fill(black)
    mixer.music.stop()        
    img = font.render('Game Over',True,white)       
    screen.blit(img,(140,250))
    
    pygame.time.delay(50)

# Game objects (Enimies of different levels, player and player's power)
e1 = enemy(1)

e2 = []
for i in range(num_of_enemies):
    x = enemy(1)
    e2.append(x)

e3 = []
for i in range(num_of_enemies):
    x = enemy(1)
    e3.append(x)
e3.append(enemy(2))

e4 = []
for i in range(num_of_enemies):
    x = enemy(3)
    e4.append(x)

e5 = []
e5.append(main_boss_class())
for i in range(num_of_enemies):
    x = enemy(1)
    e5.append(x)

p = player()
po = power()


# Game Loop (MAIN)
while(running):
    
    pygame.display.update()
    
    #Displaying level's background image
    if level==1:
        screen.blit(b1,(0,0))
    elif level==2:
        screen.blit(b2,(0,0))
    elif level==3:
        screen.blit(b3,(0,0))
    elif level==4:
        screen.blit(b4,(0,0))
    elif level==5:
        screen.blit(b5,(0,0))

    display_score()
    display_level()

    #Start player
    p.draw(screen)
    p.move()
    po.fire(p) 
    
    #Detect keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.changex = -0.1
            if event.key == pygame.K_RIGHT:
                p.changex = 0.1
            if event.key == pygame.K_UP:
                p.changey = -0.1
            if event.key == pygame.K_DOWN:
                p.changey = 0.1
            if event.key == pygame.K_LSHIFT:
                if level<5:
                    level+=1
            if event.key == pygame.K_SPACE:
                if po.state == False:
                    fire_sound.play()
                    po.x = p.x
                    po.y = p.y                    
                    po.state = True
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            p.changex = 0
            p.changey = 0

    #Level 1 runtime settings
    if level == 1:
        if e1 is not None:
            start(e1)
            
            if collision(e1.x,e1.y,po.x,po.y): #Hit Enemy
                explosion_sound.play()
                po.y = p.y
                e1.health -= 25
                po.state = False #Return power back to player
                score += 5                
                if e1.health <= 0: #Enemy death
                    score += 50
                    e1=None
                    continue                    
                    
            if collision(e1.firex,e1.firey,p.x,p.y): #Hit Player
                game_over()
    
        if e1 is None: level += 1

    #Level 2 runtime settings
    if level == 2:
        for x in e2:
            start(x)
        
        for m in e2:
            if collision(m.x,m.y,po.x,po.y): #Hit Enemy
                explosion_sound.play()
                po.y = p.y
                m.health -= 25
                po.state = False #Return power back to player
                score += 5
                if m.health <= 0: #Enemy death
                    e2.remove(m)
                    score += 50                    

            if collision(m.firex,m.firey,p.x,p.y): #Hit Player
                game_over()

        if len(e2) == 2:
            if collision(e2[0].x,e2[0].y,e2[1].x,e2[1].y):
                e2[0].change =- (e2[0].change+0.01)
                e2[1].change =- (e2[1].change-0.01)

        if len(e2)  == 0: level += 1

    #Level 3 runtime settings
    if level == 3:
        for x in e3:
            start(x)

        for m in e3: #Hit Enemy
            if collision(m.x,m.y,po.x,po.y):
                explosion_sound.play()
                po.y = p.y
                m.health -= 25
                po.state = False #Return power back to player
                score += 10
                if m.health <= 0: #Enemy death
                    if m.type == 1:
                        score += 50
                        e3.remove(m)
                    else:
                        score += 100
                        e3.remove(m)

            if collision(m.firex,m.firey,p.x,p.y): #Hit Player
                game_over()

        if len(e3) == 0: level += 1

    #Level 4 runtime settings
    if level == 4:
        for x in e4:
            start(x)

        for m in e4: #Hit Enemy
            if collision(m.x,m.y,po.x,po.y):
                explosion_sound.play()
                po.y = p.y
                m.health -= 25
                po.state = False #Return power back to player
                score += 15
                if m.health <= 0:
                    score += 200
                    e4.remove(m)

            if collision(m.firex,m.firey,p.x,p.y): #Hit Player
                game_over()
                

            if len(e4) == 0: level += 1

    #Level 5 runtime settings
    if level == 5:
        for x in e5:
            start(x)

        for m in e5: #Hit Enemy
            if collision(m.x,m.y,po.x,po.y):
                explosion_sound.play()
                po.y = p.y
                m.health -= 25
                po.state = False #Return power back to player
                score += 15
                if m.health <= 0: #Enemy death
                    score += 250
                    e5.remove(m)

            if collision(m.firex,m.firey,p.x,p.y): #Hit Player
                game_over()
        
        if len(e5) == 0: #Win Game
            screen.fill(black)        
            img = font.render('YOU WIN',True,white)
            img1 = font.render('Score = ' + str(score),True,white)  
            screen.blit(img,(140,250))
            screen.blit(img1,(140,300))
            pygame.time.delay(50)
            