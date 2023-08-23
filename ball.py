from turtle import Turtle
from player import Player
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Note: tangent of (1/2) == 26.56 degrees
        self.movement_high = self.movement_low = self.dist_y = self.dist_x = 0
        self.reset_or_start()

    def reset_or_start(self):
        self.movement_high = 5
        self.movement_low = 3
        self.dist_x = random.randint(self.movement_low, self.movement_high) * random.choice([-1, 1])
        self.dist_y = random.randint(self.movement_low, self.movement_high) * random.choice([-1, 1])
        self.goto(x=0, y=0)

    def move(self):
        new_x = self.xcor() + self.dist_x
        new_y = self.ycor() + self.dist_y
        self.goto(x=new_x, y=new_y)

    def is_out_vertical(self):
        if abs(self.ycor()) > 290:
            if abs(self.dist_y) <= 1:
                # if low self.dist_y, augment absolute value by adding/subtracting 3
                self.dist_y += 3 * self.dist_y / abs(self.dist_y)
            self.dist_y = -1 * self.dist_y * random.uniform(0.975, 1)
            self.move()
        else:
            pass

    def right_scores(self):
        # if left scores
        if self.xcor() > 590:
            return 0
        # if right scores
        elif self.xcor() < -590:
            return 1
        else:
            return -1

    def contact(self,
                player1: Player,
                player2: Player ):
        for segment in player1.segments:
            if self.distance(segment) <= 15:
                self.bounce()
                self.move()
            else:
                pass

        for segment in player2.segments:
            if self.distance(segment) <= 15:
                self.bounce()
                self.move()
            else:
                pass

    def bounce(self):
        self.dist_x = -1 * self.dist_x * random.uniform(0.95, 1.2)
        self.dist_y = random.choice([-1, 1]) * self.dist_y * random.uniform(0.95, 1.2)


