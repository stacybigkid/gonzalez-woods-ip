"""Suppose that a flat area with center at x0 , y0  is illuminated by a light source with
intensity distribution

i(x, y) = Ke-[(x - x0)^2 + (y - y0)^2].

Assume for simplicity that the reflectance of the area is constant and equal to
1.0, and let K=255. If the resulting image is digitized with k bits of intensity res-
olution, and the eye can detect an abrupt change of eight shades of intensity be-
tween adjacent pixels, what value of k will cause visible false contouring?"""

import cv2
import numpy as np
import math

# set bit_image to the desired gray sampling rate
bit_image = 5
gray_levels = (2 ** bit_image) - 1
interval = 255//gray_levels

# black canvas of specified width and height (wh)
img_wh = 5
bg = np.zeros((img_wh, img_wh), np.uint8)

# find the central pixel
x0 = img_wh // 2
y0 = img_wh // 2

# apply illumination eqation defined in problem
# to background of zeros
def illuminate(x, y):
    return 255 * np.exp(-1 * (((x - x0) ** 2) + ((y - y0) ** 2)))

for x in range(img_wh):
    for y in range(img_wh):
        intensity = illuminate(x, y)
        bg[x, y] = intensity

# resize the image to see the function clearly
bg_resized = cv2.resize(bg, (512, 512), interpolation=cv2.INTER_CUBIC)

# bin pixel intensities according to the desired bit image
bg_resampled = bg_resized.copy()
for bin in range(0, 255, interval):
    mask = ((bg_resampled>bin) & (bg_resampled<=bin+interval))
    bg_resampled[mask] = bin

print(len(np.unique(bg_resampled)))

cv2.imshow('bg', bg_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('bg', bg_resampled)
cv2.waitKey(0)
cv2.destroyAllWindows()
