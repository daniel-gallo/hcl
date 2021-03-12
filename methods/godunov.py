import numpy as np


def godunov(T, X, B, dt, dx, f, f_prime):
    B[0, :] = B[0, 0]
    B[-1, :] = B[-1, 0]
    for t in range(1, len(T)):
        f_primes = f_prime(B[:, t - 1])
        fs = np.zeros(len(X) - 1)

        for x in range(len(X) - 1):
            if f_primes[x] > 0 and f_primes[x + 1] > 0:
                # Solution moving to the right
                fs[x] = f(B[x, t - 1])
                pass
            elif f_primes[x] < 0 and f_primes[x + 1] < 0:
                # Solution moving to the left
                fs[x] = f(B[x + 1, t - 1])
            elif f_primes[x] > 0 and f_primes[x + 1] < 0:
                # Shock save with velocity x_s
                x_s = t * (f(B[x, t - 1]) - f(B[x + 1, t - 1])) / (B[x, t - 1] - B[x + 1, t - 1])

                if x_s > 0:
                    # The solution moves to the right
                    fs[x] = f(B[x, t - 1])
                elif x_s < 0:
                    # The solution moves to the left
                    fs[x] = f(B[x + 1, t - 1])
                else:
                    raise Exception('x_s is zero!')

            elif f_primes[x] < 0 and f_primes[x + 1] > 0:
                # Stationary characteristic
                # We have to find u_i < u < u_{i+1} s.t f'(u*) => BOLZANO
                left = B[x, t - 1]
                right = B[x + 1, t - 1]
                midpoint = (left + right) / 2

                fs[x] = f(midpoint)
            else:
                raise Exception(f_primes[x], f_primes[x + 1])

        B[1:-1, t] = B[1:-1, t - 1] + dt / dx * (fs[:-1] - fs[1:])
