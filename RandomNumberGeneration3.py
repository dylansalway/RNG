import numpy as np
import matplotlib.pyplot as plt
import secrets

def generate_uniform_circle_interior(num_points, radius):
    r = np.sqrt(np.random.uniform(0, radius**2, num_points))
    theta = np.random.uniform(0, 2*np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def generate_normal_circle_interior(num_points, radius, mean=0, std_dev=1):
    r = np.abs(np.random.normal(mean, std_dev, num_points))
    r = np.clip(r, 0, radius)
    theta = np.random.uniform(0, 2*np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def linear_congruential_generator_interior(seed, a, c, m, num_points, radius):
    random_numbers = []
    for _ in range(num_points):
        seed = (a * seed + c) % m
        random_numbers.append(seed / m)
    r = np.sqrt(random_numbers) * radius
    theta = np.random.uniform(0, 2*np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

lcg_seed = 12345
lcg_a = 54321
lcg_c = 67890
lcg_m = 2**32

num_points = 5000
radius = 1.0

random_numbers_lcg_interior = linear_congruential_generator_interior(lcg_seed, lcg_a, lcg_c, lcg_m, num_points, radius)
x_lcg, y_lcg = random_numbers_lcg_interior

def mersenne_twister_generator(num_points):
    r = np.random.rand(num_points)
    theta = np.random.uniform(0, 2*np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x_mt, y_mt = mersenne_twister_generator(num_points)

def xorshift_generator(seed, num_points):
    random_numbers = []
    divisor = np.uint64(2) ** 64
    for _ in range(num_points):
        seed = np.uint64(seed)
        seed ^= (seed << np.uint64(21))
        seed ^= (seed >> np.uint64(35))
        seed ^= (seed << np.uint64(4))
        random_numbers.append(seed / divisor)
    return random_numbers

xorshift_seed = 123456789
random_numbers_xorshift = xorshift_generator(xorshift_seed, num_points)
random_angles_xorshift = np.random.uniform(0, 2*np.pi, num_points)
x_xorshift = random_numbers_xorshift * np.cos(random_angles_xorshift)
y_xorshift = random_numbers_xorshift * np.sin(random_angles_xorshift)

def crypto_secure_generator_interior(num_points, radius):
    random_numbers = [secrets.randbelow(2**64) for _ in range(num_points)]
    r = np.sqrt(random_numbers) * radius
    theta = np.random.uniform(0, 2*np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x_crypto_secure, y_crypto_secure = crypto_secure_generator_interior(num_points, radius)
radius = 1.0

x_uniform_circle_interior, y_uniform_circle_interior = generate_uniform_circle_interior(num_points, radius)
x_normal_circle_interior, y_normal_circle_interior = generate_normal_circle_interior(num_points, radius)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.title('Uniformly Distributed Points')
plt.scatter(x_uniform_circle_interior, y_uniform_circle_interior, s=0.5)
plt.axis('equal')

plt.subplot(2, 3, 2)
plt.title('Normally Distributed Points')
plt.scatter(x_normal_circle_interior, y_normal_circle_interior, s=0.5)
plt.axis('equal')

plt.subplot(2, 3, 3)
plt.title('Linear Congruential Generated Points')
plt.scatter(x_lcg, y_lcg, s=0.5)
plt.axis('equal')

plt.subplot(2, 3, 4)
plt.title('Mersenne Twister Generated Points')
plt.scatter(x_mt, y_mt, s=0.5)
plt.axis('equal')

plt.subplot(2, 3, 5)
plt.title('Xorshift Generated Points')
plt.scatter(x_xorshift, y_xorshift, s=0.5)
plt.axis('equal')

plt.subplot(2, 3, 6)
plt.title('Crypto Secure Generated Points')
plt.scatter(x_crypto_secure, y_crypto_secure, s=0.5)
plt.axis('equal')

plt.show()
