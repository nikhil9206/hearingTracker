import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the lines
ax.plot(x, y1, label='sin(x)')
ax.plot(x, y2, label='cos(x)')

# Fill the area between the lines
ax.fill_between(x, y1, y2, alpha=0.3)

# Add a legend
ax.legend()

# Show the plot
plt.show()