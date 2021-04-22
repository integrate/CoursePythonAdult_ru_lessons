"""
Пакмэн:
  размер окна настраивается двумя переменными: width, height
  4 врага разных цветов всегда в углах экрана
  положение 3х съедобных точек на экране настраивается 6-ю переменными: x1, y1, x2, y, x3, y3
  над каждой точкой появляется надпись №1, №2, №3
  пакмэн двигается от точки 1 к точке 2 и потом к точке 3.

  Усложнение: Всегда только строго вертикально или строго горизонтально. Не под углом.
"""
import wrap

width = 400
height = 600
x1 = 100
y1 = 200
x2 = 300
y2 = 400
x3 = 200
y3 = 134

wrap.world.create_world(width, height, 900, 60)
wrap.world.set_back_color(100, 100, 100)

#создаем игрока. Его нужно создавать первым, чтобы его уникальный номер был равен 0!
wrap.sprite.add("pacman", width / 2, height / 2, "player1")

#создаем соперников в углах экрана
wrap.sprite.add("pacman", 16, 16, "enemy_yellow_down1")
wrap.sprite.add("pacman", 16, height - 16, "enemy_pink_down1")
wrap.sprite.add("pacman", width - 16, 16, "enemy_blue_down1")
wrap.sprite.add("pacman", width - 16, height - 16, "enemy_red_down1")

#создаем точки
wrap.sprite.add("pacman", x1, y1, "dot")
wrap.sprite.add_text("Point 1", x1, y1-15, True, "Arial", 10, True)

wrap.sprite.add("pacman", x2, y2, "dot")
wrap.sprite.add_text("Point 2", x2, y2-15, True, "Arial", 10, True)

wrap.sprite.add("pacman", x3, y3, "dot")
wrap.sprite.add_text("Point 3", x3, y3-15, True, "Arial", 10, True)

wrap.action.move_to_pos(0, x1, height/2)
wrap.action.move_to_pos(0, x1, y1)

wrap.action.move_to_pos(0, x2, y1)
wrap.action.move_to_pos(0, x2, y2)

wrap.action.move_to_pos(0, x3, y2)
wrap.action.move_to_pos(0, x3, y3)

