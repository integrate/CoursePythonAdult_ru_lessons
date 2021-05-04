"""
В летящем положении поворачивается и летит в направлении указателя мыши.
"""

import wrap
from wrap import world, sprite

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 550, "stand")


@wrap.on_key_always(wrap.K_RIGHT, delay=30)
def go_right():
    if sprite.get_costume(mario) == "stand":
        sprite.set_costume(mario, "stand")
        sprite.set_reverse_x(mario, False)
        sprite.move(mario, 2, 0)


@wrap.on_key_always(wrap.K_LEFT, delay=30)
def go_left_right():
    if sprite.get_costume(mario) == "stand":
        sprite.set_costume(mario, "stand")
        sprite.set_reverse_x(mario, True)
        sprite.move(mario, -2, 0)


@wrap.on_key_down(wrap.K_SPACE, wrap.K_DOWN)
def fly(key):
    sprite.set_reverse_x(mario, False)
    if key==wrap.K_SPACE:
        sprite.set_costume(mario, "swim3")
        sprite.set_angle(mario, 160)
    else:
        sprite.set_costume(mario, "stand")
        sprite.set_angle(mario, 90)
        sprite.move_to(mario, sprite.get_x(mario), 550)


@wrap.always(delay=10)
def follow_me(pos_x, pos_y):
    if sprite.get_costume(mario)=="swim3" and (pos_x!=sprite.get_x(mario) or pos_y!=sprite.get_y(mario)):
        angle = sprite.calc_angle_by_point(mario, pos_x, pos_y)
        sprite.set_angle(mario, angle+70)
        sprite.move_at_angle_point(mario, pos_x, pos_y, 3)