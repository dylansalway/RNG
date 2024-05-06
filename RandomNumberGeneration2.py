import numpy as np
import matplotlib.pyplot as plt

def generate_points(num_points):
    points = []
    for _ in range(num_points):
        radius = 10 * np.sqrt(np.random.random())
        angle = np.random.uniform(0, 2*np.pi)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append((x, y))
    
    for i in range(num_points):
        radius = 10 * np.sqrt(np.abs(np.random.normal()))
        angle = np.arctan2(points[i][1], points[i][0])  
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points[i] = (x, y)
    
    for i in range(num_points):
        radius = 10 * np.sqrt(np.abs(np.random.exponential()))
        angle = np.arctan2(points[i][1], points[i][0])
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points[i] = (x, y)
    
    for i in range(num_points):
        radius = 10 * np.sqrt(np.abs(np.random.laplace()))
        angle = np.arctan2(points[i][1], points[i][0])  
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points[i] = (x, y)

    for i in range(num_points):
        x = points[i][0]
        y = points[i][1]
    if x >= 0 and y >= 0:
        points[i] = (np.sqrt(x), np.sqrt(y))
    else:
        points[i] = (0, 0)

    return points

num_points = 20000

points = generate_points(num_points)

plt.figure(figsize=(8, 8))
plt.title('Sequentially Generated Points on Circle with Final Square Root')
plt.scatter([point[0] for point in points], [point[1] for point in points], s=1)
plt.axis('equal')
plt.show()
