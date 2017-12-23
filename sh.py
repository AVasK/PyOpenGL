# Shaders testing on a simple triangle...

from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random

global pointcolor 

## Shader procedure:
def create_shader(shader_type, source):
    # Creating empty shader object:
    shader = glCreateShader(shader_type)
    # Binding shader code to empty shader object:
    glShaderSource(shader, source)
    # Compiling shader:
    glCompileShader(shader)
    return shader

## KeyListener:
def specialkeys(key, x, y):
    global pointcolor
    if key == GLUT_KEY_UP:
        glRotatef(5, 1, 0, 0)
    if key == GLUT_KEY_DOWN:
        glRotatef(5, -1, 0, 0)
    if key == GLUT_KEY_LEFT:
        glRotatef(5, 0, 1, 0)
    if key == GLUT_KEY_RIGHT:
        glRotatef(5, 0, -1, 0)
    if key == GLUT_KEY_END:
        pointcolor = [[random(), random(), random()],
                      [random(), random(), random()],
                      [random(), random(), random()]]
        
## Drawing procedure:
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    glColorPointer(3, GL_FLOAT, 0, pointcolor)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glDisableClientState(GL_VERTEX_ARRAY) 
    glDisableClientState(GL_COLOR_ARRAY) 
    glutSwapBuffers()
        


# initializing display
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
#glutInitWindowPosition(50, 50)
glutInit(sys.argv)
# Binding procedures:
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialkeys)
#setting gray color for a clear screen
glClearColor(0.2, 0.2, 0.2, 1)
        
        
# Creating vertex shader
vertex = create_shader(GL_VERTEX_SHADER, """
varying vec4 vertex_color;
            void main(){
                gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                vertex_color = gl_Color;
            }""")

# Creating fragment shader:
# Each fragment has a mixed color of its vertices:
fragment = create_shader(GL_FRAGMENT_SHADER, """
varying vec4 vertex_color;
            void main() {
                gl_FragColor = vertex_color;
}""")

# Creating shader program:
program = glCreateProgram()
# Linking shaders to the program
glAttachShader(program, vertex)
glAttachShader(program, fragment)
# Linking the program:
glLinkProgram(program)

pointdata = [[0, 0.5, 0], [-0.5, -0.5, 0], [0.5, -0.5, 0]]
pointcolor = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]

glutMainLoop()













