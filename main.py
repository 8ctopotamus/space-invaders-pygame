from turtle import width
import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
REDS_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

BG = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
  run = True
  FPS = 60
  clock = pygame.time.Clock()
  
  def redraw_window():
    WIN.blit(BG, (0, 0))
    pygame.display.update()

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      redraw_window()
      if event.type == pygame.QUIT:
        run = False

main()