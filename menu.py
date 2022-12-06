import pygame
import sys
from game import continue_game
from game import load_game
from game import new_game
from game import quit_game

def render_menu_options(screen, options, selected_option):
  """Renders the menu options on the screen.

  Args:
    screen: The screen surface to draw on.
    options: A list of strings representing the menu options.
    selected_option: The index of the selected option in the options list.
  """

  font = pygame.font.SysFont("Arial", 24)

  x_pos = 200
  y_pos = 200
  spacing = 50

  # render menu options
  y_pos = 200
  for i, option in enumerate(options):
    color = (255, 255, 255)  # default color
    if i == selected_option:
      # highlight selected option
      color = (255, 0, 0)
    text = font.render(option, True, color)
    screen.blit(text, (x_pos, y_pos))
    y_pos += spacing
  pygame.display.update()


def show_menu(screen):
  """Displays the main menu on the screen and handles user input.

  Args:
    screen: The screen surface to draw on.
  """

  # load background image
  background_image = pygame.image.load("DALL-E_2022-12-06_09.35.12-Background_photograph_a_realistic_forest.png")
  background_image = pygame.transform.scale(background_image, screen.get_size())
  screen.blit(background_image, (0, 0))

  # create menu options
  options = ["Continue", "Load game", "New game", "Quit"]

  # initialize selected option
  selected_option = 0

  # render menu options
  render_menu_options(screen, options, selected_option)

  # handle user input
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          # move selection up
          selected_option = (selected_option - 1) % len(options)

          # re-render menu options
          render_menu_options(screen, options, selected_option)

        elif event.key == pygame.K_DOWN:
          # move selection down
          selected_option = (selected_option + 1) % len(options)

          # re-render menu options
          render_menu_options(screen, options, selected_option)

        elif event.key == pygame.K_RETURN:
          # handle menu option selection
          if options[selected_option] == "Continue":
            continue_game(screen)
          elif options[selected_option] == "Load game":
            load_game(screen)
          elif options[selected_option] == "New game":
            new_game(screen)
          elif options[selected_option] == "Quit":
            quit_game()
            pygame.quit()
            sys.exit()
