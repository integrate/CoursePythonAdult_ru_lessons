"""
На стрелки вправо-влево марио ходит по низу экрана.
При смене направления меняет костюм на подходящий.
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
