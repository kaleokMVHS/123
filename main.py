#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

active_apples = []
inactive_apples = []

possible_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(apple):
  apple.shape(apple_image)
  wn.update()

def fall(apple):
  if (apple in inactive_apples):
    return

  turt = apple[0]
  ydist = apple[2]
  turt.pu()
  turt.clear()
  turt.speed(5)
  turt.setheading(270)

  turt.forward(ydist + 100)
  
  turt.hideturtle()
  reset_apple(apple)
  place_apples()

def draw_letter(apple, letter):
  font_setup = ("Arial", 45, "normal")
  wn.tracer(False)
  xcor = apple.xcor()
  ycor = apple.ycor()
  apple.goto(apple.xcor() - 18, apple.ycor() - 40)
  apple.write(letter, font=font_setup)
  apple.goto(xcor, ycor)
  wn.tracer(True)
  wn.update()

def reset_apple(apple):
  active_apples.pop(active_apples.index(apple))
  inactive_apples.append(apple)

def setup_apple(apple):
  turt = apple[0]
  turt.hideturtle()
  ycor = rand.randint(0, 110)
  turt.goto(rand.randint(-200, 200), ycor)
  apple[2] = ycor
  wn.onkeypress(lambda: fall(apple), apple[1])
  wn.listen()
  draw_letter(turt, apple[1])
  turt.showturtle()

def create_apples():
  for letter in possible_letters:
    apple = trtl.Turtle()
    apple.hideturtle()
    apple.pu()
    ycor = 'ycor placeholder'
    inactive_apples.append([apple, letter, ycor])

def place_apples(num=1):
  for i in range(0, num):
    apple_info = rand.choice(inactive_apples)
    print(apple_info)
    apple = apple_info[0]
    draw_apple(apple)
    setup_apple(apple_info)
    active_apples.append(apple_info)
    inactive_apples.pop(inactive_apples.index(apple_info))
    draw_letter(apple, apple_info[1])

#-----function calls-----

wn.bgpic('background.gif')

create_apples()
place_apples(5)

wn.listen()
wn.mainloop()

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

# for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.
