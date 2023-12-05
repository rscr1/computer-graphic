import pygame
import sys
import numpy as np

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bezier Curve")

def bezier_curve(p0, p1, p2, p3, t):
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3

points = np.array([(100, 300), (300, 100), (500, 500), (700, 300)], dtype=float)

selected_point = None
dragging = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, point in enumerate(points):
                if pygame.Rect(point[0] - 5, point[1] - 5, 10, 10).collidepoint(event.pos):
                    selected_point = i
                    dragging = True
                    break
        elif event.type == pygame.MOUSEMOTION:
            if dragging and selected_point is not None:
                points[selected_point] = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    screen.fill(WHITE)

    for point in points:
        pygame.draw.circle(screen, BLACK, (int(point[0]), int(point[1])), 5)

    pygame.draw.lines(screen, RED, False, [bezier_curve(*points[i:i+4], t/100) for i in range(len(points)-3) for t in range(101)], 2)

    pygame.display.flip()
