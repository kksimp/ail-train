for d in [50.0, 30.0, 20.0, 15.0, 10.0, 5.0]:
    if d == 10.0: print(f"object at {d:>4.1f} cm: no image, rays leave parallel")
    else:
        di = 1.0 / (1.0 / 10.0 - 1.0 / d); m = 0.0 - di / d
        print(f"object at {d:>4.1f} cm: image at {di:>6.1f} cm, x{abs(m):.2f} ({'real, upside down' if di > 0.0 else 'virtual, upright'})")
