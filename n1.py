import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from random import random

N_CUBES = 20

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = []
for x in range(N_CUBES + 1):
    colors.append((random(), random(), random()))


def Cube(size, num):
    # Drawing faces
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv(list(x * num for x in colors[0]))
        #glColor3fv(colors[num])
        for vertex in surface:
            glVertex3fv(list(x * size for x in list((vertices[vertex]))))
    glEnd()
    
    # Drawing edges
    glBegin(GL_LINES)
    
    #glColor3fv((1,1,1))
    glColor3fv(list(x * num for x in colors[0]))
    if num == 1:
        glColor3fv((0,0,0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(list(x * size for x in list((vertices[vertex]))))
            
    glEnd()
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    fov = 45
    gluPerspective(fov, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 0.1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    glTranslatef(0, 0, -0.1)
               
        glRotatef(1, 3, 1, 1) # cube's rotation set.
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for x in range(1, N_CUBES + 1):
            Cube(1/x, x - 1)
        pygame.display.flip()
        pygame.time.wait(5)

        
main()
        
    
    
    
    
    
    
    
    
    
    
    
    