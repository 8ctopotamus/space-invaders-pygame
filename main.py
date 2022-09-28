import pygame
import os
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 800, 750
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

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
  run = True
  FPS = 60
  level = 1
  lives = 5
  main_font = pygame.font.SysFont("comicsans", 50)

  clock = pygame.time.Clock()
  
  def redraw_window():
    WIN.blit(BG, (0, 0))
    # draw text
    lives_label = main_font.render("Lives: " + str(lives), 1, (255, 255, 255))
    level_label = main_font.render("Level: " + str(level), 1, (255, 255, 255))

    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

    pygame.display.update()

  while run:
    clock.tick(FPS)
    redraw_window()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

main()