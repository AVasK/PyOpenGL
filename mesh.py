import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from random import random

from OpenGL.GLUT import *


def safe_avg(grid, size, x, y):
    sum = 0
    #print("in avg: ", x, y, size)
    for tx in (x - size//2, x + size//2):
        ty = y
        #print('t ', tx, ty) #####
        if (ty <= 0 or ty >= N):
            sum += 0
        elif (tx <= 0 or tx >= N):
            sum += 0
        else:
            sum += grid[tx][ty][2]
                
    for ty in (y - size//2, y + size//2):
        tx = x
        #print('t ', tx, ty) #####
        if (ty <= 0 or ty >= N):
            sum += 0
        elif (tx <= 0 or tx >= N):
            sum += 0
        else:
            sum += grid[tx][ty][2]
                
    return sum/4
    
def Diamond_Square(grid, x, y, N):
    print("x, y ", x,y) ####
    if N < 1:
        print('outta')
        return
    # diamond:
    grid[N//2 + x][N//2 + y][2] = (grid[x][y][2] + grid[x][N+y][2] + grid[N+x][y][2] + grid[N+x][N+y][2])/4 + (random() - 0.0)*roughness
    # square:
    grid[N//2 + x][y][2] = safe_avg(grid, N, N//2 + x, y)
    grid[x][N//2 + y][2] = safe_avg(grid, N, x, N//2 + y)
    grid[N//2 + x][N + y][2] = safe_avg(grid, N, N//2 + x, N + y)
    grid[N + x][N//2 + y][2] = safe_avg(grid, N, N + x, N//2 + y)
    
    Diamond_Square(grid, x, y, N//2)
    Diamond_Square(grid, x, N//2+y, N//2)
    Diamond_Square(grid, N//2 + x, y, N//2)
    Diamond_Square(grid, N//2 + x, N//2+y, N//2)


#N = 5
N = 17
size = 2
faces_draw = False
roughness = 1

vertex_grid = [[[0,0,0] for x in range(N)] for x in range(N)]

for i in (0, N-1):
    for j in (0, N-1):
        vertex_grid[i][j][2] = random() * roughness
        
        
for i in range(0, N):
    for j in range(0, N):
        vertex_grid[i][j] = [size * i, size * j, vertex_grid[i][j][-1]]
#vertex_grid = [[[-1,-1, 0], [-1, 1, 0]], [[1, -1, 0], [1, 1, 0]]]

Diamond_Square(vertex_grid, 0, 0, N-1)

for i in range(0, N):
    for j in range(0, N):
        print(vertex_grid[i][j], end = ' ')
    print()



    

def Plane():
    '''
    # Drawing faces
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv(list(x * num for x in colors[0]))
        #glColor3fv(colors[num])
        for vertex in surface:
            glVertex3fv(list(x * size for x in list((vertices[vertex]))))
    glEnd()
    '''
    if faces_draw:
        # Drawing faces
        glBegin(GL_QUADS)
    
        glColor3fv((1,1,1))
    
        for i in range(N-1):
            for j in range(N-1):
                glVertex3fv((vertex_grid[i][j]))
                glVertex3fv((vertex_grid[i+1][j]))
                glVertex3fv((vertex_grid[i+1][j]))
                glVertex3fv((vertex_grid[i+1][j+1]))
                glVertex3fv((vertex_grid[i+1][j+1]))
                glVertex3fv((vertex_grid[i][j]))
            
                glVertex3fv((vertex_grid[i][j]))
                glVertex3fv((vertex_grid[i][j+1]))
                glVertex3fv((vertex_grid[i][j+1]))
                glVertex3fv((vertex_grid[i+1][j+1]))
                glVertex3fv((vertex_grid[i+1][j+1]))
                glVertex3fv((vertex_grid[i][j]))      
        glEnd()
    
    # Drawing edges
    glBegin(GL_LINES)
    
    glColor3fv((1,1,1))
    
    for i in range(N-1):
        for j in range(N-1):
            glVertex3fv((vertex_grid[i][j]))
            glVertex3fv((vertex_grid[i+1][j]))
            glVertex3fv((vertex_grid[i+1][j]))
            glVertex3fv((vertex_grid[i+1][j+1]))
            glVertex3fv((vertex_grid[i+1][j+1]))
            glVertex3fv((vertex_grid[i][j]))
            
            glVertex3fv((vertex_grid[i][j]))
            glVertex3fv((vertex_grid[i][j+1]))
            glVertex3fv((vertex_grid[i][j+1]))
            glVertex3fv((vertex_grid[i+1][j+1]))
            glVertex3fv((vertex_grid[i+1][j+1]))
            glVertex3fv((vertex_grid[i][j]))
            
            
            
    glEnd()
    
def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    fov = 45
    gluPerspective(fov, (display[0]/display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -40)
    glRotatef(0, 0, 0, 0)
    
    while True:
        # Tracking down in-app events like quitting or keypresses:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            '''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Doesnt work :C")
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_RIGTH:
                    glTranslatef(1, 0, 0)
            '''
            if event.type == pygame.KEYDOWN:
                if event.key == K_TAB:
                    glTranslatef(0, 0, 0.1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    glTranslatef(0, 0, -0.1)
               
        glRotatef(1, 3, 1, 1) # cube's rotation set.
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Plane()
        pygame.display.flip()
        pygame.time.wait(5)

        
main()
        
    
    
    
    
    
    
    
    
    
    
    
    