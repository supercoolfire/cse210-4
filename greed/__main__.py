import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.gem import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

# FRAME_RATE = 12
FRAME_RATE = 20
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greedy Rocks Paper Stones"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 60
DEFAULT_GEMS = 20
GEM_VALUE = 0


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the prompt
    prompt = Actor()
    prompt.set_text("")
    prompt.set_font_size(FONT_SIZE * 2)
    prompt.set_color(WHITE)
    prompt.set_position(Point(int(MAX_X / 2 - 150), int(MAX_Y / 2 + 80)))
    cast.add_actor("prompts", prompt)

    # create the robot
    x = int(MAX_X / 2)
    # y = int(MAX_Y / 2)
    y = int(15 * 35)
    # input(f'why? {y}')
    # y = int(550)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        # text = chr(random.randint(33, 126))
        text = chr(random.randint(65, 90))
        message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # r = random.randint(0, 255)
        r = 255
        g = random.randint(0, 255)
        # b = random.randint(0, 255)
        b = 0
        color = Color(r, g, b)

        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        artifact.set_getstone_value()
        cast.add_actor("artifacts", artifact)

        # create the gems
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_GEMS):
        # text = chr(random.randint(33, 126))
        text = chr(random.randint(97, 122))
        message = messages[n]

        x = random.randint(1, COLS - 0)
        y = random.randint(1, ROWS - 0)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(170, 255)
        color = Color(r, g, b)

        gem = Gem()
        gem.set_text(text)
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_message(message)
        gem.set_gem_value()
        cast.add_actor("gems", gem)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
