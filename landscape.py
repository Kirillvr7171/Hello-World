import pygame
import math
import random


pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Initialize Variables

skynight = (25,25,212)
skyeblue = (135, 206, 235)
water = (0, 105, 148)
deep_water = (0, 75, 110)
sun_colour = (255, 223, 0)
brown = (139, 69, 19)
white = (240, 240, 240)
cloudwhite = (255, 255, 255)
cx = 0
sun_x = 0 
sun_speed = 2

x = 0
boat_x = -150
water_offset = 0
sun_radius = 40
growth = True
frame_count = 0
sux_x = 0

sun_colour = 255 
# need to change the sun colour, to 
# GAMESTATE UPDATES

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cx > 500:
        cx = 0
    
    frame_count += 1
    boat_x += 2

    bob = math.sin(frame_count * 0.04) * 7
    
    if boat_x > WIDTH:
        boat_x = -200
    
    water_offset = (water_offset + 1) % 100
# SUN movement
    if growth:
        sun_radius += 0.1
        if sun_radius > 50:
            growth = False
    else:
        sun_radius += -0.1
        if sun_radius < 40:
            growth = True
# SUN COLOUR 
    sun_colour += -1
    if sun_colour < 0:
        sun_colour = 255
    
    sun_x += sun_speed
    if sun_x > WIDTH + 50:
        sun_x = -50 
# Screen Hue Change
    frame_count += 1
    thecycle = (math.sin(frame_count * 0.01) + 1) / 2     
    sky_r = int(10 + (125) * thecycle)
    sky_g = int(10 + (196) * thecycle)
    sky_b = int(40 + (195) * thecycle)
    current_sky = (sky_r, sky_g, sky_b)

    screen.fill(current_sky)
    cx += 3
    if thecycle < 0.3:
        pygame.draw.circle(screen, white, (550, 60), int(sun_radius))
        pygame.draw.circle(screen, (128, 128, 128), (540, 50), 6)
        pygame.draw.circle(screen, (128, 128, 128), (565, 70), 8)
        pygame.draw.circle(screen, (128, 128, 128), (550, 80), 4)
    else:
        pygame.draw.circle(screen, (255, 223, 0), (550, 60), int(sun_radius))
# Cloud move
    for cloud_x in range(-68, WIDTH + 200, 500):
        y = 100
        pygame.draw.circle(screen, cloudwhite, (cloud_x + cx, y), 30)
        pygame.draw.circle(screen, cloudwhite, (cloud_x + 25 + cx, y - 10), 35)
        pygame.draw.circle(screen, cloudwhite, (cloud_x + 50 + cx, y), 30)
 
    for kirill in range(-100, WIDTH + 100, 100):
        pygame.draw.ellipse(screen, water, (kirill - water_offset, 440, 120, 80))

    boat_y = 440 + bob
    pygame.draw.rect(screen, brown, (boat_x, boat_y, 120, 30))
    pygame.draw.polygon(screen, brown, [(boat_x, boat_y), (boat_x - 30, boat_y), (boat_x, boat_y + 30)])
    pygame.draw.polygon(screen, brown, [(boat_x + 120, boat_y), (boat_x + 150, boat_y), (boat_x + 120, boat_y + 30)])
    pygame.draw.line(screen, (50, 50, 50), (boat_x + 40, boat_y), (boat_x + 40, boat_y - 100), 4)
    pygame.draw.polygon(screen, white, [(boat_x + 45, boat_y - 90), (boat_x + 100, boat_y - 20), (boat_x + 45, boat_y - 20)])

    for i in range(-100, WIDTH + 100, 100):
        wavex = i + water_offset
        pygame.draw.ellipse(screen, water, (wavex, 460, 120, 60))
        pygame.draw.arc(screen, white, (wavex + 30, 465, 60, 20), 0, 3.14, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
