from electromagneticspectrum import ElectromagneticSpectrum

'''Although it is not shown in Fig. 2.10, alternating current certainly is part of the
electromagnetic spectrum. Commercial alternating current in the United States
has a frequency of 60 Hz.What is the wavelength in kilometers of this component
of the spectrum?'''

es = ElectromagneticSpectrum()

# calculate wavelength from given frequency
lmda = es.calculate_wavelength(60)

# anwer in km
lmda = lmda / 1000

print("Commercial alternating current has a wavelength "
      "of {0} km.".format(round(lmda)))