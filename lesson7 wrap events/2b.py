"""
На пробел марио принимает летящее положение.
На клавишу Вниз становится обратно.
В летящем положении не реагирует на клавиши вперед-назад
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