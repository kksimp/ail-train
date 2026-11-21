h = 10.0; l = 5.0; dt = 0.01; ph = (0.0, 0.0); pl = (0.0, 0.0)
for step in range(2001):
    t = step * dt
    if step % 200 == 0: print(f"t {t:>4.1f}: hares {h:>5.1f}, lynxes {l:>5.1f}")
    if h > ph[1]: ph = (t, h)
    if l > pl[1]: pl = (t, l)
    dh = (1.1 * h - 0.4 * h * l) * dt; dl = (0.1 * h * l - 0.4 * l) * dt; h += dh; l += dl
print(f"hares peak {ph[1]:.1f} at t {ph[0]:.2f}, lynxes peak {pl[1]:.1f} at t {pl[0]:.2f}")
