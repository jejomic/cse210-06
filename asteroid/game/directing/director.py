from game.shared.point import Point
import random

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.

    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        # robot = cast.get_first_actor("robots")
        # velocity = self._keyboard_service.get_direction()
        # robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with rocks or asteroids.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        # robot = cast.get_first_actor("robots")
        asteroid = cast.get_first_actor("asteroids")

        rocks = cast.get_actors("rocks")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        # robot.move_next(max_x, max_y)
        asteroid.move_next(max_x, max_y)
        
        #asteroid movement
        rx = asteroid.get_position().get_x()
        ry = asteroid.get_position().get_y()
        
        if rx > 800:
            asteroid.set_velocity(asteroid.get_velocity().setx(-1))
        if rx < 100:
            asteroid.set_velocity(asteroid.get_velocity().setx(1))
        if ry >550:
            asteroid.set_velocity(asteroid.get_velocity().sety(-1))
        if ry <50:
            asteroid.set_velocity(asteroid.get_velocity().sety(1))
        
        
        # checks for physics
        for rock in rocks:
            
            gx = rock.get_position().get_x()
            gy = rock.get_position().get_y()
            
            rx = range(asteroid.get_position().get_x()-200,asteroid.get_position().get_x()+200)
            ry = range(asteroid.get_position().get_y()-200,asteroid.get_position().get_y()+200)
            
            if gx in rx and gy in ry:
                
                
                if rock.get_position().get_x() > asteroid.get_position().get_x():
                    rock.set_velocity(rock.get_velocity().setx(-20))
                    # rock.set_velocity(rock.get_velocity().add(Point(-3, 0)))
                if rock.get_position().get_x() < asteroid.get_position().get_x():
                    rock.set_velocity(rock.get_velocity().setx(20))
                    # rock.set_velocity(rock.get_velocity().add(Point(3, 0)))

                if rock.get_position().get_y() > asteroid.get_position().get_y():
                    rock.set_velocity(rock.get_velocity().sety(-20))
                    # rock.set_velocity(rock.get_velocity().add(Point(0, -3)))
                if rock.get_position().get_y() < asteroid.get_position().get_y():
                    rock.set_velocity(rock.get_velocity().sety(20))
                    # rock.set_velocity(rock.get_velocity().add(Point(0, 3)))
                    
                if rock.get_position().get_x() == asteroid.get_position().get_x():
                    rock.set_velocity(rock.get_velocity().setx(0))
                if rock.get_position().get_y() == asteroid.get_position().get_y():
                    rock.set_velocity(rock.get_velocity().sety(0))

            rock.move_next(900, 600)
            
            # if rock.get_position().equals(asteroid.get_position()):
            #     # asteroid.set_font_size(asteroid.get_font_size()+1)
            #     # asteroid.get_position().add(Point(10,0))
            #     cast.remove_actor("rocks", rock)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
