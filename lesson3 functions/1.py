"""
На фиксированных координатах создаем пакмэна. Даем ему случайный размер в процентах от 50 до 500%.
Создаем на рандомных координатах одну точку для пакмэна.
Пакмэн поворачивается к ней и идет по направлению к ней. Ест ее.
Справа сверху от точки появляется враг. Пакмэн поворачивается в обратную от него сторону и убегает.

Более сложный вариант:
Сделать, чтобы враг появлялся не справа сверху от Пакмэна, а сверху Пакмэна.
Положение по оси Х у врага должно быть случайным от 50 точек левее центра Пакмэна до 50 точек правее центра Пакмэна.
"""

import wrap, random

wrap.world.create_world(400, 600, 900, 60)
wrap.world.set_back_color(100, 50, 230)

pacman = wrap.sprite.add("pacman", 300, 300, "player1")
pacman_size=random.randint(50, 500)
wrap.sprite.set_size_percent(pacman, pacman_size, pacman_size)

x1 = random.randint(50, 300)
y1 = random.randint(150, 550)
point1 = wrap.sprite.add("pacman", x1, y1, "dot")

#вариант1:
# angle = wrap.sprite.calc_angle_by_point(pacman, x1, y1)
# wrap.actions.set_angle(pacman, angle, 1000)
#вариант2:
wrap.actions.set_angle_to_point(pacman, x1, y1)

#двигаем спрайт, удаляем точку
wrap.actions.move_to(pacman, x1, y1, 1000)
wrap.sprite.remove(point1)

#создаем врага в правильном месте

enemy = wrap.sprite.add("pacman", 0, 0, "enemy_yellow_down1")
enemy_pos_bottom = wrap.sprite.get_top(pacman)
wrap.sprite.move_bottom_to(enemy, enemy_pos_bottom)

# Вариант а:
enemy_pos_left = wrap.sprite.get_right(pacman)
wrap.sprite.move_left_to(enemy, enemy_pos_left)

# Вариант б:
enemy_pos_x = wrap.sprite.get_x(pacman)
diffx = random.randint(-50, 50)
wrap.sprite.move_to(enemy, wrap.sprite.get_x(pacman)+diffx, wrap.sprite.get_y(enemy))


#создаем надпись над врагом
enemy_top = wrap.sprite.get_top(enemy)
enemy_x = wrap.sprite.get_x(enemy)
wrap.sprite.add_text("Ага! Попался!", enemy_x, enemy_top-20, True, "arial", 15)

#рассчитываем угол разворота
enemy_y = wrap.sprite.get_y(enemy)
angle = wrap.sprite.calc_angle_by_point(pacman, enemy_x, enemy_y)
angle += 180
wrap.sprite.set_angle(pacman, angle)

#убегаем
wrap.actions.move_at_angle_dir(pacman, 100, 1000)
