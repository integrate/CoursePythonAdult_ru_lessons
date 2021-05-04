"""
Персонаж двигается в направлении взгляда. Реагирует на два варианта управления.
"""

import wrap
from wrap import world, sprite

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

pacman = sprite.add("pacman", 30, 100, "player2")

#аналог on_key_up
@wrap.on_key_down(wrap.K_RIGHT, wrap.K_LEFT)
def rotate(key):
    angle = sprite.get_angle(pacman)
    if key == wrap.K_RIGHT:
        sprite.set_angle(pacman, angle + 45)
    else:
        sprite.set_angle(pacman, angle - 45)

@wrap.on_key_always(wrap.K_UP, wrap.K_w, delay=10)
def go():
    sprite.move_at_angle_dir(pacman, 3)