import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return np.sin(10*x) + np.cos(3*x)

# Bisection method to find roots
def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        return None  # The bisection method requires f(a) and f(b) to have opposite signs
    
    for _ in range(max_iter):
        c = (a + b) / 2  # Midpoint
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c  # Root found within tolerance
        if f(c) * f(a) < 0:
            b = c  # Root is in the left half
        else:
            a = c  # Root is in the right half
    return c

# Find all roots within a given interval using bisection
def find_roots(f, x_min, x_max, step=0.1):
    roots = []
    x = np.arange(x_min, x_max, step)
    for i in range(len(x) - 1):
        root = bisection(f, x[i], x[i+1])
        if root is not None:
            # Ensure the root is not already in the list (within tolerance)
            if not roots or abs(root - roots[-1]) > 1e-5:
                roots.append(root)
    return roots

# Define the interval and find the roots
x_min, x_max = -2.5, 2.5
roots = find_roots(f, x_min, x_max)

# Plot the function and its roots
x_vals = np.linspace(x_min, x_max, 1000)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = sin(10x) + cos(3x)')
plt.axhline(0, color='black',linewidth=1)

# Plot the roots
for root in roots:
    plt.plot(root, 0, 'ro')  # Red dots for roots
    plt.text(root, 0.5, f'{root:.3f}', ha='center')

plt.title('Roots of f(x) = sin(10x) + cos(3x) using Bisection Method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(roots)
