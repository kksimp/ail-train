def mat(frame_w, frame_h, art_w, art_h, weight):
    if art_w > frame_w or art_h > frame_h:
        return None, "artwork larger than the frame"
    spare_w = frame_w - art_w
    spare_h = frame_h - art_h - weight
    if spare_h < 0:
        return None, "no room for a weighted bottom"
    if spare_w < 40 or spare_h < 40:
        return None, "borders under 20 mm"
    return (spare_w // 2, spare_h // 2, spare_h // 2 + weight), None

jobs = [("print A4", 400, 500, 210, 297, 15), ("postcard", 254, 203, 148, 105, 10), ("poster", 500, 700, 500, 700, 0), ("square", 300, 300, 200, 200, 20), ("panorama", 600, 300, 500, 180, 25), ("tight", 300, 400, 250, 350, 30)]
for name, fw, fh, aw, ah, w in jobs:
    m, err = mat(fw, fh, aw, ah, w)
    if m is not None:
        print(f"{name:<9} sides {m[0]} mm, top {m[1]} mm, bottom {m[2]} mm")
    else:
        print(f"{name:<9} cannot mat: {err}")
