"""Suppose that a flat area with center at x0 , y0  is illuminated by a light source with
intensity distribution

i(x, y) = Ke-[(x - x0)^2 + (y - y0)^2].

Assume for simplicity that the reflectance of the area is constant and equal to
1.0, and let K=255. If the resulting image is digitized with k bits of intensity res-
olution, and the eye can detect an abrupt change of eight shades of intensity be-
tween adjacent pixels, what value of k will cause visible false contouring?"""

import cv2
import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt


bits = list(np.arange(1,9))
bits.reverse()
plots = []
order = 1
for bit_image in bits:
    # set bit_image to the desired gray sampling rate
    gray_levels = 2 ** bit_image
    interval = 256//gray_levels

    # black canvas of specified width and height (wh)
    img_wh = 5
    bg = np.zeros((img_wh, img_wh), np.uint8)

    # find the central pixel
    x0 = img_wh // 2
    y0 = img_wh // 2

    # apply illumination equation defined in problem
    # to background of zeros
    def illuminate(x, y):
        return 255 * np.exp(-(((x - x0) ** 2) + ((y - y0) ** 2)))

    for x in range(img_wh):
        for y in range(img_wh):
            intensity = illuminate(x, y)
            bg[x, y] = intensity

    # resize the image to see the function results clearly
    bg_resized = cv2.resize(bg, (1024, 1024), interpolation=cv2.INTER_CUBIC)

    # bin pixel intensities according to the desired bit image
    bg_resampled = bg_resized.copy()
    for bin in range(0, 255, interval):
        mask = ((bg_resampled>=bin) & (bg_resampled<bin+interval))
        bg_resampled[mask] = bin

    x = np.linspace(-2.5, 2.5, 99)
    i = 255*np.exp(-(x-0)**2)

    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(1, 3, 1)
    plt.imshow(bg_resized, cmap='gray')
    ax.axis('off')
    plt.title('Original Light Source')

    ax = fig.add_subplot(1, 3, 2)
    plt.imshow(bg_resampled,  cmap='gray')
    ax.axis('off')
    plt.title(f'Resampled Image ({bit_image} bits)')

    ax = fig.add_subplot(1, 3, 3)
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the gray level intervals for a given
    # bit image
    for shade in np.arange(0, 255, interval):
        plt.axhline(y=shade, color='y', linestyle='-')

    # plot the function
    plt.plot(x,i, 'b', label='255*np.exp(-(x-0)**2)')
    plt.legend(loc='upper right')

    plt.title("Linear Representation")
    plt.tight_layout()
    # show the plot
    # plt.show()
    plt.savefig(f"{order}_{bit_image}_bit_fig.png")

    order += 1
