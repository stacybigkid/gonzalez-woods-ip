class RetinalImage:
    def __init__(self):
        
        self.eye_focal_length = 17 # mm
        self.foveal_area = 1.5 ** 2 # mm^2
        self.foveal_cone_count = 3.37 * 10**5 # total cone count within fovea
        self.foveal_density_per_mm_2 = 1.5 * 10**5 # cones/mm^2

    def calculate_retinal_image_size(self, height, distance):
        # input height and distance must be in meters
        return (height * self.eye_focal_length) / distance

r_i = RetinalImage()
print(f"The the retinal image height of the input object is {r_i.calculate_retinal_image_size(15, 100)} mm")

