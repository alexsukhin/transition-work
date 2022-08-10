import turtle

t = turtle.Turtle()
n = 36

for i in range(10):
  t.left(30)
  t.forward(50)
  t.right(60)
  t.forward(50)
  t.right(120)
  t.forward(50)
  t.right(60)
  t.forward(50)
  t.home()
  t.right(n)
  n += 36
