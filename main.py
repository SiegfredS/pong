from screen import NewScreen
from player import Player
from ball import Ball
import time

screen = NewScreen()
my_screen = screen.screen
# Screen tracer is zero == no animation delay
my_screen.tracer(0)
ball = Ball()
right_player = Player()
left_player = Player(right=-1)
right_player.write_score()
left_player.write_score()

my_screen.listen()
my_screen.onkeypress(fun=right_player.move_up, key="Up")
my_screen.onkeypress(fun=right_player.move_down, key="Down")
my_screen.onkeypress(fun=left_player.move_up, key="w")
my_screen.onkeypress(fun=left_player.move_down, key="s")
is_playing = True

while is_playing:
    time.sleep(0.01)
    my_screen.update()
    ball.contact(player1=left_player,
                 player2=right_player)
    ball.move()
    ball.is_out_vertical()
    if ball.right_scores() == 1:
        right_player.add_score()
        right_player.write_score()
        ball.reset_or_start()
    elif ball.right_scores() == 0:
        left_player.add_score()
        left_player.write_score()
        ball.reset_or_start()
    elif ball.right_scores() == -1:
        pass
    else:
        pass

my_screen.exitonclick()
