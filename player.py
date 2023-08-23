from turtle import Turtle


class Player:
    def __init__(self,
                 right=1,
                 move_distance=20,
                 speed=5,
                 length=7):
        super().__init__()
        self.move_distance = move_distance
        self.speed = speed
        self.length = length
        self.init_x = 580*right
        self.segments = []
        self.initialize_segments()
        self.head = self.segments[0]
        self.head.setheading(90)
        self.tail = self.segments[-1]
        self.tail.setheading(270)

    def initialize_segments(self):
        y_head = 10*self.length
        for i in range(self.length):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.width(20)
            new_segment.penup()
            new_segment.speed(self.speed)
            new_segment.goto(x=self.init_x,
                             y=y_head-(20*i))
            self.segments.append(new_segment)

    def move_up(self):
        # Always start with tail to head yung movement
        for i in range(self.length-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        # head forwards last
        self.head.forward(self.move_distance)

    def move_down(self):
        for i in range(0, self.length-1):
            self.segments[i].goto(self.segments[i+1].position())
        self.tail.forward(self.move_distance)