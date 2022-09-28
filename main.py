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

class Ship:
  def __init__(self, x, y, health = 100):
    self.x = x
    self.y = y
    self.health = health
    self.ship_image = None
    self.laser_img = None
    self.lasers = []
    self.cool_down_counter = 0

  def draw(self, window):
    pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50), 0)

def main():
  run = True
  FPS = 60
  level = 1
  lives = 5
  player_vel = 5
  main_font = pygame.font.SysFont("comicsans", 50)

  ship = Ship(300, 650)

  clock = pygame.time.Clock()
  
  def redraw_window():
    WIN.blit(BG, (0, 0))
    # draw text
    lives_label = main_font.render("Lives: " + str(lives), 1, (255, 255, 255))
    level_label = main_font.render("Level: " + str(level), 1, (255, 255, 255))

    WIN.blit(lives_label, (10, 10))
    WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

    ship.draw(WIN)

    pygame.display.update()

  while run:
    clock.tick(FPS)
    redraw_window()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and ship.x - player_vel > 0:
      ship.x -= player_vel
    if keys[pygame.K_d] and ship.x + player_vel + 50 < WIDTH:
      ship.x += player_vel
    if keys[pygame.K_w] and ship.y > 0:
      ship.y -= player_vel
    if keys[pygame.K_s] and ship.y + player_vel + 50 < HEIGHT:
      ship.y += player_vel

main()