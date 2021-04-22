import time

import wrap, wrap_py, random

wrap.world.create_world(400, 600, 900, 60)
wrap.world.set_back_color(100, 50, 230)

pacman = wrap.sprite.add("pacman", 300, 300, "player1")

x1 = random.randint(50, 350)
y1 = random.randint(50, 550)
point1 = wrap.sprite.add("pacman", x1, y1, "dot")


angle = wrap_py.sprite.calc_angle_by_point(pacman, [x1, y1])
wrap_py.sprite_actions.rotate_to_angle(pacman, 1000, angle)
wrap.action.move_to_pos(pacman, x1, y1, 1000)
wrap.sprite.remove(point1)

enemy_pos_left = wrap_py.sprite.get_right(pacman)
enemy_pos_bottom = wrap_py.sprite.get_top(pacman)
enemy = wrap.sprite.add("pacman", 0, 0, "enemy_yellow_down1")
wrap_py.sprite.set_left_to(enemy, enemy_pos_left)
wrap_py.sprite.set_bottom_to(enemy, enemy_pos_bottom)

enemy_top = wrap_py.sprite.get_top(enemy)
enemy_x = wrap_py.sprite.get_sprite_x(enemy)
wrap.sprite.add_text("Ага! Попался!", enemy_x, enemy_top-20, True, "arial", 15)

enemy_y = wrap_py.sprite.get_sprite_y(enemy)
angle = wrap_py.sprite.calc_angle_by_point(pacman, [enemy_x, enemy_y])
angle += 180
wrap_py.sprite.rotate_to_angle(pacman, angle)
wrap_py.sprite_actions.move_sprite_to_angle(pacman, 1000, 100)


