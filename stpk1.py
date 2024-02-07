import turtle as t


def square(size=50, col='blue'):
    # рисовать квадрат со стороной size цветом col
    t.color(col)  # установили цвет col
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)



square(col='red')

square(100)
