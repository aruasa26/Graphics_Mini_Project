import cairo
import math

def create_surface(width, height, start_color, end_color):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    context = cairo.Context(surface)

    # Create vertical gradient for background
    gradient = cairo.LinearGradient(0, 0, 0, height)
    gradient.add_color_stop_rgb(0, *start_color)  # Start color (top)
    gradient.add_color_stop_rgb(1, *end_color)  # End color (bottom)
    context.set_source(gradient)
    context.paint()

    return surface, context


# Draw arch with optional border
def draw_arch(context, x, y, width, height, fill_color, border_color=None, border_width=5):
    if border_color:
        context.set_source_rgb(*border_color)
        context.set_line_width(border_width)
        context.move_to(x, y + height)
        context.arc(x + width // 2, y + height, width // 2, math.pi, 0)
        context.line_to(x + width, y + height * 2)
        context.line_to(x, y + height * 2)
        context.close_path()
        context.stroke()

    context.set_source_rgb(*fill_color)
    context.move_to(x, y + height)
    context.arc(x + width // 2, y + height, width // 2, math.pi, 0)
    context.line_to(x + width, y + height * 2)
    context.line_to(x, y + height * 2)
    context.close_path()
    context.fill()


# Draw stairs with gradient effect
def draw_stairs(context, start_x, start_y, stair_width, stair_height, num_stairs):
    for i in range(num_stairs):
        # Gradually shift from white to light grey on each step
        gradient = cairo.LinearGradient(0, start_y + (i * stair_height), 0, start_y + (i * stair_height) + stair_height)
        gradient.add_color_stop_rgb(0, 1, 1, 1)  # White at the top
        gradient.add_color_stop_rgb(1, 0.85, 0.85, 0.85)  # Light grey at the bottom

        context.set_source(gradient)
        context.rectangle(start_x, start_y + (i * stair_height), stair_width * (i + 1), stair_height)
        context.fill()


# Draw a smiley face with enhanced eyes and smile
def draw_smiley(context, center_x, center_y, radius):
    # Draw the yellow face (head of the smiley)
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(
        center_x,
        center_y - radius * 0.5,
        radius * 0.4,
        center_x,
        center_y,
        radius
    )
    gradient.add_color_stop_rgb(0, 1, 1, 0)  # Yellow
    gradient.add_color_stop_rgb(1, 0.9, 0.7, 0)  # Darker yellow for shading
    context.set_source(gradient)
    context.fill()

    # Draw the eyes with oval scaling and radial gradient
    def draw_eye(context, eye_x, eye_y, eye_radius):
        context.save()
        context.translate(eye_x, eye_y)
        context.scale(1, 1.5)
        context.arc(0, 0, eye_radius, 0, 2 * math.pi)
        eye_gradient = cairo.RadialGradient(0, 0, eye_radius * 0.1, 0, 0, eye_radius)
        eye_gradient.add_color_stop_rgb(0, 0.61, 0.35, 0.03)
        eye_gradient.add_color_stop_rgb(0.7, 0.41, 0.3, 0.03)
        eye_gradient.add_color_stop_rgb(1, 0.31, 0.25, 0.03)
        context.set_source(eye_gradient)
        context.fill()
        context.restore()  # Restore the context state

    # Left eye
    draw_eye(context, center_x - radius * 0.4, center_y - radius * 0.3, radius * 0.1)
    # Right eye
    draw_eye(context, center_x + radius * 0.4, center_y - radius * 0.3, radius * 0.1)

    # Draw the smile with rounded line caps
    context.set_line_cap(cairo.LINE_CAP_ROUND)  # Set line cap to round
    context.arc(center_x, center_y + radius * 0.1, radius * 0.5, math.radians(30), math.radians(150))
    context.set_source_rgb(0.41, 0.3, 0.03)  # Brown color for smile
    context.set_line_width(8)
    context.stroke()


# Draw a sun in the top left corner of the blue arch
def draw_sun(context, center_x, center_y, radius):
    # Draw the sun's body
    context.set_source_rgb(1, 1, 0)  # Yellow color
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.fill()

    # Draw sun rays
    ray_length = radius * 1.5
    num_rays = 12
    for i in range(num_rays):
        angle = i * (2 * math.pi / num_rays)
        start_x = center_x + radius * math.cos(angle)
        start_y = center_y + radius * math.sin(angle)
        end_x = center_x + ray_length * math.cos(angle)
        end_y = center_y + ray_length * math.sin(angle)

        context.set_line_width(4)
        context.set_source_rgb(1, 1, 0)  # Yellow color for rays
        context.move_to(start_x, start_y)
        context.line_to(end_x, end_y)
        context.stroke()


# Main drawing function
def draw_scene(context, surface):
    # Draw outer orange arch (larger arch with border)
    draw_arch(context, 50, 250, 500, 500, (1, 0.4, 0.1), border_color=(1, 0.2, 0), border_width=8)

    # Draw inner blue arch (smaller arch inside the orange one, with a border)
    draw_arch(context, 100, 350, 400, 400, (0.3, 0.6, 1), border_color=(0.1, 0.3, 0.8), border_width=5)

    # Draw the sun in the top left corner of the blue arch
    draw_sun(context, 400, 700, 30)

    # Draw stairs leading up, with subtle color gradient
    draw_stairs(context, 100, 1000, 100, 35, 4)

    # Draw the smiley face on top of the stairs (replacing the sphere)
    draw_smiley(context, 180, 950, 50)

    # Save the result to a file
    surface.write_to_png("scene/scene.png")
