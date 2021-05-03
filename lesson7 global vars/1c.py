"""
Делаем, чтоб Марио бесконечно ходил.
Делаем добавление монетки.
"""

import wrap, random, time
from wrap import world, actions, sprite, sprite_text


def go_random():
    rand_x = random.randint(30, 470)
    marker = sprite.add("pacman", rand_x, 200, "dot")

    way = rand_x - sprite.get_x(mario)

    speed = 3
    if way < 0:
        speed = -speed

    steps_count = way / speed

    count = 0
    while count < steps_count:
        sprite.move(mario, speed, 0)
        count += 1

    sprite.remove(marker)


def add_coin():
    global time_last_coin, coin
    now = time.time()
    if now - time_last_coin < 3:
        return
    time_last_coin = now

    rand_x = random.randint(150, 350)

    sprite.remove(coin)
    coin = sprite.add("mario-items", rand_x, 200, "coin")


world.create_world(500, 250, 300, 500)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 200, "stand")
coin = sprite.add("mario-items", -30, 200, "coin", False)

time_last_coin = time.time()

while True:
    go_random()
    add_coin()
