"""A plant produces a line of translucent miniature polymer squares. Stringent qual-
ity requirements dictate 100% visual inspection, and the plant manager finds the use
of human inspectors increasingly expensive. Inspection is semiautomated.At each
inspection station, a robotic mechanism places each polymer square over a light
located under an optical system that produces a magnified image of the square.

The image completely fills a viewing screen measuring 80*80 mm. 

Defects appear as dark circular blobs, and the inspector's job is to look at the screen and 
reject any sample that has one or more such 

dark blobs with a diameter of 0.8 mm or larger,

as measured on the scale of the screen. The manager believes that, if she can find
a way to automate the process completely, she will increase profits by 50%. She
also believes that success in this project will aid her climb up the corporate ladder.
After much investigation, the manager decides that the way to solve the problem
is to view each inspection screen with a CCD TV camera and feed the output of the
camera into an image processing system capable of detecting the blobs, measuring
their diameter, and activating the accept/reject buttons previously operated by an
inspector. She is able to find a system that can do the job, as long as 

the smallest defect occupies an area of at least 2*2 pixels in the digital image.

The manager hires you to help her specify the camera and lens system, but requires that you use off-
the-shelf components. For the lenses, assume that this constraint means any 

integer multiple of 25 mm or 35 mm, up to 200 mm. 

For the cameras, it means 

resolutions of 512*512, 1024*1024, or 2048*2048 pixels.

The individual imaging elements in these cameras are 

squares measuring 8*8 um, and the spaces between imaging elements are 2 um. 

For this application, the cameras cost much more than the
lenses, so the problem should be solved with the lowest-resolution camera possible,
based on the choice of lenses. As a consultant, you are to provide a written recom-
mendation, showing in reasonable detail the analysis that led to your conclusion.
Use the same imaging geometry suggested in Problem 2.5."""

from infocusimage import InFocusImage
import math
import numpy as np

# change these according to the lens and sensor options
focal_length = 25 # mm 
resolution = 512 # pixels

# px size specified in problem
px_size = 0.008 # mm
px_spacing = 0.008 # mm


sensor_area = ((resolution*px_size) + ((resolution-1) * px_spacing)) ** 2 # mm^2
sensor_element_count = resolution ** 2 # pixels
sensor_height = np.round(np.sqrt(sensor_area), 0) # mm

# calculate if screen can be viewed 
# with selected lens and sensor at
# reasonable distance
ifi = InFocusImage(focal_length, sensor_area, sensor_element_count)

screen_height = 80 # mm
distance = ifi.calculate_distance_to_object(sensor_height, screen_height)
print("The chosen imaging system has a {} mm chip, and can view the entire screen from {} mm away.".format(sensor_height, distance))

# calculate the area of 4 px required in problem
px_area_4 = 4*(sensor_area/sensor_element_count)

# calculate the object size on the sensor
blob_height = 0.8

ifi = InFocusImage(focal_length, sensor_area, sensor_element_count)
blob_image_size = ifi.calculate_in_focus_image_size(blob_height, distance)
print("tested focal length: {} mm".format(ifi.focal_length))
print("tested chip resolution: {}".format(resolution))
print("Blob image size on sensor: {:2e} mm".format(np.round(blob_image_size, 2)))

# number of px occupied on sensor
px = blob_image_size



