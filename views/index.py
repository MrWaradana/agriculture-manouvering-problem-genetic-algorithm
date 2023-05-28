from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import turtle as turtle


## Root configuration
root = tk.Tk()
root.title('Agriculture Maneuvering Problem')
root.geometry('1980x1080')
root.config(bg='gray')
root.state('zoomed')

canvas = Canvas(root, width=1024, height=768, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=10, pady=14)

tractor = turtle.RawTurtle(canvas)


def reset():
    tractor.clear()


def start():
    solution = [18, 15, 19, 14, 17, 13, 16, 11, 8, 12, 10, 7, 3, 6, 9, 5, 1, 4, 0, 2]
    turns = [0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]

    # tractor.setup(1920, 1080, 0, 0)
    # tractor.screensize(3000, 2500)
    tractor.color("green")


    start_x = -440
    start_y = 0
    width = width_entry.get()
    height = 100
    speed = 0
    # track_dictionary ={
    #     "track" : 0,
    #     "top":{
    #         "x": 0,
    #         "y": 0
    #     },
    #     "down": {
    #         "x": 0,
    #         "y": 0
    #     }
    # }

    track_dictionary = {}

    tractor.speed(speed)
    tractor.penup()
    tractor.goto(0, 300)
    tractor.write('solution' + str(solution), align="center",  font=("Arial", 16, "normal"))


    def start_pos():
        tractor.right(90)
        tractor.up()
        tractor.setpos(start_x, start_y)
        tractor.down()
        tractor.width(2)



    start_pos()


    def draw_track(x, y, label):
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
        radius = abs(x1-x2)  / 2
        cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

        tractor.penup()
        tractor.setposition(max(x1, x2), cy)
        tractor.setheading(90)
        tractor.pendown()
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
                if(solution[i] > solution[i+1] ):
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
                    create_arc(
                        tractor,
                        track_dictionary[solution[i]]["top"]["x"],
                        track_dictionary[solution[i]]["top"]["y"],
                        track_dictionary[solution[i + 1]]["down"]["x"],
                        track_dictionary[solution[i + 1]]["down"]["y"],
                        start=180,
                        extent=-180,
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


            # create_arc(tractor, track_dictionary[solution[i]]['top']['x'], track_dictionary[solution[i]]['top']['y'], track_dictionary[solution[i+1]]['down']['x'], track_dictionary[solution[i+1]]['down']['y'], start=180, extent=-180)
            # create_omega(
            #     tractor,
            #     track_dictionary[solution[i]]["top"]["x"],
            #     track_dictionary[solution[i]]["top"]["y"],
            #     track_dictionary[solution[i + 1]]["down"]["x"],
            #     track_dictionary[solution[i + 1]]["down"]["y"],
            #     start=-180,
            #     extent=-220,
            # )
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

            # create_arc(
            #     tractor,
            #     track_dictionary[solution[i]]["down"]["x"],
            #     track_dictionary[solution[i]]["down"]["y"],
            #     track_dictionary[solution[i + 1]]["top"]["x"],
            #     -200,
            #     start=-180,
            #     extent=180,
            # )

    # create_arc(tractor, -480, 200, -435, 0, 0, 180)

    # print (track_dictionary)
    for i in track_dictionary:
        print(i, track_dictionary[i])

    # tractor.clear()


tracks_entry = tk.DoubleVar()
tk.Label(root, text="Enter number of tracks: ").pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X, pady=14)
tk.Entry(root, textvariable=tracks_entry).pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X)

width_entry = tk.DoubleVar()
tk.Label(root, text="Enter width between each track: ").pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X, pady=14)
tk.Entry(root, textvariable=width_entry).pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X)

run_entry = tk.DoubleVar()
tk.Label(root, text="Enter width between each track: ").pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X, pady=14)
tk.Entry(root, textvariable=run_entry).pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X)

tk.Button(root, text="Start", command=start, bg='lightgreen').pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X, pady=14)
tk.Button(root, text="Reset", command=reset, bg='red').pack(ipadx=6, ipady=3, anchor=tk.W, fill=tk.X, pady=4)


root.mainloop()
