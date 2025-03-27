import turtle

# Opret en skærm
screen = turtle.Screen()
screen.bgcolor("white")

# Opret en turtle
pen = turtle.Turtle()
pen.speed(0)  # Sæt høj hastighed
pen.color("green")
pen.fillcolor("lightblue")

# Tegn figuren
for count in range(1, 31):  # Loop fra 1 til 30
    angle = count * 5
    size = 150 - (count * 5)

    # Tegn en firkant
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

    # Rotér for næste firkant
    pen.right(angle)

# Afslut programmet
turtle.done()