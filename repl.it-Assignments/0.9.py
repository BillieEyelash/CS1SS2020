# create a polygon using the user's choice of sides, color, and size
import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()

def shape(color, size, sides):
  for i in range(sides):
    t1.pencolor(color)
    t1.forward(size)
    t1.right(float(360/sides))
  print(float(360/sides))

color = input('Enter a color: ')
while True:
  try:
   size = int(input('Enter a size: '))
   break
  except:
    continue
while True:
  try:
    sides = int(input('Enter the number of sides: '))
    break
  except:
    continue

shape(color, size, sides)

wn.mainloop()
