import sklearn
import matplotlib.pyplot as plt
import numpy as np
import random

x = list(range(0, 50))  # celcius
y = [1.8 * F + 32 + random.randint(-3, 3) for F in x]  # farenheit

print(f'x: {x}')
print(f'y: {y}')

plt.plot(x, y, '-*r')
plt.show()
