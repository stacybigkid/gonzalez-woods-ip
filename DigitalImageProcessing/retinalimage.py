
class RetinalImage:
    def __init__(self, height, distance):
        
        self.object_height = height
        self. object_distance = distance

        self.eye_focal_length = 17
        self.foveal_area = 1.5 ** 2
        self.foveal_cone_count = 337000
        self.foveal_density_per_mm_2 = 150000

    def calculate_retinal_image_size(self):
        return (self.object_height * self.eye_focal_length) / self.object_distance

# input height and distance must be in meters (m)
r_i = RetinalImage(15, 100)
print(f"The the retinal image height of the input object is {r_i.calculate_retinal_image_size()} mm")

