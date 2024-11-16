import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(10*x) + np.cos(3*x)

def bisection(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        return None

    for _ in range(max_iter):
        c = (a + b) / 2

        if abs(f(c)) < tolerance or (b-a) / 2 < tolerance:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c

def find_roots(x_min, x_max, step, tol=1e-5):
    roots = []
    x = np.arange(x_min, x_max, step)
    for i in range(len(x) - 1):
        root = bisection(x[i], x[i+1], tol)
        if root is not None:
            if not roots or abs(root - roots[-1]) > tol:
                roots.append(root)

    return roots

