from scene import scene

WIDTH, HEIGHT = 600, 1200  # Canvas dimensions
BG_GRADIENT_START = (0.7, 0.7, 0.7)  # Light grey at the top
BG_GRADIENT_END = (0.5, 0.5, 0.5)  # Darker grey at the bottom

if __name__ == '__main__':
    surface, context = scene.create_surface(WIDTH, HEIGHT, BG_GRADIENT_START, BG_GRADIENT_END)
    scene.draw_scene(context, surface)
