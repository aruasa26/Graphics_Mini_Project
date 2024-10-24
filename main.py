import smiley

WIDTH, HEIGHT = 600, 600
BG_COLOR = (0.9, 0.9, 0.9)

if __name__ == '__main__':
    surface, context = smiley.create_surface(WIDTH, HEIGHT, BG_COLOR)
    smiley.draw_smiley(surface, context, 300, 300, 200)
