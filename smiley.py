import cairo
import math
import canvas

def create_surface(width, height, bg_color):
    return canvas.create_surface(width, height, bg_color)

def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(
        center_x,
        center_y - 100,
        radius * 0.4,
        center_x,
        center_y,
        radius
    )

    gradient.add_color_stop_rgb(0, 1, 1, 0)
    gradient.add_color_stop_rgb(0.35, 0.9, 0.9, 0)
    gradient.add_color_stop_rgb(0.65, 0.8, 0.7, 0)
    gradient.add_color_stop_rgb(0.9, 0.8, 0.5, 0)
    gradient.add_color_stop_rgb(1, 0.7, 0.4, 0)
    context.set_source(gradient)
    context.fill()

def draw_eye(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    eye_gradient = cairo.RadialGradient(
        center_x,
        center_y,
        radius * 0.2,
        center_x,
        center_y,
        radius
    )

    eye_gradient.add_color_stop_rgb(0, 0.61, 0.35, 0.03)
    eye_gradient.add_color_stop_rgb(0.7, 0.41, 0.3, 0.03)
    eye_gradient.add_color_stop_rgb(1, 0.31, 0.25, 0.03)
    context.set_source(eye_gradient)
    context.fill()

def draw_smiley(surface, context, center_x, center_y, radius):
    # Baseline modified for the emoji
    draw_sphere(context, center_x, center_y, radius)

    # Eyes
    context.save()
    context.scale(1, 1.5)
    draw_eye(context, 230, 170, radius=20)
    draw_eye(context, 370, 170, radius=20)
    context.restore()

    # Smile
    context.arc(300, 320, 100, math.radians(30), math.radians(150))
    context.set_source_rgb(0.41, 0.3, 0.03)
    context.set_line_cap(cairo.LINE_CAP_ROUND)
    context.set_line_width(10)
    context.stroke()

    surface.write_to_png("smiley.png")
