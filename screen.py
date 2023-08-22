from turtle import Screen


class NewScreen:
    def __init__(self):
        self.screen = Screen()
        self.setup()

    def setup(self,
              width=1200,
              height=600):
        self.screen.setup(width=width,
                          height=height)
        self.screen.title(titlestring="Pong")
        self.screen.bgcolor("black")

