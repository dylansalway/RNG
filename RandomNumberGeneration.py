import numpy as np
import matplotlib.pyplot as plt

num_points = 4000 #originally 7000 however I found around 4000 showed up best on the graphs

fig, axs = plt.subplots(2, 5, figsize=(20, 4))

for i, process in enumerate(['uniform', 'SQRTuniform', 'normal',  'SQRTnormal', 'exponential', 'SQRTexponential', 'poisson', 'SQRTpoisson', 'laplace','SQRTlaplace']):
    if process == 'uniform':
        radius = 10 * np.random.random(num_points)
    elif process == 'SQRTuniform':
        radius = 10 * np.sqrt(np.random.random(num_points))
    elif process == 'normal':
        radius = 10 * np.abs(np.random.normal(size=num_points))
    elif process == 'SQRTnormal':
        radius = 10 * np.sqrt(np.abs(np.random.normal(size=num_points)))
    elif process == 'exponential':
        radius = 10 * np.abs(np.random.exponential(size=num_points))
    elif process == 'SQRTexponential':
        radius = 10 * np.sqrt(np.abs(np.random.exponential(size=num_points)))
    elif process == 'poisson':
        radius = 10 * np.abs(np.random.poisson(size=num_points))
    elif process == 'SQRTpoisson':
        radius = 10 * np.sqrt(np.abs(np.random.poisson(size=num_points)))
    elif process == 'laplace':
        radius = 10 * np.abs(np.random.laplace(size=num_points))
    elif process == 'SQRTlaplace':
        radius = 10 * np.sqrt(np.abs(np.random.laplace(size=num_points)))

    theta = 2 * np.pi * np.random.random(num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    axs[i // 5, i % 5].scatter(x, y, s=0.4, alpha=0.5)
    axs[i // 5, i % 5].set_title(f'{process} Distribution')

fig, axs = plt.subplots(1, 2, figsize=(20, 4))

for i, process in enumerate(['multinomial', 'SQRTmultinomial']):
    if process == 'multinomial':
        n = 10
        p = [0.2, 0.3, 0.5]
        radius = 10 * np.abs(np.sqrt(np.random.multinomial(n, p, size=num_points)))
    elif process == 'SQRTmultinomial':
        n = 10
        p = [0.2, 0.3, 0.5]
        radius = 10 * np.sqrt(np.abs(np.random.multinomial(n, p, size=num_points)))

    theta = 2 * np.pi * np.random.random(num_points)
    theta = theta[:, np.newaxis]
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    axs[i].scatter(x, y, s=0.4, alpha=0.5)
    axs[i].set_title(f'{process} Distribution')

plt.tight_layout()
plt.show()
