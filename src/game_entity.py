from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from src.game_entity_manager import GameEntityManager


class GameEntity(object):
    """
    Represents a game entity with a position, radius, speed, and color.
    Provides functionality for movement, collision detection, and drawing.
    """

    def __init__(self,
                 game_entity_manager: GameEntityManager,
                 position: tuple[float, float],
                 colour: tuple[int, int, int] = (255, 0, 0),
                 max_speed: float = 128.0,
                 radius: float = 16.0) -> None:
        self._colour: tuple[int, int, int] = colour
        self._game_entity_manager: GameEntityManager = game_entity_manager
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

        return distance_squared <= combined_radius ** 2

    def move_towards(self,
                     target_position: tuple[float, float],
                     delta_time: float) -> None:
        delta_x: float = target_position[0] - self._position[0]
        delta_y: float = target_position[1] - self._position[1]
        distance: float = (delta_x ** 2 + delta_y ** 2) ** 0.5
        max_move_distance: float = self._max_speed * delta_time

        if distance <= max_move_distance:
            self.set_position(target_position)

        else:
            direction: tuple[float, float] = (delta_x / distance, delta_y / distance)
            new_position: tuple[float, float] = (self._position[0] + direction[0] * max_move_distance,
                                                 self._position[1] + direction[1] * max_move_distance)
            self.set_position(new_position)

    def resolve_collision(self,
                          original_position: tuple[float, float],
                          target_position: tuple[float, float],
                          colliding_entities: list[GameEntity]) -> tuple[float, float]:
        """
        Resolves collisions with sliding, considering all colliding entities and
        calculating a direction to move away from the overlapping ones.
        """
        # Initialize a final resolution vector
        resolution_x, resolution_y = 0, 0

        # Iterate over all colliding entities
        for entity in colliding_entities:
            colliding_position = entity.get_position()
            delta_x = self._position[0] - colliding_position[0]
            delta_y = self._position[1] - colliding_position[1]

            # Calculate the overlap distance
            distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
            overlap = max(0, self._radius + entity._radius - distance)  # Overlap resolution distance

            if overlap > 0:  # If there is an overlap, calculate push-out vector
                if distance > 0:  # Valid direction exists
                    normal_x = delta_x / distance  # Normalize vector
                    normal_y = delta_y / distance
                else:  # If positions are exactly the same, arbitrarily choose a direction
                    normal_x = 1.0
                    normal_y = 0.0

                # Push out of collision along the normal vector
                resolution_x += normal_x * overlap
                resolution_y += normal_y * overlap

        # Apply the calculated resolution to the entity's position
        adjusted_position = (
            self._position[0] + resolution_x,
            self._position[1] + resolution_y,
        )

        # Add a small buffer (epsilon) to ensure entities fully resolve and prevent re-collision
        epsilon = 0.01  # Tune buffer size if needed
        adjusted_position = (
            adjusted_position[0] + resolution_x * epsilon,
            adjusted_position[1] + resolution_y * epsilon,
        )

        # Test if the adjusted position resolves all collisions
        self._position = adjusted_position
        if not self._game_entity_manager.test_collision(self):  # All collisions resolved
            return adjusted_position

        # If still colliding after adjustments, fallback to original position (rare case)
        self._position = original_position
        return original_position

    def set_position(self,
                     new_position: tuple[float, float],
                     ignore_collision: bool = False) -> None:
        original_position: tuple[float, float] = self._position
        self._position = new_position
        colliding_game_entities: list[GameEntity] = self._game_entity_manager.test_collision(self)

        # If no collision or collisions are ignored, set position
        if not len(colliding_game_entities) or ignore_collision:
            self._position = new_position
            return

        # More complicated collision resolution: sliding off entities
        print(f"Collision detected with {len(colliding_game_entities)} entities.")
        self._position = self.resolve_collision(original_position, new_position, colliding_game_entities)
