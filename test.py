from textwrap import shorten
import turtle 



# bob = turtle.Turtle()

# bob.color("green" , "yellow")

# bob.speed(20)

# bob.penup()
# bob.goto((-200,100))
# bob.pendown()

# def star(bob, size):
#     for j in range(5):
#         if size>=10:
#             for i in range(5):
#                 bob.forward(size)
#                 star(bob,size/3)
#                 bob.left(216)
#         else:
#             return
        


# star(bob,360)

tree = turtle.Turtle()
tree.hideturtle()
tree.setheading(90)
tree.color("green")


def pattern(tree, branch_length, shorten_by, angle):

    MIN_LENGTH = branch_length/2

    new_length = branch_length - shorten_by

    if branch_length > MIN_LENGTH

    tree.forward(branch_length)

    tree.left(angle)
        pattern(tree, new_length, shorten_by, angle)

    tree.right(angle)
    

turtle.mainloop()