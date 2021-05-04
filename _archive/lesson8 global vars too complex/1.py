"""
Делаем функцию перемещения Марио на случайную координату X.

"""

import wrap, random, time
from wrap import world, actions, sprite, sprite_text


def go_random():
    global coins, mario_speed

    rand_pos_x = random.randint(30, 470)

    marker = sprite.add("pacman", rand_pos_x, sprite.get_top(mario) - 10, "dot")

    way = rand_pos_x - sprite.get_x(mario)

    speed = mario_speed
    if way < 0:
        speed = -speed

    steps = way / speed


    steps_count = 0
    while steps_count < steps:
        sprite.move(mario, speed, 0)

        if sprite.is_collide_sprite(mario, coin):

            if sprite.get_costume(coin) == "coin":
                coins += 1
                update_texts()
            else:
                sprite.set_height_proportionally(mario, sprite.get_height(mario)+5)
                mario_speed+=2
                update_texts()
            make_coin()
            break

        steps_count += 1

    sprite.remove(marker)


def make_coin():
    global coin, coins

    rand_x = random.randint(150, 350)
    sprite.remove(coin)

    if coins>=3:
        coin = sprite.add("battle_city_items", rand_x, sprite.get_y(mario), "block_gift_star", True)
        coins -=3
        update_texts()
    else:
        coin = sprite.add("mario-items", rand_x, sprite.get_y(mario), "coin", True)

def update_texts():
    sprite_text.set_text(counter, "Coins:" + str(coins))
    sprite_text.set_text(speed_text, "Speed:" + str(mario_speed))



world.create_world(500, 250, 300, 500)
world.set_back_color(100, 200, 200)

mario = sprite.add("mario-1-big", 30, 200, "stand")
mario_speed = 6

coin = sprite.add("mario-items", 30, sprite.get_y(mario), "coin", True)

coins = 0
counter = sprite.add_text("Coins:" +str(coins), 50, 30)
speed_text = sprite.add_text("Speed:" +str(mario_speed), 250, 30)

make_coin()
while True:
    go_random()
