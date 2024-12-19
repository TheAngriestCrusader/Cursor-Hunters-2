from game_entity import GameEntity
import pygame


class Player(GameEntity):

    def __init__(self) -> None:
        super().__init__()
        self._colour: tuple[int, int, int] = (255, 0, 0)
        self._health: float = 100.0
        self._max_health: float = 100.0
        self._max_speed: float = 256.0
        self._radius: float = 16.0

    def draw(self,
             surface: pygame.Surface) -> None:
        position: tuple[int, int] = (int(self._position[0]), int(self._position[1]))
        pygame.draw.circle(surface, self._colour, position, self._radius)
