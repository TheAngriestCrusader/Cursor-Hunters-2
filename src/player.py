from game_entity import GameEntity
import pygame


class Player(GameEntity):

    def __init__(self,
                 position: tuple[float, float]) -> None:
        super().__init__(position)
        self._health: float = 100.0
        self._max_health: float = 100.0
        self._max_speed: float = 256.0
        self._radius: float = 16.0
