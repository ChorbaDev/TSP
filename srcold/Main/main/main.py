import pygame
import time
import random
import os

from Points import Point

os.environ["SDL_VIDEO_CENTRED"]='1'
width,height=1000,1000
#colors
black=(0,0,0)
white=(255,255,255)
green=(0,255,24)

#pygame settings
pygame.init()
pygame.display.set_caption("Traveling Sales Algorithm")
screen=pygame.display.set_mode((width,height))


#variables
points=[]
offset_screen=50
smallest_path=[]
record_distance=0
number_of_point=5

#Generate random points on screen
for n in range(number_of_point):
    x=random.randint(offset_screen,width-offset_screen)
    y=random.randint(offset_screen,height-offset_screen)

    point=Point(x,y)
    points.append(point)
#shuffle points in the list

def shuffle(a,b,c):
        temp=a[b];
        a[b]=a[c]
        a[c]=temp

#Distance between point using pythagore theorem
def calculate_distance(point_list):
    total=0
    for n in range(len(points)-1):
        distance=((points[n].x-points[n+1].x)**2+(points[n].y-points[n+1].y)**2)**0.5
        total+=distance
    return total

dist=calculate_distance(points)
record_distance=dist

smallest_path=points.copy()

run = False

while run:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for n in range(len(points)):
        pygame.draw.circle(screen,white,(points[n].x,points[n].y),10)
    a=random.randint(0,len(points)-1)
    b=random.randint(0,len(points)-1)
    shuffle(points,a,b)
    dist=calculate_distance(points)
    if dist < record_distance:
        record_distance=dist
        smallest_path=points.copy()

    for m in range(len(points)-1):
        pygame.draw.line(screen,white,(points[m].x,points[m].y),(points[m+1].x,points[m+1].y),2)
    for m in range(len(smallest_path)-1):
        pygame.draw.line(screen,green,(smallest_path[m].x,smallest_path[m].y),(smallest_path[m+1].x,smallest_path[m+1].y),4)
    pygame.display.update()

print("the smallest distance is :", record_distance)
pygame.quit()
