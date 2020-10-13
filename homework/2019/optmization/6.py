import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return -np.sin(x) ** 6 * np.tan(1 - x) * np.exp(10 * x)


# 0.618
def zoe_update_left_interval():
    return a + (1 - 0.618) * (b - a)


def zoe_update_right_interval():
    return a + 0.618 * (b - a)


a = 0
b = 1
Left = zoe_update_left_interval()
Right = zoe_update_right_interval()
resultOne = []

while True:
    if f(Left) <= f(Right):
        b = Right
        Right = Left
        Left = zoe_update_left_interval()
    else:
        a = Left
        Left = Right
        Right = zoe_update_right_interval()
    resultOne.append(f((Left + Right) / 2))
    if (Right - Left) < 10 ** (-9):
        break

print('Step:{}'.format(len(resultOne)) + ' result:x={}'.format((Left +
                                                                Right) / 2) + ' Minimum:{}'.format(resultOne[-1]))

plt.plot(range(len(resultOne)), resultOne, '-', label='0.618')
plt.legend()
plt.figure()
plt.show()

# Fibonacci
Fibonacci = [1, 1]
FibonacciNeeded = 1 / 10 ** (-9)
while Fibonacci[-1] < FibonacciNeeded:
    Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])


def f_update_left_interval():
    temp = a + (Fibonacci[-3] / Fibonacci[-1]) * (b - a)
    return temp


def f_update_right_interval():
    temp = a + (Fibonacci[-2] / Fibonacci[-1]) * (b - a)
    return temp


a = 0
b = 1
Left = f_update_left_interval()
Right = f_update_right_interval()
del Fibonacci[-1]
resultTwo = []

while len(Fibonacci) >= 4:
    if f(Left) <= f(Right):
        b = Right
        Right = Left
        del Fibonacci[-1]
        Left = f_update_left_interval()
    else:
        a = Left
        Left = Right
        del Fibonacci[-1]
        Right = f_update_right_interval()
    resultTwo.append(f((Left + Right) / 2))

print('Step:{}'.format(len(resultTwo)) + ' Results:x={}'.format((Left +
                                                                 Right) / 2) + ' Minimum:{}'.format(resultTwo[-1]))

plt.plot(range(len(resultTwo)), resultTwo, '--', label='Fibonacci')
plt.legend()
plt.figure()
plt.show()

# Quadratic Interpolation
a = 0.1
b = 1
Left = (a + b) / 4
resultThree = []


def minimum():
    down = -((Left - b) * f(a) + (b - a) * f(Left) + (a - Left)
            * f(b)) / (a - Left) * (Left - b) * (b - a)
    up = ((Left ** 2 - b ** 2) * f(a) + (b ** 2 - a ** 2) * f(Left) +
          (a ** 2 - Left ** 2) * f(b)) / (a - Left) * (Left - b) * (b - a)
    return -up / (2 * down)


while True:
    new = minimum()
    if new <= Left:
        b = Left
    else:
        a = Left
    Left = new
    resultThree.append(f(new))
    if len(resultThree) >= 2:
        if abs(resultThree[-1] - resultThree[-2]) < 10 ** (-9):
            break

print('Step:{}'.format(len(resultThree)) +
      ' Results:x={}'.format(Left) + ' Minimum:{}'.format(resultThree[-1]))

plt.plot(range(len(resultThree)), resultThree,
         '-.', label='Quadratic Interpolation')
plt.legend()
plt.figure()
plt.show()
