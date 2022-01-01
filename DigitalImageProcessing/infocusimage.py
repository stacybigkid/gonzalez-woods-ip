class InFocusImage:
    """A class to calculate either the size of an in focus image on a sensor
    of known dimensions or the size of an object from a known in-focus image. 
    Default values correspond to the focal length (in mm)
    foveal area (mm^2), and number of cones in the human eye."""

    def __init__(self, focal_length, sensor_area = 1.5 ** 2, sensor_element_count=3.37 * 10**5):
        
        self.focal_length = focal_length # mm
        self.sensor_area = sensor_area # mm^2
        self.sensor_element_count = sensor_element_count # total cone count within fovea
        # self.foveal_density_per_mm_2 = 1.5 * 10**5 # cones/mm^2

    def calculate_in_focus_image_size(self, object_height, object_distance):
        # input height and distance must be the same metric unit
        # output in mm
        return object_height * (self.focal_length / object_distance)

    def calculate_object_size(self, image_height, object_distance):
        # input height and distance must be in same unit (mm or m)
        # output in m
        return image_height / self.focal_length * object_distance

    def calculate_focal_length(self, image_height, distance_to_object, object_height):
        return distance_to_object * image_height / object_height

    def calculate_distance_to_object(self, image_height, object_height):
        return self.focal_length * object_height / image_height



if __name__ == "__main__":
    ifi = InFocusImage()
    h = 15000 
    d = 100000 
    unit = 'mm'
    print( f"A {h} {unit} high object viewed "
        f"at a distance of {d} {unit} produces "
        f"a retinal image {ifi.calculate_retinal_image_size(15, 100)} mm "
            "in height.")

