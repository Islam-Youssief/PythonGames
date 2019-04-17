# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    # these are vectors stored as lists
    global ball_pos, ball_vel
    # start on the center of the table
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60,
                  -(random.randrange(60, 180) / 60)]
    else:
        ball_vel = [-(random.randrange(120, 240) / 60),
                    -(random.randrange(60, 180) / 60)]


# define event handlers
def new_game():
    # these are numbers
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    # these are ints
    global score1, score2
    # initialize postion of every paddle and start with zero
    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2, (HEIGHT - PAD_HEIGHT) / 2
    paddle1_vel = paddle2_vel = score1 = score2 = 0
    # change direction
    spawn_ball(not(LEFT))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "#48e1e5")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "#48e1e5")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, "#48e1e5")
    # update ball
    update_ball()
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 0.1, "#fcada7", "#fcada7")
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos],[PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH / 2, paddle2_pos],[WIDTH- PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    # draw scores
    canvas.draw_text(str(score1), (185, 40), 40, "#48e1e5")
    canvas.draw_text(str(score2), (400, 40), 40, "#48e1e5")


def update_ball():
    """Change the postion of the ball."""
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # check on ball_pos[0]
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # chage ball vel
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            # score a goal and increase value of score
            spawn_ball(RIGHT)
            score2 = score2 + 1

    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        # chage ball vel
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            # score a goal and increase value of score
            spawn_ball(LEFT)
            score1 = score1 + 1

    # check on ball_pos[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    # change postion
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

def keydown(key):
    """Control the velocity."""
    global paddle1_vel, paddle2_vel
    velocity = 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = velocity
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -velocity
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = velocity
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -velocity


def keyup(key):
    """Reset the velocity."""
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def start_the_game():
    """Create the frame of the game."""
    frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(keydown)
    frame.set_keyup_handler(keyup)
    frame.add_button("Restart", new_game, 180)

    # start frame
    new_game()
    frame.start()


def main():
    """Start point of the game."""
    start_the_game()

if __name__ == "__main__":
    main()
