import turtle
import time
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MARGIN = 20

def init_screen():
    #set up the screen
    w = turtle.Screen()
    w.title("Snake game")
    w.bgcolor("blue")
    w.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
    w.tracer(0)
    return w

def init_snake_head():
    t = turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("black")
    t.penup()
    t.goto(0, 100)
    t.direction = "istadeh"
    return t

def add_snake_length():
    t = turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("grey")
    t.penup()
    segments.append(t)

def move(h):
    x, y = h.position()
    if h.direction == "bala":
        # h.setpos(x, y + 20)
        h.sety(y+20)
 
    if h.direction == "paein":
        h.setpos(x, y - 20)
 
    if h.direction == "rast":
        h.setpos(x + 20, y)
 
    if h.direction == "chap":
        h.setpos(x - 20, y)

def init_key_listener(s):
    s.listen()
    s.onkey(go_up, "Up")
    s.onkey(go_down, "Down")
    s.onkey(go_right, "Right")
    s.onkey(go_left, "Left")  


def go_up():
    if head.direction != "paein":
        head.direction = "bala"

def go_down():
    if head.direction != "bala":
        head.direction = "paein"

def go_left():
    if head.direction != "rast":
        head.direction = "chap"

def go_right():
    if head.direction != "chap":
        head.direction = "rast"

def init_food():
    f = turtle.Turtle()
    f.speed(0)
    f.shape("circle")
    f.color("red")
    f.penup()
    f.shapesize(0.50, 0.50)
    f.goto(0, 0)
    return f

def check_food(f, h):
    xf, yf = f.position()
    xh, yh = h.position()
    return abs(xh-xf) < 15 and abs(yf-yh) < 15

def reposition_food(f):
    half_width = SCREEN_WIDTH // 2 - MARGIN
    half_height = SCREEN_HEIGHT // 2 - MARGIN
    new_x = random.randint(-1 * half_width, half_width)
    new_y = random.randint(-1 * half_height, half_height)
    f.setpos(new_x, new_y)

def move_segments():
    if len(segments) > 0:
        for i in range(len(segments)-1, 0, -1):
            x_prev_seg, y_prev_seg = segments[i-1].position()
            segments[i].setpos(x_prev_seg, y_prev_seg)
        
        xh, xy = head.position()
        segments[0].setpos(xh, xy)

def check_border_collision(h):
    x,y = h.position()
    half_width = SCREEN_WIDTH // 2 
    half_height = SCREEN_HEIGHT // 2 
    return x > half_width or x < (-1 * half_width) or y > half_height or y < (-1 * half_height)

def check_self_collision():
    for seg in segments:
        if seg.distance(head) < 10:
            return True
    return False

def update_score():
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.goto(0, 260)
    s = "Score: {} High Score: {}".format(score, high_score)
    score_writer.write(s, align="center", font=("Courier", 20, "normal"))

def reset_game():
    global segments
    for seg in segments:
        seg.goto(1000,0)
    segments = []
    food.goto(0,0)
    head.goto(0,100)
    head.direction = "istadeh"

def init_score_writer():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    return pen   


scrn = init_screen()
head = init_snake_head()
food = init_food()
score_writer = init_score_writer()

init_key_listener(scrn)
segments = []
score = 0
high_score = 0

while True:
    move_segments()
    move(head)

    if check_border_collision(head) or check_self_collision():        
        if score > high_score:
            high_score = score
        score = 0
        reset_game()

    if check_food(food, head):
        reposition_food(food)
        add_snake_length()   
        score = score + 10

    update_score() 
    scrn.update()
    time.sleep(0.2)

