import pygame
from pygame.locals import *
import random
import os

def holes(hole):
    scrn.fill((207, 184, 128), (0, 100, scrn.get_width(), scrn.get_height()))
    scrn.blit(hole, (25, 300))
    scrn.blit(hole, (125, 200))
    scrn.blit(hole, (225, 300))
    scrn.blit(hole, (325, 200))
    scrn.blit(hole, (425, 300))
    pygame.display.flip()

def numbers(hole):
    holes(hole)

def peek(hole, frogpeek, frogpop, num):
    x = (num - 1)*100 + 25
    y = 0
    if num%2 == 0:
        y = 200
    else:
        y = 300

    scrn.blit(frogpeek, (x,y))
    pygame.display.flip()

    pygame.time.delay(100)
    scrn.fill((207, 184, 128), (0, 100, scrn.get_width(), scrn.get_height()))
    holes(hole)

    scrn.blit(frogpop, (x,y))
    pygame.display.flip()

def leave(hole, frogpeek, num):
    x = (num - 1)*100 + 25
    y = 0
    if num%2 == 0:
        y = 200
    else:
        y = 300
    scrn.fill((207, 184, 128), (0, 100, scrn.get_width(), scrn.get_height()))
    holes(hole)
    scrn.blit(frogpeek, (x,y))
    pygame.display.flip()
    pygame.time.wait(50)

def explode(hole, boom1, boom2, num):
    x = (num - 1)*100 + 25
    y = 0
    if num%2 == 0:
        y = 200
    else:
        y = 300
    scrn.fill((207, 184, 128), (0, 100, scrn.get_width(), scrn.get_height()))
    holes(hole)

    scrn.blit(boom2, (x,y))
    pygame.display.flip()
    pygame.time.delay(100)


pygame.init()

scrn = pygame.display.set_mode((600,600))
pygame.display.set_caption("jeffrey's frog game")

#get path to images
script_dir = os.path.dirname(__file__)
rel_path = "..\\frog game\\images\\"
abs_file_path = os.path.join(script_dir, rel_path)


imp = pygame.image.load(abs_file_path + "menufrog" + ".png").convert_alpha()

# imp = pygame.transform.scale(imp, (60,60))
imp.set_colorkey((246, 246, 246))

scrn.fill((207, 184, 128))
scrn.blit(imp, (-150,150))

font = pygame.font.SysFont(None, 72)
f = font.render('Frog game', True, (0,0,0))

start = pygame.font.SysFont(None, 30)
s = start.render('Press any button to play', True, (0,0,0))

scrn.blit(f, (155, 60))
scrn.blit(s, (160, 120))

# paint screen one time
pygame.display.flip()
status = True

#wait for input
while (status):
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        quit()
    elif event.type == KEYDOWN:
        break

#screen reset
scrn.fill((207, 184, 128))
pygame.display.flip()

#load images
hole = pygame.image.load(abs_file_path + "hole" + ".png").convert_alpha()
frogpeek = pygame.image.load(abs_file_path + "frogpeek" + ".png").convert_alpha()
frogpop = pygame.image.load(abs_file_path + "frogpop" + ".png").convert_alpha()
boom1 = pygame.image.load(abs_file_path + "hit1" + ".png").convert_alpha()
boom2 = pygame.image.load(abs_file_path + "hit2" + ".png").convert_alpha()

hole = pygame.transform.scale(hole, (150, 150))
hole.set_colorkey((255, 255, 255))

frogpeek = pygame.transform.scale(frogpeek, (150, 150))
frogpeek.set_colorkey((255, 255, 255))

frogpop = pygame.transform.scale(frogpop, (150, 150))
frogpop.set_colorkey((255, 255, 255))

boom1 = pygame.transform.scale(boom1, (150, 150))
boom1.set_colorkey((255, 255, 255))

boom2 = pygame.transform.scale(boom2, (150, 150))
boom2.set_colorkey((255, 255, 255))

keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]

while(1):
    #screen reset and start game
    scrn.fill((207, 184, 128))
    points = 0
    #start game
    status = True
    holes(hole)

    d = 1500

    wrong = 0

    #show numbers over holes
    fsize = 60  
    one = pygame.font.FontType(None, fsize)
    o = one.render('1', True, (0,0,0))

    two = pygame.font.Font(None, fsize)
    to = two.render('2', True, (0,0,0))

    three = pygame.font.Font(None, fsize)
    th = three.render('3', True, (0,0,0))

    four = pygame.font.Font(None, fsize)
    fo = four.render('4', True, (0,0,0))

    five = pygame.font.Font(None, fsize)
    fi = five.render('5', True, (0,0,0))
    nums = [o, to, th, fo, fi]

    holes(hole)
    for i in range(0,5):
        scrn.blit(nums[i], (i*100 + 25, 350 - 100*(i%2)))

    pygame.display.flip()
    pygame.time.wait(4000)
    pygame.event.clear()

    t = pygame.time.get_ticks()
    
    str_points = pygame.font.SysFont(None, 80)
    point_img = str_points.render('Score' + '  ' + '0', True, (0,0,0))
    scrn.blit(point_img, (300, 20))

    #Game
    while (status):

        h = random.randint(1,5)
        peek(hole, frogpeek, frogpop, h)
        
        pygame.time.wait(100)
        t = pygame.time.get_ticks()
        t_status = True
        pygame.event.clear()
        while(pygame.time.get_ticks() - t <= d and t_status):
            event = pygame.event.poll()
            if event.type == QUIT:
                    pygame.quit()
                    quit()
            elif event.type == KEYDOWN and event.key in keys:
                t_status = False
                if event.key != keys[h - 1]:
                    leave(hole,frogpeek, h)
                    wrong = wrong + 1
                else:
                    explode(hole, boom1, boom2, h)
                    points = points + 1
        
        if pygame.time.get_ticks() - t > d :
            leave(hole, frogpeek, h)
            wrong = wrong + 1

        holes(hole)

        st = ''
        for i in range(0, wrong):
            st = st + 'X   '
        scrn.fill((207, 184, 128), (0, 0, scrn.get_width(), 100))
        fal = pygame.font.SysFont(None, 80)
        fal_img = fal.render(st, True, (252, 3, 3))
        scrn.blit(fal_img, (50, 20))

        str_points = pygame.font.SysFont(None, 80)
        point_img = str_points.render('Score' + '  ' + str(points), True, (0,0,0))
        scrn.blit(point_img, (300, 20))
        pygame.display.flip()


        pygame.time.wait(d)

        if d > 300:
            d = d - 30

        if wrong > 2:
            break
        

    #end game screen, give choice to restart
    end_status = True
    scrn.fill((207, 184, 128))
    fsize = 70
    one = pygame.font.FontType(None, fsize)
    o = one.render('Play again?', True, (0,0,0))

    two = pygame.font.Font(None, fsize)
    to = two.render('[1] YES', True, (0,0,0))

    three = pygame.font.Font(None, fsize)
    th = three.render('[2] NO', True, (0,0,0))

    four = pygame.font.Font(None, fsize)
    fo = three.render('Final Score' + '   ' + str(points), True, (0,0,0))
    
    scrn.blit(fo, (150, 100))
    scrn.blit(o, (175, 220))
    scrn.blit(to, (125, 300))
    scrn.blit(th, (325, 300))

    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.event.clear(pygame.KEYDOWN)

    while(end_status):
        event = pygame.event.wait()

        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_1:
                break
            elif event.key == pygame.K_2:
                pygame.quit()
                quit()

