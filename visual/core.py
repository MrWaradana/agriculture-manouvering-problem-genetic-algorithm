import turtle as tractor
import numpy as np


def create_solution(solution, turns):
    start_x = -480
    start_y = 0
    width = 25
    height = 100
    track_dictionary = {}
    
    init(solution)
    start_pos(start_x, start_y)
    
    for i, track in enumerate(solution):
        x = start_x + (i * (width + 20))
        y = start_y
        label = f"Track {i}"
        track_dictionary[i] = {
            "track": track,
            "top": {"x": x, "y": y + height * 2},
            "down": {"x": x, "y": y},
        }
        draw_track(x, y, label)
    
    
    for i in range(len(solution) - 1):
        if i == len(track_dictionary) - 1:
            break
        if i % 2 == 0:
            if(turns[i] == 0):
                create_arc(
                    tractor,
                    track_dictionary[solution[i]]["top"]["x"],
                    track_dictionary[solution[i]]["top"]["y"],
                    track_dictionary[solution[i + 1]]["down"]["x"],
                    track_dictionary[solution[i + 1]]["down"]["y"],
                    start=0,
                    extent=180,
                )
            else:
                create_omega(
                tractor,
                track_dictionary[solution[i]]["top"]["x"],
                track_dictionary[solution[i]]["top"]["y"],
                track_dictionary[solution[i + 1]]["down"]["x"],
                track_dictionary[solution[i + 1]]["down"]["y"],
                start=-180,
                extent=-240,
                )
        else:
            if(turns[i] == 0):
                create_arc(
                tractor,
                track_dictionary[solution[i]]["down"]["x"],
                track_dictionary[solution[i]]["down"]["y"],
                track_dictionary[solution[i + 1]]["top"]["x"],
                -200,
                start=-180,
                extent=180,
                )
            else:
                create_omega(
                tractor,
                track_dictionary[solution[i]]["down"]["x"],
                track_dictionary[solution[i]]["down"]["y"],
                track_dictionary[solution[i + 1]]["top"]["x"],
                -200,
                start=-180,
                extent=220,
                )

    tractor.done()
    

def init(solution):
    tractor.speed(5)
    tractor.setup(1920, 1080, 0, 0)
    tractor.screensize(3000, 2500)
    tractor.color("green")
    tractor.penup()
    tractor.goto(0, 300)
    tractor.write('solution' + str(solution), align="center",  font=("Arial", 24, "normal"))
    

def start_pos(start_x, start_y):
    tractor.right(90)
    tractor.up()
    tractor.setpos(start_x, start_y)
    tractor.down()
    tractor.width(2)


def draw_track(x, y, label, height=100):
    tractor.up()
    tractor.goto(x, y)
    tractor.down()
    tractor.forward(height)
    tractor.write(label, align="center")
    tractor.up()
    tractor.setpos(x, y)
    tractor.down()
    tractor.backward(height)


def create_arc(tractor, x1, y1, x2, y2, start=0, extent=90):
    tractor.color('orange')
    radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
    cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

    tractor.penup()
    tractor.setposition(max(x1, x2), cy)
    tractor.pendown()
    tractor.setheading(90)
    tractor.circle(radius, extent=start)
    position = tractor.position()

    tractor.pendown()
    # tractor.penup()
    tractor.circle(radius, extent=extent)
    tractor.penup()
    tractor.setposition(cx, cy)
    tractor.setposition(position)


def create_omega(tractor, x1, y1, x2, y2, start=0, extent=90):
    tractor.color('blue')
    radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
    cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

    tractor.penup()
    # tractor.pendown()
    tractor.setposition(max(x1, x2), cy)
    tractor.setheading(90)
    tractor.circle(radius, extent=start)
    position = tractor.position()

    tractor.pendown()
    tractor.backward(20)
    tractor.left(30)
    tractor.circle(20+radius, extent=extent)
    # tractor.left(15)
    tractor.backward(30)
    tractor.penup()
    tractor.setposition(cx, cy)
    tractor.setposition(position)
