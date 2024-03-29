import pygame
from time import localtime as now 
pygame.init()
minute = second = 0

def get_time():
    global minute, second
    minute, second = now().tm_min, now().tm_sec
get_time()

screen_h = 675
screen_w = 900
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Mouse')


img_main = pygame.image.load('lab7/IMG_6054.JPG')
img_main = pygame.transform.scale(img_main, (screen_w, screen_h))
img_left = pygame.image.load('lab7/IMG_6056.PNG')
img_left = pygame.transform.scale(img_left, (45, screen_h))
img_right = pygame.image.load('lab7/IMG_6053.PNG')
img_right = pygame.transform.scale(img_right, (screen_w, screen_h))

def print_img_by_degree(image, degree):
    image = pygame.transform.rotate(image, degree) 
    rect = image.get_rect() 
    rect.center = win.get_rect().center 
    win.blit(image, rect) 

def print_time():
    font = pygame.font.Font('mouse\\Alice-Regular.ttf', 40)
    text = font.render(f'{minute//10}{minute%10}:{second//10}{second%10}', True, (169, 169, 169))
    win.blit(text, (screen_w-100, screen_h-50))

def play_tick():
    music = pygame.mixer.music.load('lab7/JPEG image-4591-9ECA-58-0.jpeg')
    pygame.mixer.music.play()
play_tick()

clock = pygame.time.Clock()
run = 1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = 0
    win.blit(img_main, (0, 0))
    get_time()
    if not pygame.mixer.music.get_busy(): play_tick() # unnecessary
    print_img_by_degree(img_left, -second*6 - (0.7 if second>30 else +1.2)) #-0.7/-1.2 used to normalize line
    print_img_by_degree(img_right, -minute*6 -40) #-40 used to normalize line
    
    print_time()
    pygame.display.update()
    clock.tick(60)