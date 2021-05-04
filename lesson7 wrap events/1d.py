"""
Приведение появляется при нажатии на мышь. Исчезает при отпускании. Двигается за мышью.
"""

import wrap
from wrap import world, sprite

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

pacman = sprite.add("pacman", 30, 100, "player2")
enemy = sprite.add("pacman", 30, 100, "enemy_ill_blue1", False)


# аналог on_key_up
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


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def show_enemy(pos_x, pos_y):
    sprite.show(enemy)


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def hide_enemy():
    sprite.hide(enemy)

@wrap.on_mouse_move
def follow_me(pos_x, pos_y):
    wrap.sprite.move_to(enemy, pos_x, pos_y)

