import numpy as np
import matplotlib.pyplot as plt

# This script should aid in explaining the Van de Vooren transformation

# 1. Create an array of angles
theta = np.linspace(0, 2 * np.pi, 100)

# 2. Setup the required parameters
tau = np.radians(15) # Trailing edge thickness
k = (2 * np.pi - tau) / np.pi 
e = 0.025 # Thickness parameter
l = 0.5 # Trailing edge x-coordinate
a = 2 * l * np.power(e + 1, k - 1) / np.power(2, k) # Radius of the circle

# 3. Create the circle in the complex plane
circle = a * np.cos(theta) + a * 1j * np.sin(theta)

# 4. Transform the circle to the airfoil in the complex plane
airfoil = np.power(circle - a, k) / np.power(circle - a * e, k - 1) + l

# 5. Plot the circle and the airfoil
plt.plot(circle.real, circle.imag, color='r')
plt.plot(airfoil.real, airfoil.imag, color='b')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axis('equal')
plt.show()
