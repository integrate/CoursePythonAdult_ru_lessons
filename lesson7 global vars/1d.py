"""
Делаем, чтоб марио мог собирать монетки.
Делаем счетчик монеток.
"""

import wrap, random, time
from wrap import world, actions, sprite, sprite_text


def go_random():
    global coins
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

        if sprite.is_collide_sprite(mario, coin):
            add_coin()
            coins+=1
            sprite_text.set_text(coins_text, "Coins:"+str(coins))
            break

        count += 1

    sprite.remove(marker)


def add_coin():
    global coin
    rand_x = random.randint(150, 350)

    sprite.remove(coin)
    coin = sprite.add("mario-items", rand_x, 200, "coin")


world.create_world(500, 250, 300, 500)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 200, "stand")
coin = sprite.add("mario-items", 30, 200, "coin", False)

coins = 0
coins_text = sprite.add_text("Coins:"+str(coins), 100, 30)

add_coin()
while True:
    go_random()
