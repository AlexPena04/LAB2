import time
import random
from graphics import *

winWidth, winHeight = 400, 500
ballRadius = 10
ballColor = 'red'
numBalls = 10
delay = .005
runFor = 30  # in seconds

# create 10 balls, randomly located
def makeBalls(xLow, xHigh, yLow, yHigh):

    balls = []

    for _ in range(numBalls):
        center = getRandomPoint(xLow, xHigh, yLow, yHigh)

        aBall = Circle(center, ballRadius)
        aBall.setFill(ballColor)
        aBall.draw(win)
        balls.append(aBall)

    return balls

# animate 10 balls bouncing off edges of window
def bounceInWin(shapes, dx, dy, xLow, xHigh, yLow, yHigh):
    movedShapes = [(getRandomDirection(dx, dy), shape) for shape in shapes]

    start_time = time.time()

    while time.time() < start_time + runFor:
        shapes = movedShapes
        movedShapes = []

        for (dx, dy), shape in shapes:
            shape.move(dx, dy)
            center = shape.getCenter()

            x = center.getX()
            if x < xLow or x > xHigh:
                dx = -dx

            y = center.getY()
            if y < yLow or y > yHigh:
                dy = -dy

            # Could be so much simpler if Point had setX() and setY() methods
            movedShapes.append(((dx, dy), shape))

        time.sleep(delay)

# get a random direction
def getRandomDirection(dx, dy):
    x = random.randrange(-dx, dx)
    y = random.randrange(-dy, dy)

    return x, y

# get a random Point
def getRandomPoint(xLow, xHigh, yLow, yHigh):
    x = random.randrange(xLow, xHigh + 1)
    y = random.randrange(yLow, yHigh + 1)

    return Point(x, y)

# make balls bounce
def bounceBalls(dx, dy):

    xLow = ballRadius * 2
    xHigh = winWidth - ballRadius * 2
    yLow = ballRadius * 2
    yHigh = winHeight - ballRadius * 2

    balls = makeBalls(xLow, xHigh, yLow, yHigh)

    win.getMouse()

    bounceInWin(balls, dx, dy, xLow, xHigh, yLow, yHigh)

# create screen
win = GraphWin('Ball Bounce', winWidth, winHeight)

bounceBalls(3, 5)

# wait for another click to end program
win.getMouse()
win.close()
