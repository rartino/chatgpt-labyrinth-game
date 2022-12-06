import pygame
from menu import show_menu

def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption("2D Adventure Game")

  # show game menu and start game
  show_menu(screen)

  pygame.quit()

if __name__ == "__main__":
  main()
