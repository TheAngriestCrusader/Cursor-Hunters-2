import pygame


class Player(object):

    def __init__(self) -> None:
        self._colour: tuple[int, int, int] = (255, 0, 0)
        self._health: float = 100.0
        self._max_health: float = 100.0
        self._max_speed: float = 256.0
        self._position: tuple[float, float] = (0.0, 0.0)
        self._radius: float = 16.0

    def draw(self,
             surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self._colour, self._position, self._radius)

    def move_towards(self,
                     target_position: tuple[int, int],
                     delta_time: float) -> None:
        delta_x: float = target_position[0] - self._position[0]
        delta_y: float = target_position[1] - self._position[1]
        distance: float = (delta_x ** 2 + delta_y ** 2) ** 0.5
        max_move_distance: float = self._max_speed * delta_time

        if distance <= max_move_distance:
            self._position = target_position

        else:
            # Normalize the direction vector and scale by adjusted max speed
            direction: tuple[float, float] = (delta_x / distance, delta_y / distance)
            new_position: tuple[float, float] = (self._position[0] + direction[0] * max_move_distance,
                                                 self._position[1] + direction[1] * max_move_distance)
            self.set_position(new_position)

    def set_position(self,
                     new_position: tuple[float, float]):
        self._position = new_position
