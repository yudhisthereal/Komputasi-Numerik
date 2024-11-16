import numpy
import matplotlib.pyplot as plt

def f(x):
    return numpy.sin(10*x) + numpy.cos(3*x)

def bisection(a, b, tolerance=1e-5, max_iterations=100):
    if f(a) * f(b) >= 0:
        return None
    
    for _ in range(max_iterations):
        c = (a + b) / 2
        if abs(f(c)) < tolerance or (b-a) / 2 < tolerance:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c

def find_roots(x_min, x_max, step, tolerance=1e-5):
    roots = []
    x = numpy.arange(x_min, x_max, step)
    for i in range(len(x) - 1):
        root = bisection(x[i], x[i+1], tolerance)
        if root is not None:
            if not roots or (root - roots[-1]) > tolerance:
                roots.append(root)
    
    return roots

x_min, x_max = -2.5, 2.5
step = 0.1
roots = find_roots(x_min, x_max, step)
x = numpy.linspace(x_min, x_max, 1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="f(x) = sin(10x) + cos(3x)")
plt.axhline(0, x_min, x_max, color='black', linewidth=1)
for root in roots:
    plt.plot(root, 0, 'ro')
    plt.text(root, 0.1, f'{root:.3f}', ha='center')

plt.title('Komnum Bisection')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()


