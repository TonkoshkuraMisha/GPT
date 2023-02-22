def draw_figure(width, height):
    if width < 2 or height < 2:
        print("Width and height must be at least 2")
        return

    # draw top border
    print("#" * width)

    # draw sides and center
    for i in range(1, height - 1):
        if i % 2 == 1:
            print("#" + "@" * (width - 2) + "#")
        else:
            if i == (height // 2):
                s = "!" * (width - 2)
                if width > 2:
                    s = s[:width // 2 - 1] + "@" + s[width // 2:]
                print("#@" + s + "@#")
            else:
                print("#!" + " " * (width - 4) + "!#")

    # draw bottom border
    print("#" * width)

# test the function
draw_figure(14, 12)
