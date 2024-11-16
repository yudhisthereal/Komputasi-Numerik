import numpy as np
import matplotlib.pyplot as plt

f1_text = 'x^10 - 1'
f2_text = 'cos(5x) - sin(3x)'
f3_text = 'x^3 - 2x^2 - 6x + 5'

def f1(x):
    return x**10 - 1

def f2(x):
    return np.cos(5*x) - np.sin(3*x)

def f3(x):
    return x**3 - 2*(x**2) - 6*x + 5

def regula_falsi(a, b, f, tol=1e-1, max_iter=10000):
    cp = a
    if f(a) * f(b) >= 0:
        return None

    n = 0
    e = 1000
    print("R: Iter\t a\t b\t c\t f(c)\t e")
    while abs(e) > tol or n < max_iter:
        c = b - (f(b) * (a-b))/(f(a) - f(b))
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        
        cc = c
        e = ((cc-cp/cc))*100
        print(f'{n}\t {a}\t {b}\t {c}\t {f(c)}\t {e}')
        n += 1
        cp = cc

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c
        

def bisection(a, b, f, tol=1e-1, max_iter=10000):
    if f(a) * f(b) >= 0:
        return None
    print("B: Iter\t a\t b\t c\t f(c)\t")
    for i in range(max_iter):
        c = (a + b) / 2
        print(f'{i}\t {a}\t {b}\t {c}\t {f(c)}')
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

def find_roots(min_x, max_x, method, f, tol=1e-3, step=0.1):
    roots = []
    x = np.arange(min_x, max_x, step)
    for i in range(len(x) - 1):
        root = method(x[i], x[i + 1], f)
        if root is not None:
            if not roots or abs(root - roots[-1]) > tol:
                roots.append(root)
    return roots


def main(f, f_name):
    # Define the interval and find the roots
    x_min, x_max = 0.9, 1.2
    roots = find_roots(x_min, x_max, bisection, f)
    x_vals = np.linspace(x_min, x_max, 1000)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {f_name}')
    plt.axhline(0, color='black',linewidth=1)

    # Plot the roots
    for root in roots:
        plt.plot(root, 0, 'ro')  # Red dots for roots
        plt.text(root, 0.5, f'{root:.3f}', ha='center')

    plt.title(f'Roots of f(x) = {f_name} using Bisection Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Define the interval and find the roots
    x_min, x_max = 0, 3
    roots = find_roots(x_min, x_max, regula_falsi, f)
    x_vals = np.linspace(x_min, x_max, 1000)
    y_vals = f(x_vals)
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {f_name}')
    plt.axhline(0, color='black',linewidth=1)

    # Plot the roots
    for root in roots:
        plt.plot(root, 0, 'ro')  # Red dots for roots
        plt.text(root, 0.5, f'{root:.3f}', ha='center')

    plt.title(f'Roots of {f_name} using Regula Falsi Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main(f1, f1_text)