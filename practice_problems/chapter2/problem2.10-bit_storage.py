"""High-definition television (HDTV) generates images with a resolution of 1125
horizontal TV lines interlaced (where every other line is painted on the tube face
in each of two fields, each field being 1/60th of a second in duration). The width-
to-height aspect ratio of the images is 16 : 9. The fact that the horizontal lines are
distinct fixes the vertical resolution of the images. A company has designed an
image capture system that generates digital images from HDTV images. The res-
olution of each TV (horizontal) line in their system is in proportion to vertical res-
olution, with the proportion being the width-to-height ratio of the images. Each
pixel in the color image has 24 bits of intensity resolution, 8 pixels each for a red,
a green, and a blue image.These three “primary” images form a color image. How
many bits would it take to store a 2-hour HDTV program?"""

program_duration_hrs = 2
program_duration_min = program_duration_hrs * 60
program_duration_sec = program_duration_min * 60

images_per_sec = 30

num_px_rows = 1125
num_px_cols = int(num_px_rows * (16/9))

total_px = num_px_rows * num_px_cols
bits_per_image = total_px * 24

total_bits = (images_per_sec * program_duration_sec * bits_per_image)

print("The 2 hr film would require {:2e} bits of storage,".format(total_bits))

byts = total_bits / 8

print("or {:2e} bytes.".format(byts))
