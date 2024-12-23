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
        Spawns a new enemy at a random position on the screen and assigns a target.

        Args:
            target (GameEntity | None): The target GameEntity that the spawned 
                enemy will move towards. Defaults to None.

        Returns:
            GameEntity: The newly spawned enemy instance.
        """
        # Generate a random position within the game window
        spawn_position: tuple[float, float] = (random.randint(0, WINDOW_SIZE[0]),
                                               random.randint(0, WINDOW_SIZE[1]))
        # Create a new enemy instance via the game entity manager
        enemy: Enemy = self._game_entity_manager.spawn_game_entity(Enemy,
                                                                   target=target,
                                                                   game_entity_manager=self._game_entity_manager,
                                                                   position=spawn_position,
                                                                   radius=8.0)
        self._enemies.append(enemy)

        return enemy
