import pygame
import sys

# global declarations
BLOCK_SIZE = 20

# map data
map_data = []

# position of guy
guy_x = 0
guy_y = 0

# position of camera
camera_x = 0
camera_y = 0

action = None

def initialize_game():
  """Initializes the game by loading the map data and setting the initial positions for the guy and camera."""
  global map_data, guy_x, guy_y, camera_x, camera_y

  # load map data from file
  with open("map.txt", "r") as f:
    map_data = [list(line.strip()) for line in f]

  # initialize position of guy
  guy_x = 20
  guy_y = 20

  # initialize camera position
  camera_x = guy_x
  camera_y = guy_y

def user_input():
  """Handles user input."""
  global guy_x, guy_y, action

  pygame.event.get()
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    # check if guy is trying to move into a wall
    if map_data[guy_y][guy_x - 1] != "#":
      # move guy left
      guy_x -= 1
  elif keys[pygame.K_RIGHT]:
    # check if guy is trying to move into a wall
    if map_data[guy_y][guy_x + 1] != "#":
      # move guy right
      guy_x += 1
      # check if guy is trying to move off the map
      if guy_x > len(map_data[0]) - 1:
        # prevent guy from moving off the map
        guy_x = len(map_data[0]) - 1
  elif keys[pygame.K_UP]:
    # check if guy is trying to move into a wall
    if map_data[guy_y - 1][guy_x] != "#":
      # move guy up
      guy_y -= 1
  elif keys[pygame.K_DOWN]:
    # check if guy is trying to move into a wall
    if map_data[guy_y + 1][guy_x] != "#":
      # move guy down
      guy_y += 1
      # check if guy is trying to move off the map
      if guy_y > len(map_data) - 1:
        # prevent guy from moving off the map
        guy_y = len(map_data) - 1
  elif keys[pygame.K_ESCAPE]:
    # set action flag to quit
    action = "quit"


def handle_camera(screen, screen_width, screen_height):
  global camera_x, camera_y

  # check if guy is close to the edge of the screen
  if guy_x < camera_x + 10:
    # guy is close to left edge, scroll map left
    camera_x = max(0, camera_x - 1)
  elif guy_x > camera_x + screen_width - 10:
    # guy is close to right edge, scroll map right
    camera_x = min(len(map_data[0]) - screen_width, camera_x + 1)
  if guy_y < camera_y + 10:
    # guy is close to top edge, scroll map up
    camera_y = max(0, camera_y - 1)
  elif guy_y > camera_y + screen_height - 10:
    # guy is close to bottom edge, scroll map down
    camera_y = min(len(map_data) - screen_height, camera_y + 1)

def render_map(screen, screen_width, screen_height):

  # render visible part of map
  for i, row in enumerate(map_data):
    for j, col in enumerate(row):
      if i >= camera_y and i < camera_y + screen.get_height() and j >= camera_x and j < camera_x + screen_width:
        if col == "#":
          # render wall block
          pygame.draw.rect(screen, (0, 0, 255), (j * BLOCK_SIZE - camera_x * BLOCK_SIZE, i * BLOCK_SIZE - camera_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        elif col == " ":
          # render empty space
          pygame.draw.rect(screen, (255, 255, 255), (j * BLOCK_SIZE - camera_x * BLOCK_SIZE, i * BLOCK_SIZE - camera_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def game_loop(screen):
  """Main game loop that handles user input and draws the game on the screen.

  Args:
    screen: The screen surface to draw on.
  """
  global action, camera_x, camera_y

  # initialize game
  initialize_game()

  # create clock object to control game speed
  clock = pygame.time.Clock()

  # calculate screen dimensions in blocks
  screen_width = screen.get_width() // BLOCK_SIZE
  screen_height = screen.get_height() // BLOCK_SIZE

  # main game loop
  while True:
    # handle user input events
    user_input()

    # check action flag
    if action == "quit":
      # quit game
      quit_game()

    # handle camera
    handle_camera(screen, screen_width, screen_height)

    # render map
    render_map(screen, screen_width, screen_height)

    # render guy
    pygame.draw.rect(screen, (255, 0, 0), (guy_x * BLOCK_SIZE - camera_x * BLOCK_SIZE, guy_y * BLOCK_SIZE - camera_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # update screen
    pygame.display.update()

    # delay to control game speed
    clock.tick(10)

def new_game(screen):
  """Starts a new game.

  Args:
    screen: The screen surface to draw on.
  """
  # initialize game
  initialize_game()

  # start game loop
  game_loop(screen)

def continue_game():
    pass

def load_game():
    pass

def quit_game():
    """Quits the game."""
    pygame.quit()
    sys.exit()
