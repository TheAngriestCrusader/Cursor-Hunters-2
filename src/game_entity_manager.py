from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar
import pygame

if TYPE_CHECKING:
    from src.game_entity import GameEntity

Type_GameEntity: TypeVar = TypeVar('Type_GameEntity',
                                   bound="GameEntity")


class GameEntityManager(object):
    """
    Manages a collection of GameEntity objects and provides functionality for
    drawing, spawning, and testing for collisions between entities.
    """

    def __init__(self) -> None:
        self._game_entities: list[GameEntity] = []

    def draw_game_entities(self,
                           surface: pygame.Surface) -> None:
        """
        Draws all game entities onto the provided surface.

        Args:
            surface (pygame.Surface): The pygame surface to draw on.
        """

        for game_entity in self._game_entities:
            game_entity.draw(surface)

    def spawn_game_entity(self,
                          entity_type: type[GameEntity],
                          *args,
                          **kwargs) -> Type_GameEntity:
        """
        Spawns a new game entity of the given type and adds it to the manager's list.

        Args:
            entity_type (type[GameEntity]): The class of the entity to spawn.
            *args: Positional arguments to pass to the entity's constructor.
            **kwargs: Keyword arguments to pass to the entity's constructor.

        Returns:
            Type_GameEntity: The newly created game entity.
        """
        game_entity: entity_type = entity_type(*args, **kwargs)

        # Check for collisions with existing entities
        for existing_entity in self._game_entities:

            if game_entity.is_colliding(existing_entity):

                raise ValueError("Spawned entity collides with an existing entity.")

        self._game_entities.append(game_entity)

        return game_entity

    def test_collision(self,
                       game_entity: GameEntity) -> list[GameEntity]:
        """
        Tests for collisions between the given game entity and all other entities.

        Args:
            game_entity (GameEntity): The entity to test for collisions against others.

        Returns:
            list[GameEntity]: A list of entities that are colliding with the given entity.
        """
        colliding_game_entities = []

        for other_game_entity in self._game_entities:

            if game_entity.is_colliding(other_game_entity) and game_entity is not other_game_entity:
                colliding_game_entities.append(other_game_entity)

        return colliding_game_entities
