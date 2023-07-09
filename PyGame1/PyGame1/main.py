import pygame as pgm
import random as rnd
#initialize the pygame
pgm.init()

#create the screen
screenW = 800
screenH = 600
screen = pgm.display.set_mode((screenW,screenH))

#Caption and Icon
pgm.display.set_caption("Space Invaders")
icon = pgm.image.load("./imageresource/ufo.png")

pgm.display.set_icon(icon)

# Player
playerImg = pgm.image.load("./imageresource/spaceship2.png")
playerX = 370
playerY = 480
player_max_X = 770
player_max_Y = 570
player_min_X = 0
player_min_Y = 0
playerx_change = 0
playerx_change_ratio = 0.1;

#Enemy
enemyImg = pgm.image.load("./imageresource/alien.png")
enemy_spwan_x = rnd.randint(0,760)
enemy_spawn_y = rnd.randint(30,130)

enemyX = enemy_spwan_x
enemyY = enemy_spawn_y
enemy_max_X = 760
enemy_max_Y = 570
enemy_min_X = 0
enemy_min_Y = 0
#enemyx_change = 0
#enemyy_change = 0
enemy_change_ratio_x = 0.05;
enemy_change_ratio_y = 10;

#Backgroud
background =  pgm.image.load("./imageresource/gamebg.jpg")

# Bullet
bulletImg = pgm.image.load("./imageresource/spaceship2.png")
bulletX = 0
bulletY = 0
bullet_max_X = 800
bullet_max_Y = 600
bullet_min_X = 0
bullet_min_Y = 0
bullet_change_ratio = 0.5;
bullet_spawn = True

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
def bullet(x,y):
    screen.blit(bulletImg,(x,y))
# Game Loop
running = True;
while running:
    #RGB - Red, Green, Blue
    screen.fill((0,10,0))
    #background load
    screen.blit(background,(0,0))
    

    for ev in pgm.event.get():
        if ev.type == pgm.QUIT: 
             running = False

    #if keystroke pressed check right or left
        if ev.type == pgm.KEYDOWN:
            if ev.key == pgm.K_LEFT:
                print("LEFT ARROW PRESSED")
                playerx_change -= playerx_change_ratio;
            if ev.key == pgm.K_RIGHT:
                print("RIGHT ARROW PRESSED")
                playerx_change += playerx_change_ratio;
            if ev.key == pgm.K_SPACE:
                print("BULLET FIRED")
                bullet_spawn = True
                bullet(playerX,playerY)
        if ev.type == pgm.KEYUP:
            if ev.key == pgm.K_LEFT or ev.key == pgm.K_RIGHT:
                print("KeyStroke Released ")
                playerx_change = 0;

    # player coordinate change
    playerX += playerx_change
    if (playerX > player_max_X):
        playerX = player_max_X
    if (playerX < player_min_X):
        playerX = player_min_X
    # Enemy coordinate change
    enemyX += enemy_change_ratio_x
    #enemyY += enemy_change_ratio_y

    if (enemyX > enemy_max_X):
        enemyX = enemy_max_X
        enemy_change_ratio_x = -enemy_change_ratio_x
        enemyY += enemy_change_ratio_y
    if (enemyX < enemy_min_X):
        enemyX = enemy_min_X
        enemy_change_ratio_x = -enemy_change_ratio_x
        enemyY += enemy_change_ratio_y

    if (enemyY > enemy_max_Y):
        enemyY = enemy_max_Y
    if (enemyY < enemy_min_Y):
        enemyY = enemy_min_Y
    # bullet fire
    if bullet_spawn==True:
        bulletY += bullet_change_ratio
        print(str(bulletX) + '-Bx-By-'+ str(bulletY))


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pgm.display.update()

    
