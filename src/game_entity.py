from __future__ import annotations

import pygame


class GameEntity(object):

    def __init__(self,
                 position: tuple[float, float],
                 colour: tuple[int, int, int] = (255, 0 ,0),
                 max_speed: float = 128.0,
                 radius: float = 16.0) -> None:
        self._colour: tuple[int, int, int] = colour
        self._max_speed: float = max_speed
        self._position: tuple[float, float] = position
        self._radius: float = radius

    def draw(self,
             surface: pygame.Surface) -> None:
        position: tuple[int, int] = (int(self._position[0]), int(self._position[1]))
        pygame.draw.circle(surface, self._colour, position, self._radius)

    def get_position(self) -> tuple[float, float]:

        return self._position

    def get_radius(self) -> float:

        return self._radius

    def is_colliding(self,
                     target: GameEntity | None = None) -> bool:

        if target is None:

            return False

        target_position: tuple[float, float] = target.get_position()
        target_radius: float = target.get_radius()
        delta_x: float = self._position[0] - target_position[0]
        delta_y: float = self._position[1] - target_position[1]
        distance_squared: float = delta_x ** 2 + delta_y ** 2
        combined_radius: float = self._radius + target_radius
        colliding: bool = distance_squared <= combined_radius ** 2

        return colliding

    def move_towards(self,
                     target_position: tuple[float, float],
                     delta_time: float) -> None:
        delta_x: float = target_position[0] - self._position[0]
        delta_y: float = target_position[1] - self._position[1]
        distance: float = (delta_x ** 2 + delta_y ** 2) ** 0.5
        max_move_distance: float = self._max_speed * delta_time

        if distance <= max_move_distance:
            self._position = target_position

        else:
            direction: tuple[float, float] = (delta_x / distance, delta_y / distance)
            new_position: tuple[float, float] = (self._position[0] + direction[0] * max_move_distance,
                                                 self._position[1] + direction[1] * max_move_distance)
            self.set_position(new_position)

    def set_position(self,
                     new_position: tuple[float, float]) -> None:
        self._position = new_position
