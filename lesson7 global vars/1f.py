"""
При сборе звезды марио растет на 3 пиксела. Скорость тоже растет на 2 пиксела.
Сбор звезды не должен считаться монеткой.
"""

import wrap, random, time
from wrap import world, actions, sprite, sprite_text


def go_random():
    global coins, speed
    rand_x = random.randint(30, 470)
    marker = sprite.add("pacman", rand_x, 200, "dot")

    way = rand_x - sprite.get_x(mario)

    speedx = speed
    if way < 0:
        speedx = -speedx

    steps_count = way / speedx

    count = 0
    while count < steps_count:
        sprite.move(mario, speedx, 0)

        if sprite.is_collide_sprite(mario, coin):

            if sprite.get_costume(coin)=="coin":
                coins+=1
                sprite_text.set_text(coins_text, "Coins:"+str(coins))
            else:
                sprite.set_height_proportionally(mario, sprite.get_height(mario) + 2)
                speed +=2

            add_coin()
            break

        count += 1

    sprite.remove(marker)


def add_coin():
    global coin, coins
    rand_x = random.randint(150, 350)

    sprite.remove(coin)

    if coins<3:
        coin = sprite.add("mario-items", rand_x, 200, "coin")
    else:
        coin = sprite.add("battle_city_items", rand_x, 200, "block_gift_star")
        coins -=3
        sprite_text.set_text(coins_text, "Coins:" + str(coins))


world.create_world(500, 250, 300, 500)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 200, "stand")
coin = sprite.add("mario-items", 30, 200, "coin", False)

coins = 0
coins_text = sprite.add_text("Coins:"+str(coins), 100, 30)
speed = 3

add_coin()
while True:
    go_random()
