from constants import *
from enemy import Enemy
from game_entity import GameEntity
from game_entity_manager import GameEntityManager
import random


class EnemyManager(GameEntityManager):

    def __init__(self,
                 game_entity_manager: GameEntityManager) -> None:
        super().__init__()
        self._enemies: list[Enemy] = []
        self._game_entity_manager = game_entity_manager

    def move_enemies(self,
                     delta_time: float) -> None:

        for enemy in self._enemies:
            enemy.move_towards_target(delta_time)

    def spawn_enemy(self,
                    target: GameEntity | None = None) -> GameEntity:
        spawn_position: tuple[float, float] = (random.randint(0, WINDOW_SIZE[0]),
                                               random.randint(0, WINDOW_SIZE[1]))
        enemy: Enemy = self._game_entity_manager.spawn_game_entity(Enemy,
                                                                   target = target,
                                                                   position = spawn_position,
                                                                   radius = 8.0)
        self._enemies.append(enemy)

        return enemy
