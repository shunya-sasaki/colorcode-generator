"""In this module, we define utility functions for the colgen package.
"""


def generate_hex_codes_from_rgb(dict_rgb):
    """Generate hex codes from RGB values

    Args:
        dict_rgb (dict[str, tuple[int, int, int]]):
            Dictionary with color names as keys and RGB values as values.
    Returns:
        dict[str, str]:
            Dictionary with color names and hex codes.
    """
    new_dict = {}
    for key, value in dict_rgb.items():
        r, g, b = value
        dr_dark = r / 500
        dg_dark = g / 500
        db_dark = b / 500
        dr_light = (255 - r) / 500
        dg_light = (255 - g) / 500
        db_light = (255 - b) / 500
        for i_color in range(50, 1000, 50):
            if i_color < 500:
                new_r = int(dr_dark * i_color)
                new_g = int(dg_dark * i_color)
                new_b = int(db_dark * i_color)
            elif i_color == 500:
                new_r = r
                new_g = g
                new_b = b
            else:
                new_r = int(r + dr_light * (i_color - 500))
                new_g = int(g + dg_light * (i_color - 500))
                new_b = int(b + db_light * (i_color - 500))
            hex_code = f"#{new_r:02x}{new_g:02x}{new_b:02x}"
            new_dict[f"{key}-{i_color}"] = hex_code
        return new_dict
