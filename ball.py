from turtle import Turtle
from player import Player
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        # Note: tangent of (1/2) == 26.56 degrees
        self.movement_high = 6
        self.movement_low = 3
        self.dist_x = random.randint(self.movement_low, self.movement_high)*random.choice([-1, 1])
        self.dist_y = random.randint(self.movement_low, self.movement_high)*random.choice([-1, 1])

    def move(self):
        new_x = self.xcor() + self.dist_x
        new_y = self.ycor() + self.dist_y
        self.goto(x=new_x, y=new_y)

    def is_out_vertical(self):
        if abs(self.ycor()) > 290:
            self.dist_y = -1 * self.dist_y * random.uniform(0.75, 1.25)
        else:
            pass

    def is_out_horizontal(self):
        if self.xcor() > 590:
            print("right score")
        elif self.xcor() < -590:
            print("left score")
        else:
            pass

    def contact(self,
                player1: Player,
                player2: Player ):
        for segment in player1.segments:
            if self.distance(segment) < 15:
                self.bounce()
            else:
                pass

        for segment in player2.segments:
            if self.distance(segment) < 15:
                self.bounce()
            else:
                pass

    def bounce(self):
        self.dist_x = -1 * self.dist_x * random.uniform(0.9, 1.2)



