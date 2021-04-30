"""
Создаем привидение из Пакмэна. По случайным координатам.
Случайно выбирается положение точки. На выбранных координатах рисуется точка (dot) Пакмэна.
Приведение перемещается только по прямым линиям влево-вправо и вверх-вниз.
За два шага приведение перемещается к точке назначения.
Использовать if для определения подходящего костюма для приведения.
"""
import random
from wrap import world, sprite, actions

world.create_world(400, 600, 900, 60)

enemy = sprite.add("pacman", random.randint(30, 370), random.randint(30, 570), "enemy_blue_down1")

x = random.randint(0, 400)
y = random.randint(0, 600)
sprite.add("pacman", x, y, "dot")

if x>sprite.get_x(enemy):
    sprite.set_costume(enemy, "enemy_blue_right1")
else:
    sprite.set_costume(enemy, "enemy_blue_left1")
actions.move_to(enemy, x, sprite.get_y(enemy))

if y>sprite.get_y(enemy):
    sprite.set_costume(enemy, "enemy_blue_down1")
else:
    sprite.set_costume(enemy, "enemy_blue_up1")
actions.move_to(enemy, sprite.get_x(enemy), y)