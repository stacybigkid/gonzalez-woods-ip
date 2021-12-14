
class RetinalImage:
    def __init__(self, height, distance):
        
        self.object_height = height
        self. object_distance = distance

        self.eye_focal_length = 17

    def calculate_retinal_image_size(self):
        return (self.object_height * self.eye_focal_length) / self.object_distance

# input height and distance must be in meters (m)
r_i = RetinalImage(15, 100)
print(f"The the retinal image height of the input object is {r_i.calculate_retinal_image_size()} mm")

