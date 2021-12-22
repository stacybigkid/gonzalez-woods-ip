'''You are hired to design the front end of an imaging system for studying the bound-
ary shapes of cells, bacteria, viruses, and protein.The front end consists, in this case,
of the illumination source(s) and corresponding imaging camera(s). The diame-
ters of circles required to enclose individual specimens in each of these categories
are 50, 1, 0.1, and 0.01 um, respectively.
      
      (a) Can you solve the imaging aspects of this problem with a single sensor and
      camera? If your answer is yes, specify the illumination wavelength band and
      the type of camera needed. Identify the camera as being a color camera, far-
      infrared camera, or whatever appropriate name corresponds to the illumi-
      nation source.

      (b) If your answer in (a) is no, what type of illumination sources and corre-
      sponding imaging sensors would you recommend? Specify the light sources
      and cameras as requested in part (a). Use the minimum number of illumina-
      tion sources and cameras needed to solve the problem'''

# min diameters in m
cells = 50 * 10**-6 
bacteria = 1 * 10**-6  
viruses = 0.1 * 10**-6  
protein = 0.01 * 10**-6  

print("""\nThe following wavelengths of radiation are required
to view the specimens of interest:
         cells: {:.2e}
         bacteria: {:.2e}
         viruses: {:.2e}
         protein: {:.2e}""".format(cells, bacteria, viruses, protein))

