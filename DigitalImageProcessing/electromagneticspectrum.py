class ElectromagneticSpectrum:
    def __init__(self):

        self.c = 2.998 * 10**8 # meters/sec
        
        def calculate_wavelength(self, v):
            # input v is frequency in hertz (Hz)
            return self.c/v # meters

        def calculate_frequency(self, lmda):
            # input lmda is wavelength in meters
            return self.c/lmda # Hz