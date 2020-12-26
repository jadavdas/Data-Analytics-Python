# %% SciPy Tutorial

'''SciPy is a very popular library among Machine Learning enthusiasts as it contains different modules for optimization,
linear algebra, integration and statistics. There is a difference between the SciPy library and the SciPy stack.
The SciPy is one of the core packages that make up the SciPy stack. SciPy is also very useful for image manipulation.
'''
import numpy as np
from scipy.misc import imread, imsave, imresize
from scipy.spatial.distance import pdist, squareform

# Read a JPEG image into a numpy array
img = imread('cat.jpg')  # path of the image
print(img.dtype, img.shape)

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
img_tint = img * [1, 0.45, 0.3]

# Saving the tinted image
imsave('cat_tinted.jpg', img_tint)

# Resizing the tinted image to be 300 x 300 pixels
img_tint_resize = imresize(img_tint, (300, 300))

# Saving the resized tinted image
imsave('cat_tinted_resized.jpg', img_tint_resize)

# Create the following array where each row is a point in 2D space:
# [[0 1]
#  [1 0]
#  [2 0]]
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

# Compute the Euclidean distance between all rows of x.
# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
d = squareform(pdist(x, 'euclidean'))
print(d)