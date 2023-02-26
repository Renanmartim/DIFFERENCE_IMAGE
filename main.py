import numpy as np
from skimage import io, img_as_float, img_as_ubyte

# Load the two images
image1 = img_as_float(io.imread('image1.jpg', as_gray=True))
image2 = img_as_float(io.imread('image2.jpg', as_gray=True))

# Convert the images to the same data type
image1 = img_as_ubyte(image1)
image2 = img_as_ubyte(image2)

# Compute the absolute difference between the two images
diff = np.abs(image1 - image2)

# Save the difference image
io.imsave('diff.jpg', diff)

# Compute the mean difference between the two images
mean_diff = np.mean(diff)

print(f"Mean difference between the images: {mean_diff}")
