def lax_friedrichs(T, B, dt, dx, f):
    B[0, :] = B[0, 0]
    B[-1, :] = B[-1, 0]
    for t in range(1, len(T)):
        B[1:-1, t] = .5 * (B[2:, t - 1] + B[:-2, t - 1]) - \
                     .5 * dt / dx * (f(B[2:, t - 1]) - f(B[:-2, t - 1]))