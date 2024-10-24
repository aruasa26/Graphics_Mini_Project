""" This script contains the baseline code, modularized into functions """

import cairo
import math
import canvas

# Default measurements:
WIDTH, HEIGHT = 600, 600
BG_COLOR = (0.2, 0.2, 0.2)

def create_surface():
    return canvas.create_surface(WIDTH, HEIGHT, BG_COLOR)

# Baseline default: center_x = WIDTH // 2, center_y = HEIGHT // 2, radius = 200
def draw_sphere(context, center_x=WIDTH//2, center_y=HEIGHT//2, radius=200):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(
        center_x - radius * 0.5,
        center_y - radius * 0.5,
        radius * 0.2,
        center_x,
        center_y,
        radius
    )

    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(0.7, 0.5, 0.5, 0.5)
    gradient.add_color_stop_rgb(1, 0.1, 0.1, 0.1)
    context.set_source(gradient)
    context.fill()