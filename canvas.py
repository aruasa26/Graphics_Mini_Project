""" This module contains the function for setting up the surface """

import cairo

# Set up the surface
def create_surface(width, height, bg_color):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*bg_color)
    context.paint()
    return surface, context