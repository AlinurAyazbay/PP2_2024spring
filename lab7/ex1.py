import pygame
import sys
from datetime import datetime
pygame.init()
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load('lab7/JPEG image-4591-9ECA-58-0.jpeg')
mickey_rect = mickey_image.get_rect(center=(window_width // 2, window_height // 2))

clock_center = (window_width // 2, window_height // 2)
minute_length = 100
second_length = 150
hour_length = 80

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    current_time = datetime.now().time()
    hours = current_time.hour
    minutes = current_time.minute
    seconds = current_time.second

    window.blit(mickey_image, mickey_rect)

    minute_angle = (minutes / 60) * 360 - 90
    minute_hand_end = (clock_center[0] + minute_length * pygame.math.Vector2().from_polar((1, minute_angle)),
                       clock_center[1])
    pygame.draw.line(window, (0, 0, 0), clock_center, minute_hand_end, 5)

    second_angle = (seconds / 60) * 360 - 90
    second_hand_end = (clock_center[0] + second_length * pygame.math.Vector2().from_polar((1, second_angle)),
                       clock_center[1])
    pygame.draw.line(window, (255, 0, 0), clock_center, second_hand_end, 2)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
