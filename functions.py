def width_from_height(h: float, ratio_w: float, ratio_h: float) -> float:
    """
    Calculates the width when given height and
    an aspect ratio
    :param h: the given height
    :param ratio_w: the aspect ratio width
    :param ratio_h: the aspect ratio height
    :return: the calculated width
    """
    return h / (ratio_h / ratio_w)


def height_from_width(w: float, ratio_w: float, ratio_h: float) -> float:
    """
    Calculates the height when given width and
    an aspect ratio
    :param w: the given width
    :param ratio_w: the aspect ratio width
    :param ratio_h: the aspect ratio height
    :return: the calculated height
    """
    return w * (ratio_h / ratio_w)
