def width_from_height(h, ratio_w, ratio_h):
    return h / (ratio_h / ratio_w)


def height_from_width(w, ratio_w, ratio_h):
    return w * (ratio_h / ratio_w)
