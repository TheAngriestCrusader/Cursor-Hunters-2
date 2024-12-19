from constants import *
from game_entity import GameEntity
import pygame
import random


class Enemy(GameEntity):

    def __init__(self,
                 target: GameEntity | None = None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._colour: tuple[int, int, int] = (random.randint(ENEMY_COLOUR_MIN_RED, ENEMY_COLOUR_MAX_RED), 0, 0)
        self._target: GameEntity | None = target

    def is_colliding_target(self) -> bool:

        if self._target is None:

            return False

        return super().is_colliding(self._target)

    def move_towards_target(self,
                            delta_time: float) -> bool:

        if self._target is None:

            return False

        super().move_towards(self._target.get_position(), delta_time)

        return super().is_colliding(self._target)
