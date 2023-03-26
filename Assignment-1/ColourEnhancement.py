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

# Convert the image from BGR to HSV color space
Lenna = cv2.cvtColor(Lenna, cv2.COLOR_RGB2HSV)

# Adjust the hue, saturation, and value of the image
# Adjusts the hue by multiplying it by 0.7
Lenna[:, :, 0] = Lenna[:, :, 0] * 0.7
# Adjusts the saturation by multiplying it by 1.5
Lenna[:, :, 1] = Lenna[:, :, 1] * 1.5
# Adjusts the value by multiplying it by 0.5
Lenna[:, :, 2] = Lenna[:, :, 2] * 0.5

# Convert the image back to BGR color space
Lenna2 = cv2.cvtColor(Lenna, cv2.COLOR_HSV2BGR)

# Save the image
cv2.imwrite('EnhancedColoured.jpg', Lenna2)

# Plot the enhanced image
plt.subplot(1, 2, 2)
plt.title("Enhanced Coloured")
plt.imshow(Lenna2)
plt.show()
