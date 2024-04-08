import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x, y):
    return 9 - x**2 - y**2

# Define the region (circle centered at the origin with radius r)
r = 3
x = np.linspace(-r, r, 400)
y_upper = np.sqrt(9 - x**2)
y_lower = -np.sqrt(9 - x**2)

# Plot the function and the boundary
plt.figure(figsize=(8, 6))
plt.plot(x, y_upper, 'b', label='Upper Boundary')
plt.plot(x, y_lower, 'r', label='Lower Boundary')
plt.fill_between(x, y_upper, y_lower, color='gray', alpha=0.2, label='Region')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Boundary of $f(x, y) = 9 - x^2 - y^2$ within Circle of Radius 3')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
