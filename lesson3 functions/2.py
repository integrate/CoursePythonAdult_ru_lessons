"""
На экране прячется клад по случайным координатам.
На экране появляется марио.
На центре марио появляется точка и пишется надпись “до клада Xpx”. Марио поворачивается в направлении расположения клада.

Консоль спрашивает “куда идем?” Мы вводим координаты x, y.
Марио переходит на новое место.
Также как в начале, обозначается расстояние до клада и направление его поиска.

Игроку дается всего 3 попытки. После третьей попытки показывается клад.
"""

import random, math

from wrap import sprite, actions, world

world.create_world(400, 600, 900, 60)
world.set_back_color(100, 50, 230)

#создаем марио
mario = sprite.add("mario-1-big", 80, 50, "stand")

#создаем клад #нужно создавать после марио, чтобы он рисовался поверх марио
treasure_x = random.randint(100, 350)
treasure_y = random.randint(400, 550)
treasure = sprite.add("mario-items", treasure_x, treasure_y, "flower1", False)

#поворачиваем марио к кладу
sprite.set_angle_to_point(mario, treasure_x, treasure_y)

#показываем расстояние до клада
dist_x = treasure_x - sprite.get_x(mario)
dist_y = treasure_y - sprite.get_y(mario)
dist = math.sqrt( dist_x**2 + dist_y**2 )
dist = int(dist)
point = sprite.add("pacman", sprite.get_x(mario), sprite.get_y(mario))
text="до клада "+str(dist)+"px"
sprite.add_text(text, sprite.get_x(mario), sprite.get_y(mario)-10)

#ввод места назначения
x = input("Куда идти по X:")
y = input("Куда идти по Y:")
actions.move_to(mario, int(x), int(y))

#поворачиваем марио к кладу
sprite.set_angle_to_point(mario, treasure_x, treasure_y)

#показываем расстояние до клада
dist_x = treasure_x - sprite.get_x(mario)
dist_y = treasure_y - sprite.get_y(mario)
dist = math.sqrt( dist_x**2 + dist_y**2 )
dist = int(dist)
point = sprite.add("pacman", sprite.get_x(mario), sprite.get_y(mario))
text="до клада "+str(dist)+"px"
sprite.add_text(text, sprite.get_x(mario), sprite.get_y(mario)-10)

#ввод места назначения
x = input("Куда идти по X:")
y = input("Куда идти по Y:")
actions.move_to(mario, int(x), int(y))

#поворачиваем марио к кладу
sprite.set_angle_to_point(mario, treasure_x, treasure_y)

#показываем расстояние до клада
dist_x = treasure_x - sprite.get_x(mario)
dist_y = treasure_y - sprite.get_y(mario)
dist = math.sqrt( dist_x**2 + dist_y**2 )
dist = int(dist)
point = sprite.add("pacman", sprite.get_x(mario), sprite.get_y(mario))
text="до клада "+str(dist)+"px"
sprite.add_text(text, sprite.get_x(mario), sprite.get_y(mario)-10)

#ввод места назначения
x = input("Куда идти по X:")
y = input("Куда идти по Y:")
actions.move_to(mario, int(x), int(y))

#поворачиваем марио к кладу
sprite.set_angle_to_point(mario, treasure_x, treasure_y)

#показываем расстояние до клада
dist_x = treasure_x - sprite.get_x(mario)
dist_y = treasure_y - sprite.get_y(mario)
dist = math.sqrt( dist_x**2 + dist_y**2 )
dist = int(dist)
point = sprite.add("pacman", sprite.get_x(mario), sprite.get_y(mario))
text="до клада "+str(dist)+"px"
sprite.add_text(text, sprite.get_x(mario), sprite.get_y(mario)-10)

#показываем клад
sprite.show(treasure)