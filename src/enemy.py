from game_entity import GameEntity
import pygame


class Enemy(GameEntity):

    def __init__(self):
        super().__init__()
        self._colour: tuple[int, int, int] = (200, 0, 0)
        self._radius: float = 12.0

    def draw(self,
             surface: pygame.Surface) -> None:
        position: tuple[int, int] = (int(self._position[0]), int(self._position[1]))
        pygame.draw.circle(surface, self._colour, position, self._radius)