from infocusimage import InFocusImage
import numpy as np

'''A CCD camera chip of dimensions 7*7 mm, and having 1024*1024 elements,
is focused on a square, flat area, located 0.5 m away. How many line pairs per mm
will this camera be able to resolve? The camera is equipped with a 35-mm lens.
(Hint: Model the imaging process as in Fig. 2.3, with the focal length of the cam-
era lens substituting for the focal length of the eye.)'''

ifi = InFocusImage(focal_length=35, sensor_area=7*7, sensor_element_count=1024*1024)

# calculate area per cone
pixel_area = ifi.sensor_area / ifi.sensor_element_count

# width of pixel (assuming cones are square)
pixel_size = np.sqrt(pixel_area)

# mm
object_distance = 500

min_viewable_object_size = round(ifi.calculate_object_size(pixel_size, object_distance), 2)

print("\nThe height and width of an individual pixel is {:.2e} mm in the specified imaging system.".format(pixel_size),
      "The minimum object width viewed from {} mm away is therefore {} mm.".format(object_distance, min_viewable_object_size))

line_pair_thickness = round(min_viewable_object_size*2, 2)
line_pairs_per_mm = int(1/line_pair_thickness)
print("\nAssuming that a line pair consists of 2 'objects', the minimum width "
      "of a resolvable line pair is {:2} mm. {} line pairs can therefore be imaged per mm.".format(line_pair_thickness, line_pairs_per_mm))
