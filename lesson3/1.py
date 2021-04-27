import time

import wrap, random

wrap.world.create_world(400, 600, 900, 60)
wrap.world.set_back_color(100, 50, 230)

pacman = wrap.sprite.add("pacman", 300, 300, "player1")

x1 = random.randint(50, 350)
y1 = random.randint(50, 550)
point1 = wrap.sprite.add("pacman", x1, y1, "dot")


angle = wrap.sprite.calc_angle_by_point(pacman, x1, y1)
wrap.actions.set_angle(pacman, angle, 1000)
wrap.actions.move_to(pacman, x1, y1, 1000)
wrap.sprite.remove(point1)

enemy_pos_left = wrap.sprite.get_right(pacman)
enemy_pos_bottom = wrap.sprite.get_top(pacman)
enemy = wrap.sprite.add("pacman", 0, 0, "enemy_yellow_down1")
wrap.sprite.move_left_to(enemy, enemy_pos_left)
wrap.sprite.move_bottom_to(enemy, enemy_pos_bottom)

enemy_top = wrap.sprite.get_top(enemy)
enemy_x = wrap.sprite.get_x(enemy)
wrap.sprite.add_text("Ага! Попался!", enemy_x, enemy_top-20, True, "arial", 15)

enemy_y = wrap.sprite.get_y(enemy)
angle = wrap.sprite.calc_angle_by_point(pacman, enemy_x, enemy_y)
angle += 180
wrap.sprite.set_angle(pacman, angle)
wrap.actions.move_at_angle_dir(pacman, 100, 1000)
