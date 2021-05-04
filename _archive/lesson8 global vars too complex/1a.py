"""
Создаем горизонтальный мир и Марио.
"""

import wrap, random, time
from wrap import world, actions, sprite, sprite_text

world.create_world(500, 250, 300, 500)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 200, "stand")