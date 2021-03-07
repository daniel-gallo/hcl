def lax_wendroff(T, B, dt, dx, f):
    B[0, :] = B[0, 0]
    B[-1, :] = B[-1, 0]
    for t in range(1, len(T)):
        half_step = .5 * (B[1:, t - 1] + B[:-1, t - 1]) - \
                    .5 * dt / dx * (f(B[1:, t - 1]) - f(B[:-1, t - 1]))

        B[1:-1, t] = B[1:-1, t - 1] - dt / dx * (f(half_step[1:]) - f(half_step[:-1]))
