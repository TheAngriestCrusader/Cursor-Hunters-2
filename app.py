from constants import *
import pygame


class App(object):
    _version_major: int = 2
    _version_minor: int = 1
    _version_patch: int = 0

    def __init__(self,
                 window_resolution: tuple[float, float] = (640.0, 640.0),
                 window_title: str = GAME_TITLE):
        # Set caption before instantiating window to avoid seeing default window caption before changing it
        pygame.display.set_caption(window_title)

        self._background_colour: tuple[int, int, int] = (255, 255, 255)
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._mouse_position: tuple[int, int] = (0, 0)
        self._running: bool = True
        self._window = pygame.display.set_mode(window_resolution)
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

            self._window.fill(self._background_colour)

            pygame.display.flip()

        return 0