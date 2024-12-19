from game_entity import GameEntity
from typing import TypeVar
import pygame

Type_GameEntity: TypeVar = TypeVar('Type_GameEntity',
                                   bound=GameEntity)


class GameEntityManager(object):

    def __init__(self) -> None:
        self._game_entities: list[GameEntity] = []

    def draw_game_entities(self,
                           surface: pygame.Surface) -> None:

        for game_entity in self._game_entities:
            game_entity.draw(surface)

    def spawn_game_entity(self,
                          entity_type: type[GameEntity],
                          *args,
                          **kwargs) -> Type_GameEntity:
        game_entity: entity_type = entity_type(*args, **kwargs)
        self._game_entities.append(game_entity)

        return game_entity

    def test_collision(self,
                       game_entity: GameEntity) -> list[GameEntity]:
        colliding_game_entities = []

        for other_game_entity in self._game_entities:

            if game_entity.is_colliding(other_game_entity):
                colliding_game_entities.append(other_game_entity)

        return colliding_game_entities
