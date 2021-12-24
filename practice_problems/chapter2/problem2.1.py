from infocusimage import InFocusImage
import numpy as np

'''Using the background information provided in Section 2.1, and thinking purely
in geometric terms, estimate the diameter of the smallest printed dot that the eye
can discern if the page on which the dot is printed is 0.2 m away from the eyes.
Assume for simplicity that the visual system ceases to detect the dot when the
image of the dot on the fovea becomes smaller than the diameter of one recep-
tor (cone) in that area of the retina. Assume further that the fovea can be mod-
eled as a square array of dimensions 1.5 mm*1.5 mm, and that the cones and
spaces between the cones are distributed uniformly throughout this array.'''

ifi = InFocusImage()

# calculate area per cone
cone_area = ifi.sensor_area / ifi.sensor_element_count

# width of cone (assuming cones are square)
# divide by 2 to account for 
# evenly distributed spaces between cones
cone_height = np.sqrt(cone_area) / 2

# mm
object_distance = 200 

min_viewable_object_size = ifi.calculate_object_size(cone_height, object_distance)

print("Assuming that the height and width of an individual cone is {:.2e} mm, ".format(cone_height),
      "the minimum viewable diameter of a dot 0.2 m away is {:.2e} mm.".format(min_viewable_object_size))