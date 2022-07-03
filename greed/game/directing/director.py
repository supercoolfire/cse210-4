from game.shared.point import Point

from game.casting.artifact import Artifact
from game.casting.gem import Gem

from game.shared.color import Color
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
        self._score = 0

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
        robot = cast.get_first_actor("robots")
        # print(F'director velocity: {velocity}')

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        prompt = cast.get_first_actor("prompts")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        gems = cast.get_actors("gems")
        # gem.set_position(position)

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        banner.set_text(f'Score: {self._score}')

        for artifact in artifacts:
            if self._score < -1 or len(gems) == 0:
                artifact.move_next(max_x, max_y)
                pass
            else:
                artifact.move_next(max_x, max_y)
            if robot.get_position().equals(artifact.get_position()):
                cast.remove_actor("artifacts", artifact)
                self._score -= artifact.get_getstone_value()

                text = chr(random.randint(65, 90))

                x = random.randint(1, 60 - 1)
                y = random.randint(1, 40 - 20)
                position = Point(x, y)
                position = position.scale(15)

                # r = random.randint(0, 255)
                r = 255
                g = random.randint(0, 255)
                # b = random.randint(0, 255)
                b = 0
                color = Color(r, g, b)

                artifact = Artifact()
                artifact.set_text(text)
                artifact.set_font_size(15)
                artifact.set_color(color)
                artifact.set_position(position)
                artifact.set_getstone_value()
                cast.add_actor("artifacts", artifact)

        for gem in gems:
            if self._score >= 0:
                gem.move_next(max_x, max_y)
            else:
                gem.move_next(max_x, max_y)
                pass
            if robot.get_position().equals(gem.get_position()):
                cast.remove_actor("gems", gem)
                self._score += gem.get_gem_value()

                text = chr(random.randint(97, 122))
                x = random.randint(1, 60 - 1)
                y = random.randint(1, 40 - 20)
                position = Point(x, y)
                position = position.scale(15)
                r = random.randint(0, 100)
                g = random.randint(0, 100)
                b = random.randint(170, 255)
                color = Color(r, g, b)
                gem = Gem()
                gem.set_text(text)
                gem.set_font_size(15)
                gem.set_color(color)
                gem.set_position(position)
                gem.set_gem_value()
                cast.add_actor("gems", gem)

        # everyting below is for scoring
        def promptings():
            prompt.set_text(f"Score: {self._score}\nPlay again? (Y/N)")
            if self._keyboard_service.get_prompt():
                # cast.clear_actors()
                banner.set_text("")
                prompt.set_text("")

                self._score = 100
                pass
            pass

        if self._score < 0:
            # promptings()
            # posx = int(max_x / 2 - (60 * 3))
            # posy = int(max_y / 2)
            # banner.set_position(Point(posx, posy))
            # banner.set_font_size(60)
            # banner.set_text("GAME OVER!")
            pass

        elif len(gems) == 0:
            promptings()
            posx = int(max_x / 2 - (60 * 3))
            posy = int(max_y / 2)
            banner.set_position(Point(posx, posy))
            banner.set_font_size(60)
            banner.set_text(f"YOU WIN!")

        else:
            velocity = self._keyboard_service.get_direction()
            robot.set_velocity(velocity)
            banner.set_text(f'Score: {self._score}')

        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
