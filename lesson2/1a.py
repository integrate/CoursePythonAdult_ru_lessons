import wrap, wrap_py, random

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

#создаем игрока
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

wrap.action.move_to_pos(0, x1, y1)

wrap.action.move_to_pos(0, x2, y2)

wrap.action.move_to_pos(0, x3, y3)

