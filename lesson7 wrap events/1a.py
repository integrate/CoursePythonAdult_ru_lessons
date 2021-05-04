"""
Персонаж реагирует на нажатие любой клавиши.
"""

import wrap
from wrap import world, sprite

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

pacman = sprite.add("pacman", 30, 100, "player2")

@wrap.on_key_down
def go_right():
    sprite.move(pacman, 3, 0)
