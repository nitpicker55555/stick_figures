import matplotlib.pyplot as plt
import numpy as np

# Set the random seed for reproducibility
np.random.seed(4)


# Function to plot the stick figure
def plot_stick_figure(angles):
    # Define the figure and axis
    fig, ax = plt.subplots()

    # Starting point for the drawing
    start_point = np.array([0, 0])
    points = [start_point]

    # Each limb is represented by a line segment in polar coordinates, with a length of 1
    # We'll convert polar coordinates (angle, length) to cartesian coordinates (x, y)
    for angle in angles:
        end_point = start_point + np.array([np.cos(angle), np.sin(angle)])
        ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], marker='o')
        points.append(end_point)
        start_point = end_point

    # Set the plot limits
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    # Equal aspect ratio ensures that the stick figure proportions are correct
    ax.set_aspect('equal')

    # Hide the axes
    ax.axis('off')

    # Show the plot
    plt.show()


# Generate 5 random angles in radians between 0 and 2*pi
random_angles = np.random.rand(5) * 2 * np.pi

# Call the function to plot the stick figure with random angles
plot_stick_figure(random_angles)
