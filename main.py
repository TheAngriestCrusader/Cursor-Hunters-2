from app import App
import pygame


class Player(object):

    def __init__(self):
        pass


def main() -> None:
    pygame.init()
    app: App = App()
    exit_code = app.mainloop()
    pygame.quit()
    exit(exit_code)


if __name__ == "__main__":
    main()
