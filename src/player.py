from src.game_entity import GameEntity


class Player(GameEntity):
    """
    Represents the player entity in the game, inheriting from GameEntity.
    """

    def __init__(self,
                 *args,
                 **kwargs) -> None:
        """
        Initializes the player with default attributes such as health, speed, and radius,
        and sets the player's initial position.

        Args:
            position (tuple[float, float]): Coordinates for the player's initial position.
        """
        super().__init__(*args, **kwargs)
        self._health: float = 100.0
        self._max_health: float = 100.0
        self._max_speed: float = 256.0
        self._radius: float = 16.0
