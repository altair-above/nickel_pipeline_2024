import numpy as np

# For the Nickel Telescope original science camera
plate_scale_approx = 0.37
ccd_shape = np.array([1024, 1024])
fov_shape = np.array([1024, 1056])

sat_columns = [255]

bad_columns = [255, 256, 783, 784, 1002]
bad_triangles = [((0, 960), (64, 1024), (0, 1024)), ((0, 33), (34, 0), (0, 0))]
bad_rectangles = []

# Labels for different types of astronomical frames
bias_label = 'Bias'
dome_flat_label = 'Dome flat'
sky_flat_label = 'Flat'
dark_label = 'dark'
focus_label = 'focus'

# For slow readout speed and 2x2 binning
gain = 1.8
read_noise = 10.7