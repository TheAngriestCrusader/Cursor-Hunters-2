from __future__ import annotations
from src.constants import *
from src.enemy import Enemy
from src.game_entity_manager import GameEntityManager
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from src.game_entity import GameEntity


class EnemyManager(GameEntityManager):
    """
    Manages enemy-specific behavior, such as spawning and moving enemies.
    This is a specialized version of GameEntityManager.
    """

    def __init__(self,
                 game_entity_manager: GameEntityManager) -> None:
        """
        Initializes the EnemyManager.

        Args:
            game_entity_manager (GameEntityManager): The primary entity manager 
                that handles all game entities.
        """
        super().__init__()
        self._enemies: list[Enemy] = []
        self._game_entity_manager = game_entity_manager

    def _is_position_valid(self, position: tuple[float, float], radius: float) -> bool:
        """
        Checks whether a position is valid by ensuring it doesn't overlap
        with any existing enemies.

        Args:
            position (tuple[float, float]): The position to check.
            radius (float): The radius of the enemy being spawned.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        for enemy in self._enemies:
            existing_pos = enemy.get_position()
            existing_radius = enemy.get_radius()
            distance = ((position[0] - existing_pos[0]) ** 2 + (position[1] - existing_pos[1]) ** 2) ** 0.5
            # Check if the distance is less than the sum of the radii (overlap)

            if distance < (radius + existing_radius):

                return False

        return True

    def move_enemies(self,
                     delta_time: float) -> None:
        """
        Moves all managed enemies towards their respective targets.

        Args:
            delta_time (float): The time delta for consistent movement calculations.
        """

        for enemy in self._enemies:
            enemy.move_towards_target(delta_time)

    def spawn_enemy(self,
                    target: GameEntity | None = None) -> GameEntity:
        """
        Spawns a new enemy at a random position on the screen edges and ensures
        it doesn't overlap with existing enemies.

        Args:
            target (GameEntity | None): The target GameEntity that the spawned
                enemy will move towards. Defaults to None.

        Returns:
            GameEntity: The newly spawned enemy instance.
        """
        max_retries = 100  # Prevent infinite loops
        radius = 8.0  # Radius of the new enemy
        spawn_position: tuple[float, float] = (0, 0)

        for _ in range(max_retries):
            # Randomly select an edge: 0=top, 1=bottom, 2=left, 3=right
            edge = random.choice(["top", "bottom", "left", "right"])

            # Determine spawn position based on the selected edge
            if edge == "top":
                spawn_position = (random.randint(0, WINDOW_SIZE[0]), 0)
            elif edge == "bottom":
                spawn_position = (random.randint(0, WINDOW_SIZE[0]), WINDOW_SIZE[1])
            elif edge == "left":
                spawn_position = (0, random.randint(0, WINDOW_SIZE[1]))
            elif edge == "right":
                spawn_position = (WINDOW_SIZE[0], random.randint(0, WINDOW_SIZE[1]))

            # Check if the position is valid (no overlaps)
            if self._is_position_valid(spawn_position, radius):
                break
        else:
            raise RuntimeError("Unable to spawn enemy without overlap after 100 retries.")

        # Create a new enemy instance via the game entity manager
        enemy: Enemy = self._game_entity_manager.spawn_game_entity(Enemy,
                                                                   target=target,
                                                                   game_entity_manager=self._game_entity_manager,
                                                                   position=spawn_position,
                                                                   radius=radius)
        self._enemies.append(enemy)

        return enemy
