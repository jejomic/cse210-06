import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.rock import Rock
from game.casting.asteroid import Asteroid

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Gravitational pull simulation"
WHITE = Color(255, 255, 255)
DEFAULT_rockS = 2000


def main():

    # create the cast
    cast = Cast()


    # create huge asteroid
    asteroid = Actor()
    asteroid.set_text("*")
    asteroid.set_font_size(FONT_SIZE)
    asteroid.set_color(Color(150, 75, 0))
    asteroid.set_position(Point(random.randint(
        200, 800), random.randint(100, 500)))
    asteroid.set_velocity(Point(1, 1))
    cast.add_actor("asteroids", asteroid)

    # create rocks
    for n in range(DEFAULT_rockS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

      
        color = Color( 150, 75, 0)

        rock = Rock()
        rock.set_text(".")
        rock.set_font_size(random.randint(15,20))
        rock.set_color(color)
        rock.set_position(position)
        rock.set_velocity(Point(random.randint(-1, 1), random.randint(-1, 1)))

        cast.add_actor("rocks", rock)

    

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
