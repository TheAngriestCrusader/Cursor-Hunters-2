from constants import *
from player import Player
import pygame


class App(object):
    _version_major: int = 2
    _version_minor: int = 2
    _version_patch: int = 0

    def __init__(self,
                 window_resolution: tuple[int, int] = (640, 640),
                 window_title: str = GAME_TITLE) -> None:
        # Set caption before instantiating window to avoid seeing default window caption before changing it
        pygame.display.set_caption(window_title)

        self._background_colour: tuple[int, int, int] = (255, 255, 255)
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._delta_time: float = 0.0
        self._framerate_limit: int = 0
        self._mouse_position: tuple[int, int] = (0, 0)
        self._player: Player = Player()
        self._running: bool = True
        self._window: pygame.Surface = pygame.display.set_mode(window_resolution)
        print(f"Running {GAME_TITLE} version {App.get_version()}")

    @staticmethod
    def get_version() -> str:
        return f"{App._version_major}.{App._version_minor}.{App._version_patch}"

    def close(self) -> None:
        self._running = False

    def mainloop(self) -> int:

        while self._running:

            for event in pygame.event.get():

                match event.type:

                    case pygame.QUIT:
                        self.close()

            self._mouse_position = pygame.mouse.get_pos()
            self._player.move_towards((float(self._mouse_position[0]), float(self._mouse_position[1])),
                                      self._delta_time)

            self._window.fill(self._background_colour)
            self._player.draw(self._window)

            pygame.display.flip()
            self._delta_time = self._clock.tick(self._framerate_limit) / MS_IN_SECOND

        return 0
