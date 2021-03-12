import numpy as np
import matplotlib.pyplot as plt

u_l = 1
u_r = 2

X = np.arange(-150, 500, 1e-2)
U_0 = (X < 0)*u_l + (X >= 0)*u_r

f, f_prime, f_prime_inverse = np.exp, np.exp, np.log


def solution(X, t):
    a = f_prime(u_l) * t
    b = f_prime(u_r) * t

    left = np.argmax(X > a)
    right = np.argmax(X >= b)

    U = np.zeros(X.shape)
    U[:left] = u_l
    U[left:right] = f_prime_inverse(X[left:right] / t)
    U[right:] = u_r

    return U


plt.plot(X, U_0, label='t=0')
for t in (10, 20, 30, 40, 50):
    plt.plot(X, solution(X, t), label=f't={t}')

plt.title('Analytic Riemann Problem solution')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.show()
