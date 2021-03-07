import numpy as np
import matplotlib.pyplot as plt

from methods.godunov import godunov
from methods.lax_friedrichs import lax_friedrichs
from methods.lax_wendroff import lax_wendroff

dt = 5e-2
dx = 1e-1
max_t = 30
max_x = 100
problem = 'ferry'
method = lax_wendroff

T = np.arange(0, max_t, dt)
X = np.arange(0, max_x, dx)
B = np.zeros((len(X), len(T)))


def f(v):
    return v - v ** 3 / 250 ** 2


def f_prime(v):
    return 1 - 3 * v ** 2 / 250 ** 2


if problem == 'ferry':
    B[:len(X) // 2, 0] = 250
elif problem == 'police':
    B[:, 0] = 25 * (0.45 * max(X) < X) * (X < .55 * max(X)) + 50
elif problem == 'police (congested)':
    B[:, 0] = 25 * (0.45 * max(X) < X) * (X < .55 * max(X)) + 175

method(T, B, dt, dx, f)

# Ensure CFL condition holds
assert (f_prime(B) * dt <= dx).all()

for t in (0, 50, 100, 150, 200, 250):
    plt.plot(X, B[:, t], label=f't = {t}')

plt.title(method.__name__)
plt.xlabel('Distance (km)')
plt.ylabel('Cars per km')
plt.legend()
plt.savefig('plot.png')
