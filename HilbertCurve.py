import turtle

def hilbert_curve(turtle, order, size, orientation):
    if order == 0:
        return
    else:
        turtle.right(orientation * 90)
        hilbert_curve(turtle, order - 1, size, -orientation)
        turtle.forward(size)
        turtle.left(orientation * 90)
        hilbert_curve(turtle, order - 1, size, orientation)
        turtle.forward(size)
        hilbert_curve(turtle, order - 1, size, orientation)
        turtle.left(orientation * 90)
        turtle.forward(size)
        hilbert_curve(turtle, order - 1, size, -orientation)
        turtle.right(orientation * 90)

def draw_hilbert(order, size):
    screen = turtle.Screen()
    screen.title("Hilbert Curve")
    screen.bgcolor("white")

    hilbert_turtle = turtle.Turtle()
    hilbert_turtle.speed(0)  # Set the fastest drawing speed
    hilbert_turtle.hideturtle()  # Hide the turtle icon

    # Move the turtle to the starting position
    hilbert_turtle.penup()
    hilbert_turtle.goto(-size / 2, -size / 2)
    hilbert_turtle.pendown()

    hilbert_curve(hilbert_turtle, order, size, 1)

    screen.mainloop()

# Пример использования:
order = 4  # Порядок кривой Хилберта
size = 400  # Размер квадрата

draw_hilbert(order, size)
