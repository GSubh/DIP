# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
Lenna = cv2.imread('test_img1.png')

# Plot the original image
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(Lenna)


# Create the sharpening kernel
x = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Sharpen the image
Lemma2 = cv2.filter2D(Lenna, -1, x)

# Save the image
cv2.imwrite('SharpenImage.jpg', Lemma2)

# Plot the sharpen image
plt.subplot(1, 2, 2)
plt.title("Sharpen")
plt.imshow(Lemma2)
plt.show()
