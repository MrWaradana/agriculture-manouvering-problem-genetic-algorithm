import turtle as tractor
import numpy as np


def create_solution(solution, turns, fitness):
    start_x = -480
    start_y = 0
    width = 25
    height = 100
    track_dictionary = {}
    
    init(solution, fitness)
    start_pos(start_x, start_y)
    
    for i, track in enumerate(solution):
        x = start_x + (i * (width + 20))
        y = start_y
        label = ""
        if i == solution[0] :
                label = "Start"
        elif i == solution[len(solution) - 1]:
                label = "End"
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
                if(solution[i] > solution[i+1] ):
                    create_omega_top(
                    tractor,
                    track_dictionary[solution[i]]["top"]["x"],
                    track_dictionary[solution[i]]["top"]["y"],
                    track_dictionary[solution[i + 1]]["down"]["x"],
                    track_dictionary[solution[i + 1]]["down"]["y"],
                    start='left',
                    extent=240,
                    )
                else:
                    create_omega_top(
                    tractor,
                    track_dictionary[solution[i]]["top"]["x"],
                    track_dictionary[solution[i]]["top"]["y"],
                    track_dictionary[solution[i + 1]]["down"]["x"],
                    track_dictionary[solution[i + 1]]["down"]["y"],
                    start='right',
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
                if(solution[i] > solution[i+1] ):
                    create_omega_down(
                        tractor,
                        track_dictionary[solution[i]]["down"]["x"],
                        track_dictionary[solution[i]]["down"]["y"],
                        track_dictionary[solution[i + 1]]["top"]["x"],
                        -200,
                        start='right',
                        extent=-240,
                        )
                else:   
                    create_omega_down(
                        tractor,
                        track_dictionary[solution[i]]["down"]["x"],
                        track_dictionary[solution[i]]["down"]["y"],
                        track_dictionary[solution[i + 1]]["top"]["x"],
                        -200,
                        start='left',
                        extent=240,
                        )

    tractor.done()
    

def init(solution, fitness):
    tractor.speed(5)
    tractor.setup(1920, 1080, 0, 0)
    tractor.screensize(3000, 2500)
    tractor.color("green")
    tractor.penup()
    tractor.goto(0, 300)
    tractor.write('solution' + str(solution), align="center",  font=("Arial", 24, "normal"))
    tractor.goto(0, 250)
    tractor.write('Total Distance: ' + str(fitness), align="center",  font=("Arial", 24, "normal"))

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
    radius = abs(x1 - x2) / 2
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


def create_omega_top(tractor, x1, y1, x2, y2, start, extent=90):
    tractor.color('blue')
    radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
    cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

    tractor.penup()
    # tractor.pendown()
    if(start == 'left'):
        tractor.setposition(max(x1, x2), cy)
        tractor.setheading(90)
        tractor.pendown()
        tractor.forward(20)
        tractor.right(30)
    elif(start == 'right'):
        tractor.setposition(min(x1, x2), cy)
        tractor.setheading(270)
        tractor.pendown()
        tractor.backward(20)
        tractor.left(30)
    tractor.circle(12+radius, extent=extent)
    # tractor.left(30)
    tractor.goto(x2, y2+100)
    position = tractor.position()

    # tractor.pendown()
    tractor.penup()
    # tractor.circle(radius, extent=extent)
    # tractor.setposition(cx, cy)
    tractor.setposition(position)

def create_omega_down(tractor, x1, y1, x2, y2, start, extent=90):
    tractor.color('blue')
    radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
    cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

    tractor.penup()
    # tractor.pendown()
    if(start == 'right'):
        tractor.setposition(max(x1, x2), cy)
        tractor.setheading(90)
        tractor.pendown()
        tractor.backward(20)
        tractor.left(30)
    elif(start == 'left'):
        tractor.setposition(min(x1, x2), cy)
        tractor.setheading(270)
        tractor.pendown()
        tractor.forward(20)
        tractor.right(30)
    tractor.circle(12+radius, extent=extent)
    # tractor.left(30)
    tractor.goto(x2, y2+100)
    position = tractor.position()

    tractor.pendown()
    # tractor.penup()
    # tractor.circle(radius, extent=extent)
    # tractor.setposition(cx, cy)
    tractor.setposition(position)


# def create_omega(tractor, x1, y1, x2, y2, start=0, extent=90):
#     tractor.color('blue')
#     radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
#     cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

#     tractor.penup()
#     # tractor.pendown()
#     tractor.setposition(max(x1, x2), cy)
#     tractor.setheading(90)
#     tractor.pendown()
#     tractor.forward(20)
#     tractor.right(30)
#     tractor.circle(12+radius, extent=extent)
#     # tractor.left(30)
#     tractor.goto(x2, y2+100)
#     position = tractor.position()

#     # tractor.pendown()
#     tractor.penup()
#     tractor.circle(radius, extent=extent)
#     tractor.setposition(cx, cy)
#     tractor.setposition(position)
