import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def scaled_figure(draw_function, *args, scale_x:float = 1, scale_y:float = 1, scale_z:float = 1):
    """
    Function for scale figure

    Args: 
        - draw_function: functions, that draw the figure
        - args: arguments for `draw_function`
        - scale_x: scale size on the X axis
        - scale_y: scale size on the Y axis
        - scale_z: scale size on the Z axis
    """
    
    glPushMatrix()
    glScalef(scale_x, scale_y, scale_z)
    draw_function(*args)
    glPopMatrix()

def draw_half_sphere(radius: float, slices: int, stacks: int) -> None:
    """
    Function for drawing a half sphere with a base

    Args: 
        - radius: radius of the sphere
        - slices: the number of subdivisions around the z-axis
        - stacks: the number of subdivisions along the z-axis
    """

    phi_step = 2.0 * math.pi / slices
    theta_step = math.pi / stacks

    for i in range(stacks // 2 + 1):
        theta1 = i * theta_step
        theta2 = (i + 1) * theta_step

        glBegin(GL_TRIANGLE_STRIP)
        for j in range(slices + 1):
            phi = j * phi_step

            x = radius * math.sin(theta1) * math.cos(phi)
            y = radius * math.sin(theta1) * math.sin(phi)
            z = radius * math.cos(theta1)

            glVertex3f(x, y, z)

            x = radius * math.sin(theta2) * math.cos(phi)
            y = radius * math.sin(theta2) * math.sin(phi)
            z = radius * math.cos(theta2)

            glVertex3f(x, y, z)
        glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)  

    for j in range(slices + 1):
        phi = j * phi_step

        x = radius * math.cos(phi)
        y = radius * math.sin(phi)

        glVertex3f(x, y, 0)

    glEnd()

def main():  
    pygame.init()
    display = (1280, 720)  
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    reflect = 0.0
    time = 0.

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glLightfv(GL_LIGHT0, GL_POSITION, [3, 3, -15, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 1.0, 1.0, 1.0])
    glEnable(GL_LIGHT0)

    glMaterial(GL_FRONT, GL_DIFFUSE, [0.11, 0.9, 0.1, 1.0])
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        time += 0.01
        
        red = (math.sin(time) + 1) / 2
        green = (math.sin(time + math.pi / 2) + 1) / 2
        blue = (math.sin(time + math.pi) + 1) / 2

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [red, green, blue, reflect])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [red, green, blue, reflect])

        glRotatef(1, 0, 1, 0)  # Вращение относительно оси OY
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        scaled_figure(draw_half_sphere, 1, 36, 36)
        pygame.display.flip()
        pygame.time.wait(50)

if __name__ == "__main__":
    main()
