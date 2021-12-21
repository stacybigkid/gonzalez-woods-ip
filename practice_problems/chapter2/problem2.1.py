from retinalimage import RetinalImage
import numpy as np

'''Using the background information provided in Section 2.1, and thinking purely
in geometric terms, estimate the diameter of the smallest printed dot that the eye
can discern if the page on which the dot is printed is 0.2 m away from the eyes.
Assume for simplicity that the visual system ceases to detect the dot when the
image of the dot on the fovea becomes smaller than the diameter of one recep-
tor (cone) in that area of the retina. Assume further that the fovea can be mod-
eled as a square array of dimensions 1.5 mm*1.5 mm, and that the cones and
spaces between the cones are distributed uniformly throughout this array.'''

# calcuate diameter (width) of 1 cone
r_i = RetinalImage()

# area per cone
cone_area = r_i.foveal_area / r_i.foveal_cone_count

# width of cone (assuming cones are square)
cone_height = np.sqrt(cone_area)

# convert m to mm
object_distance = 0.2 * 10 ** 3

min_viewable_object_size = r_i.calculate_object_size(cone_height, object_distance)

print(f"Assuming that the height and width of an individual cone is {cone_height} mm, "
      f"the minimum viewable diameter of a dot 0.2 m away is {min_viewable_object_size} mm.")