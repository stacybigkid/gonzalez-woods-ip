from random import randint

class WeberTest:
    def __init__(self):
        
        self.background_intensity = randint(0, 128)
        self.delta_i = randint(0, 128)
        self.center_intensity = self.background_intensity + self.delta_i

        def get_background():
            



