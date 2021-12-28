"""Suppose that a flat area with center at Ax 0 , y 0 B is illuminated by a light source with
intensity distribution

i(x, y) = Ke-[(x - x 0)^2 + (y - y 0)^2].


Assume for simplicity that the reflectance of the area is constant and equal to
1.0, and let K=255. If the resulting image is digitized with k bits of intensity res-
olution, and the eye can detect an abrupt change of eight shades of intensity be-
tween adjacent pixels, what value of k will cause visible false contouring?"""

import numpy as np
import matplotlib.pyplot as plt

bits = 4

x = np.linspace(-2.5, 2.5, 99)
i = 255*np.exp(-1*(x-0)**2)

shades_per_bit = 256 / 2 ** bits

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

for shade in np.arange(0, 255, shades_per_bit):
    plt.axhline(y=shade, color='y', linestyle='-')

# plot the function
plt.plot(x,i, 'b', label='i = 255*np.exp(-1*(x-0)**2)')
plt.legend(loc='upper right')

plt.title(f"8 bit image sampled at {bits} bits\nEach interval includes {shades_per_bit} gray levels per bit.")

# show the plot
plt.show()

