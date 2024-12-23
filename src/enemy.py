from src.constants import *
from src.game_entity import GameEntity
import random


class Enemy(GameEntity):
    """
    Represents an enemy entity in the game, which can target and move towards another GameEntity.
    """

    def __init__(self,
                 target: GameEntity | None = None,
                 *args,
                 **kwargs):
        """
        Initializes an Enemy instance.

        Args:
            target (GameEntity | None): The GameEntity that this Enemy will target.
            *args: Positional arguments passed to the base GameEntity class.
            **kwargs: Keyword arguments passed to the base GameEntity class.
        """
        super().__init__(*args, **kwargs)
        # Set the enemy's color to a random shade of red
        self._colour: tuple[int, int, int] = (random.randint(ENEMY_COLOUR_MIN_RED, ENEMY_COLOUR_MAX_RED), 0, 0)
        self._target: GameEntity | None = target

    def is_colliding_target(self) -> bool:
        """
        Checks if the Enemy is colliding with its target.

        Returns:
            bool: True if colliding with the target, False otherwise.
        """
        if self._target is None:  # No target assigned, cannot collide

            return False

        # Use the base class's method to check collision with the target
        return super().is_colliding(self._target)

    def move_towards_target(self,
                            delta_time: float) -> None:
        """
        Moves the Enemy towards its target and checks for collision after movement.

        Args:
            delta_time (float): The time elapsed since the last frame, used for smooth movement.

        Returns:
            bool: True if the Enemy is colliding with its target after moving, False otherwise.
        """
        if self._target is None:  # No target assigned, cannot move towards it

            return

        # Move towards the target's position using the base class's method
        super().move_towards(self._target.get_position(), delta_time)
