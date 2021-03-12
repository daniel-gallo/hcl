def lax_wendroff2(T, X, B, dt, dx, f, f_prime):
    B[0, :] = B[0, 0]
    B[-1, :] = B[-1, 0]
    for t in range(1, len(T)):
        coefficients = f_prime(.5 * B[1:, t - 1] + .5 * B[:-1, t - 1])
        B[1:-1, t] = B[1:-1, t - 1] -\
                     .5 * dt / dx * (f(B[2:, t - 1]) - f(B[:-2, t - 1])) -\
                     .5 * (dt / dx) ** 2 * (coefficients[1:] * (f(B[2:, t - 1]) - f(B[1:-1, t - 1])) -
                                            coefficients[:-1] * (f(B[1:-1, t - 1]) - f(B[:-2, t - 1])))
