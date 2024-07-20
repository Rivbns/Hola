#pgzero

import random
cell = Actor('Limites')
cell1 = Actor('Suelo2')
cell2 = Actor("n")
q = Actor("Trampilla")
q.topleft = (cell.height*7,cell.width*6)
q1 = Actor("Trampilla")
q1.topleft = (cell.height*5,cell.width*6)
q2 = Actor("Trampilla")
q2.topleft = (cell.height*8,cell.width*3)

size_w = 10
size_h = 10
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h
col = []
enemiesQ=[]
enemies=[]
enemiesQ1=[]
enemies1=[]
enemiesQ2=[]
enemies2=[]
d = "yes"
TITLE = "Hongo escape"
FPS = 60
win = 0
level = 1
my_map1 = [[2, 2, 2, 2, 0, 0, 0, 0, 2], 
          [2, 0, 0, 0, 0, 1, 1, 0, 2],
          [2, 0, 1, 1, 1, 1, 1, 0, 2],
          [0, 0, 1, 1, 1, 1, 0, 0, 2],
          [0, 1, 1, 0, 0, 0, 0, 0, 2],
          [0, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
          
my_map2 = [[2, 0, 0, 0, 0, 0, 0, 2, 2], 
          [2, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 1, 1, 0],
          [2, 2, 2, 2, 0, 0, 0, 0, 0]]
          
my_map3 = [[0, 0, 0, 0, 0, 0, 0, 2, 2, 2], 
          [0, 1, 0, 1, 1, 1, 0, 0, 0, 2],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [2, 0, 0, 0, 0, 0, 0, 0, 2, 2],]
char1 = Actor('Adventure2')
char1.topleft = (cell.height*6,cell.width)
char1.health = 100
char1.attack = 5
X11 = 4 * cell.width 
Y11 = 2 * cell.height
X21 = 5 * cell.width
Y21 = 3 * cell.height
X31 = 3 * cell.width
Y31 = 3 * cell.height
x11 = 5 * cell.width
y11 = 5 * cell.height
x21 = 4 * cell.width
y21 = 6 * cell.height
x31 = 2 * cell.width
y31 = 5 * cell.height
x41 = 2 * cell.width
y41 = 6 * cell.height

X12 = 5 * cell.width 
Y12 = 3 * cell.height
X22 = 6 * cell.width
Y22 = 3 * cell.height
X32 = 7 * cell.width
Y32 = 3 * cell.height
x12 = 2 * cell.width
y12 = 2 * cell.height
x22 = 6 * cell.width
y22 = 5 * cell.height
x32 = 7 * cell.width
y32 = 6 * cell.height

x13 = 1 * cell.width
y13 = 3 * cell.height
x23 = 2 * cell.width
y23 = 2 * cell.height
x33 = 2 * cell.width
y33 = 4 * cell.height
x43 = 3 * cell.width
y43 = 3 * cell.height
x53 = 3 * cell.width
y53 = 5 * cell.height
x63 = 4 * cell.width
y63 = 2 * cell.height
x73 = 4 * cell.width
y73 = 4 * cell.height
x83 = 5 * cell.width
y83 = 1 * cell.height
x93 = 5 * cell.width
y93 = 3 * cell.height
x103 = 5 * cell.width
y103 = 5 * cell.height
x113 = 6 * cell.width
y113 = 3 * cell.height
x123 = 6 * cell.width
y123 = 4 * cell.height
x133 = 7 * cell.width
y133 = 4 * cell.height

enemyq1_1 = Actor("rock_q1", topleft = (X11,Y11))
enemyq1_1.health = 10
enemyq1_1.attack = 5
enemiesQ.append(enemyq1_1)
enemyq2_1 = Actor("rock_q1", topleft = (X21,Y21))
enemyq2_1.health = 10
enemyq2_1.attack = 5
enemiesQ.append(enemyq2_1)
enemyq3_1 = Actor("rock_q1", topleft = (X31,Y31))
enemyq3_1.health = 10
enemyq3_1.attack = 5
enemiesQ.append(enemyq3_1)

enemy1_1 = Actor("enemy2", topleft = (x11,y11))
enemy1_1.health = 10
enemy1_1.attack = 5
enemies.append(enemy1_1)
enemy2_1 = Actor("enemy2", topleft = (x21,y21))
enemy2_1.health = 10
enemy2_1.attack = 5
enemies.append(enemy2_1)
enemy3_1 = Actor("enemy2", topleft = (x31,y31))
enemy3_1.health = 10
enemy3_1.attack = 5
enemies.append(enemy3_1)
enemy4_1 = Actor("enemy2", topleft = (x41,y41))
enemy4_1.health = 10
enemy4_1.attack = 5
enemies.append(enemy4_1)
#_______________________________________________
enemyq1_2 = Actor("rock_q1", topleft = (X12,Y12))
enemyq1_2.health = 10
enemyq1_2.attack = 5
enemiesQ1.append(enemyq1_2)
enemyq2_2 = Actor("rock_q1", topleft = (X22,Y22))
enemyq2_2.health = 10
enemyq2_2.attack = 5
enemiesQ1.append(enemyq2_2)
enemyq3_2 = Actor("rock_q1", topleft = (X32,Y32))
enemyq3_2.health = 10
enemyq3_2.attack = 5
enemiesQ1.append(enemyq3_2)

enemy1_2 = Actor("enemy2", topleft = (x12,y12))
enemy1_2.health = 10
enemy1_2.attack = 5
enemies1.append(enemy1_2)
enemy2_2 = Actor("enemy2", topleft = (x22,y22))
enemy2_2.health = 10
enemy2_2.attack = 5
enemies1.append(enemy2_2)
enemy3_2 = Actor("enemy2", topleft = (x32,y32))
enemy3_2.health = 10
enemy3_2.attack = 5
enemies1.append(enemy3_2)
#---------------------------------------------------
enemy1_3 = Actor("enemy2", topleft = (x13,y13))
enemy1_3.health = 10
enemy1_3.attack = 5
enemies2.append(enemy1_3)
enemy2_3 = Actor("enemy2", topleft = (x23,y23))
enemy2_3.health = 10
enemy2_3.attack = 5
enemies2.append(enemy2_3)
enemy3_3 = Actor("enemy2", topleft = (x33,y33))
enemy3_3.health = 10
enemy3_3.attack = 5
enemies2.append(enemy3_3)
enemy4_3 = Actor("enemy2", topleft = (x43,y43))
enemy4_3.health = 10
enemy4_3.attack = 5
enemies2.append(enemy4_3)
enemy5_3 = Actor("enemy2", topleft = (x53,y53))
enemy5_3.health = 10
enemy5_3.attack = 5
enemies2.append(enemy5_3)
enemy6_3 = Actor("enemy2", topleft = (x63,y63))
enemy6_3.health = 10
enemy6_3.attack = 5
enemies2.append(enemy6_3)
enemy7_3 = Actor("enemy2", topleft = (x73,y73))
enemy7_3.health = 10
enemy7_3.attack = 5
enemies2.append(enemy7_3)
enemy8_3 = Actor("enemy2", topleft = (x83,y83))
enemy8_3.health = 10
enemy8_3.attack = 5
enemies2.append(enemy8_3)
enemy9_3 = Actor("enemy2", topleft = (x93,y93))
enemy9_3.health = 10
enemy9_3.attack = 5
enemies2.append(enemy9_3)
enemy10_3 = Actor("enemy2", topleft = (x103,y103))
enemy10_3.health = 10
enemy10_3.attack = 5
enemies2.append(enemy10_3)
enemy11_3 = Actor("enemy2", topleft = (x113,y113))
enemy11_3.health = 10
enemy11_3.attack = 5
enemies2.append(enemy11_3)
enemy12_3 = Actor("enemy2", topleft = (x123,y123))
enemy12_3.health = 10
enemy12_3.attack = 5
enemies2.append(enemy12_3)
enemy13_3 = Actor("enemy2", topleft = (x133,y133))
enemy13_3.health = 10
enemy13_3.attack = 5
enemies2.append(enemy13_3)

def end():
    global win
def map1_draw():
    for i in range(len(my_map1)):
        for j in range(len(my_map1[0])):
            if my_map1[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map1[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map1[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                col.append(cell2)
                cell2.draw()
def map2_draw():
    for i in range(len(my_map2)):
        for j in range(len(my_map2[0])):
            if my_map2[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map2[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map2[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                col.append(cell2)
                cell2.draw()
def map3_draw():
    for i in range(len(my_map3)):
        for j in range(len(my_map3[0])):
            if my_map3[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map3[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map3[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                col.append(cell2)
                cell2.draw()
def draw():
    screen.fill("#2f3542")
    if win == 0 and level == 1:
        map1_draw()
        char1.draw()
        q.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(char1.health, center=(75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(char1.attack, center=(425, 475), color = 'white', fontsize = 20)
        for i in range(len(enemiesQ)):
            enemiesQ[i].draw()
        for i in range(len(enemies)):
            enemies[i].draw()
    if win == 0 and level == 2:
        map2_draw()
        char1.draw()
        q1.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(char1.health, center=(75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(char1.attack, center=(425, 475), color = 'white', fontsize = 20)
        for i in range(len(enemiesQ1)):
            enemiesQ1[i].draw()
        for i in range(len(enemies1)):
            enemies1[i].draw()
    if win == 0 and level == 3:
        map3_draw()
        char1.draw()
        q2.draw()
        screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
        screen.draw.text(char1.health, center=(75, 475), color = 'white', fontsize = 20)
        screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
        screen.draw.text(char1.attack, center=(425, 475), color = 'white', fontsize = 20)
        for i in range(len(enemiesQ2)):
            enemiesQ2[i].draw()
        for i in range(len(enemies2)):
            enemies2[i].draw()
    if win == 0 and level == 4:
        screen.draw.text("!!HAZ GANADO¡¡", center=(cell.width*5, cell.width*5), color = 'white', fontsize = 40)
    if win == -1:
        screen.draw.text("Perdiste", center=(225, 250), color = 'white', fontsize = 40)
    if win == 1:
        screen.draw.text("Ganaste", center=(225, 250), color = 'white', fontsize = 40)
def on_key_down(key):
    global level
    global d
    global char
    old_x = char1.x
    old_y = char1.y
    if level == 1:
        if (keyboard.right or keyboard.d) and (char1.topleft != (cell.height*6,cell.width*1) and char1.topleft != (cell.height*6,cell.width*2) and char1.topleft != (cell.height*5,cell.width*3) and char1.topleft != (cell.height*2,cell.width*4) and char1.topleft != (cell.height*6,cell.width*5)) :
            char1.x += cell.width
            char1.image = 'Adventure_right2'
        if (keyboard.left or keyboard.a) and (char1.topleft != (cell.height*5,cell.width*1) and char1.topleft != (cell.height*2,cell.width*2) and char1.topleft != (cell.height*2,cell.width*3) and char1.topleft != (cell.height*1,cell.width*4) and char1.topleft != (cell.height*1,cell.width*5) and char1.topleft != (cell.height*1,cell.width*6)):
            char1.x -= cell.width
            char1.image = 'Adventure_left2'
        if (keyboard.down or keyboard.s) and (char1.topleft != (cell.height*1,cell.width*6) and char1.topleft != (cell.height*2,cell.width*6) and char1.topleft != (cell.height*3,cell.width*6) and char1.topleft != (cell.height*4,cell.width*6) and char1.topleft != (cell.height*5,cell.width*6) and char1.topleft != (cell.height*6,cell.width*6) and char1.topleft != (cell.height*6,cell.width*2) and char1.topleft != (cell.height*5,cell.width*3) and char1.topleft != (cell.height*4,cell.width*3) and char1.topleft != (cell.height*3,cell.width*3)):
            char1.y += cell.height
            char1.image = 'Adventure_down2'
        if (keyboard.up or keyboard.w) and (char1.topleft != (cell.height*6,cell.width*1) and char1.topleft != (cell.height*1,cell.width*4) and char1.topleft != (cell.height*5,cell.width*1) and char1.topleft != (cell.height*4,cell.width*2) and char1.topleft != (cell.height*3,cell.width*2) and char1.topleft != (cell.height*2,cell.width*2) and char1.topleft != (cell.height*6,cell.width*5) and char1.topleft != (cell.height*5,cell.width*5) and char1.topleft != (cell.height*4,cell.width*5) and char1.topleft != (cell.height*3,cell.width*5)):
            char1.y -= cell.height
            char1.image = 'Adventure_up2'
    if level == 2:
        if (keyboard.right or keyboard.d) and (char1.topleft != (cell.height*2,cell.width*5) and char1.topleft != (cell.height*2,cell.width*4) and char1.topleft != (cell.height*2,cell.width*3) and char1.topleft != (cell.height*2,cell.width*2) and char1.topleft != (cell.height*5,cell.width*1) and char1.topleft != (cell.height*7,cell.width*2) and char1.topleft != (cell.height*7,cell.width*3) and char1.topleft != (cell.height*7,cell.width*4) and char1.topleft != (cell.height*7,cell.width*5) and char1.topleft != (cell.height*7,cell.width*6)):
            char1.x += cell.width
            char1.image = 'Adventure_right2'
        if (keyboard.left or keyboard.a) and (char1.topleft != (cell.height*1,cell.width*5) and char1.topleft != (cell.height*1,cell.width*4) and char1.topleft != (cell.height*1,cell.width*3) and char1.topleft != (cell.height*2,cell.width*2) and char1.topleft != (cell.height*2,cell.width*1) and char1.topleft != (cell.height*4,cell.width*2) and char1.topleft != (cell.height*5,cell.width*3) and char1.topleft != (cell.height*5,cell.width*4) and char1.topleft != (cell.height*5,cell.width*5) and char1.topleft != (cell.height*5,cell.width*6)):
            char1.x -= cell.width
            char1.image = 'Adventure_left2'
        if (keyboard.down or keyboard.s) and (char1.topleft != (cell.height*1,cell.width*5) and char1.topleft != (cell.height*2,cell.width*5) and char1.topleft != (cell.height*3,cell.width*1) and char1.topleft != (cell.height*4,cell.width*2) and char1.topleft != (cell.height*5,cell.width*6) and char1.topleft != (cell.height*6,cell.width*6) and char1.topleft != (cell.height*7,cell.width*6)):
            char1.y += cell.height
            char1.image = "Adventure_down2"
        if (keyboard.up or keyboard.w) and (char1.topleft != (cell.height*1,cell.width*3) and char1.topleft != (cell.height*2,cell.width*1) and char1.topleft != (cell.height*3,cell.width*1) and char1.topleft != (cell.height*4,cell.width*1) and char1.topleft != (cell.height*5,cell.width*1) and char1.topleft != (cell.height*6,cell.width*2) and char1.topleft != (cell.height*7,cell.width*2)):
            char1.y -= cell.height
            char1.image = 'Adventure_up2'
    if level == 3:
        if (keyboard.right or keyboard.d) and (char1.topleft != (cell.height*1,cell.width*1) and char1.topleft != (cell.height*5,cell.width*1) and char1.topleft != (cell.height*7,cell.width*2) and char1.topleft != (cell.height*8,cell.width*3) and char1.topleft != (cell.height*8,cell.width*4) and char1.topleft != (cell.height*6,cell.width*5)):
            char1.x += cell.width
            char1.image = 'Adventure_right2'
        if (keyboard.left or keyboard.a) and (char1.topleft != (cell.height*1,cell.width*1) and char1.topleft != (cell.height*3,cell.width*1) and char1.topleft != (cell.height*1,cell.width*2) and char1.topleft != (cell.height*1,cell.width*3) and char1.topleft != (cell.height*1,cell.width*4) and char1.topleft != (cell.height*2,cell.width*5)):
            char1.x -= cell.width
            char1.image = 'Adventure_left2'
        if (keyboard.down or keyboard.s) and (char1.topleft != (cell.height*1,cell.width*4) and char1.topleft != (cell.height*2,cell.width*5) and char1.topleft != (cell.height*3,cell.width*5) and char1.topleft != (cell.height*4,cell.width*5) and char1.topleft != (cell.height*5,cell.width*5) and char1.topleft != (cell.height*6,cell.width*5) and char1.topleft != (cell.height*7,cell.width*4) and char1.topleft != (cell.height*8,cell.width*4)):
            char1.y += cell.height
            char1.image = "Adventure_down2"
        if (keyboard.up or keyboard.w) and (char1.topleft != (cell.height*1,cell.width*1) and char1.topleft != (cell.height*2,cell.width*2) and char1.topleft != (cell.height*3,cell.width*1) and char1.topleft != (cell.height*4,cell.width*1) and char1.topleft != (cell.height*5,cell.width*1) and char1.topleft != (cell.height*6,cell.width*2) and char1.topleft != (cell.height*7,cell.width*2) and char1.topleft != (cell.height*8,cell.width*3)):
            char1.y -= cell.height
            char1.image = 'Adventure_up2'
    
    enemy_list = char1.collidelist(enemiesQ)
    if enemy_list != -1 and level == 1:
        char1.x = old_x
        char1.y = old_y
        enemy = enemiesQ[enemy_list]
        if (keyboard.right or keyboard.d):
            enemy.x += cell.width
        elif (keyboard.left or keyboard.a):
            enemy.x -= cell.width
        elif (keyboard.down or keyboard.s):
            enemy.y += cell.height
        elif (keyboard.up or keyboard.w):
            enemy.y -= cell.width
        if enemy.health <= 0:
            enemiesQ.pop(enemy_list)
    enemy_list_1 = char1.collidelist(enemiesQ1)
    if enemy_list_1 != -1 and level == 2:
        char1.x = old_x
        char1.y = old_y
        enemy_1 = enemiesQ1[enemy_list_1]
        if (keyboard.right or keyboard.d):
            enemy_1.x += cell.width
        elif (keyboard.left or keyboard.a):
            enemy_1.x -= cell.width
        elif (keyboard.down or keyboard.s):
            enemy_1.y += cell.height
        elif (keyboard.up or keyboard.w):
            enemy_1.y -= cell.width
        if enemy_1.health <= 0:
            enemiesQ1.pop(enemy_list_1)
            
    enemy_list2 = char1.collidelist(enemies)
    if enemy_list2 != -1 and level == 1:
        char1.x = old_x
        char1.y = old_y
        enemy1 = enemies[enemy_list2]
        if (keyboard.right or keyboard.d):
            enemy1.x += cell.width
        elif (keyboard.left or keyboard.a):
            enemy1.x -= cell.width
        elif (keyboard.down or keyboard.s):
            enemy1.y += cell.height
        elif (keyboard.up or keyboard.w):
            enemy1.y -= cell.width
        if enemy1.health <= 0:
            enemies.pop(enemy_list2)
    enemy_list2_1 = char1.collidelist(enemies1)
    if enemy_list2_1 != -1 and level == 2:
        char1.x = old_x
        char1.y = old_y
        enemy1_1 = enemies1[enemy_list2_1]
        if (keyboard.right or keyboard.d):
            enemy1_1.x += cell.width
        elif (keyboard.left or keyboard.a):
            enemy1_1.x -= cell.width
        elif (keyboard.down or keyboard.s):
            enemy1_1.y += cell.height
        elif (keyboard.up or keyboard.w):
            enemy1_1.y -= cell.width
        if enemy1_1.health <= 0:
            enemies1.pop(enemy_list2_1)
    enemy_list2_2 = char1.collidelist(enemies2)
    if enemy_list2_2 != -1 and level == 3:
        char1.x = old_x
        char1.y = old_y
        enemy1_2 = enemies2[enemy_list2_2]
        if (keyboard.right or keyboard.d):
            enemy1_2.x += cell.width
        elif (keyboard.left or keyboard.a):
            enemy1_2.x -= cell.width
        elif (keyboard.down or keyboard.s):
            enemy1_2.y += cell.height
        elif (keyboard.up or keyboard.w):
            enemy1_2.y -= cell.height
        if enemy1_2.health <= 0:
            enemies2.pop(enemy_list2_2)
            
    if char1.colliderect(q) and level == 1:
        level = 2
        d = "yes"
    if char1.colliderect(q1) and level == 2:
        level = 3
        d = "yes"
    if char1.colliderect(q2) and level == 3:
        level = 4
        d = "yes"
    if keyboard.s or keyboard.w or keyboard.a or keyboard.d:
            if level == 2 and d == "yes":
                char1.topleft = (cell.height,cell.width*4)
                d = "no"
            elif level == 3 and d == "yes":
                char1.topleft = (cell.height,cell.width)
                d = "no"
            elif level == 4 and d == "yes":
                char1.topleft = (cell.height*5,cell.width*5)
                d = "no"
