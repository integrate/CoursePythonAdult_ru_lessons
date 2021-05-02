"""
Сделаем, чтобы Марио плавно перемещался на случайную координату. Не используем модуль actions.
"""

import wrap, random, time
from wrap import world, actions, sprite, sprite_text


def go_random():
    rand_x = random.randint(30, 470)
    marker = sprite.add("pacman", rand_x, 200, "dot")

    way = rand_x - sprite.get_x(mario)

    speed = 3
    if way<0:
        speed = -speed

    steps_count = way / speed

    count = 0
    while count < steps_count:
        sprite.move(mario, speed, 0)
        count += 1

    sprite.remove(marker)


world.create_world(500, 250, 300, 500)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 200, "stand")

go_random()
go_random()
go_random()
