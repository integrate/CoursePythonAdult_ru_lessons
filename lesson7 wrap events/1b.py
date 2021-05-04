"""
Персонаж поворачивается на 45 гр на нажатие клавиши вправо.
"""

import wrap
from wrap import world, sprite

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

pacman = sprite.add("pacman", 30, 100, "player2")

#аналог on_key_up
@wrap.on_key_down(wrap.K_RIGHT)
def rotate():
    angle = sprite.get_angle(pacman)
    sprite.set_angle(pacman, angle+45)