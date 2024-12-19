from app import App
from constants import *
import pygame


def main() -> None:
    pygame.init()
    app: App = App()
    app.set_window_title(f"{GAME_TITLE} V{app.get_version()}")
    print(f"Running {GAME_TITLE} version {App.get_version()}")
    exit_code = app.mainloop()
    pygame.quit()
    exit(exit_code)


if __name__ == "__main__":
    main()
