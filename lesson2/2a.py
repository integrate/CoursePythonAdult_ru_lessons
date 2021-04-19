import wrap

width = 400
height = 600

y = 500
x1 = 100
x2 = 250

wrap.world.create_world(width, height, 900, 60)

#создаем марио. Его нужно создавать первым, чтобы его уникальный номер был равен 0!
mario_start_x = 24
mario_start_y = y-8-32
wrap.sprite.add("mario", mario_start_x, mario_start_y, "stand")

#создаем платформы
last_x = width-24
wrap.sprite.add("mario-items", 24, y, "moving_platform1")
wrap.sprite.add("mario-items", last_x, y, "moving_platform1")

#создаем островки
wrap.sprite.add("mario-items", x1, y, "moving_platform1")
wrap.sprite.add("mario-items", x2, y, "moving_platform1")

#первый прыжок
half_way = (x1-24)/2
wrap.action.move_to_pos(0, 24+half_way, mario_start_y-half_way)
wrap.action.move_to_pos(0, x1, mario_start_y)

#второй прыжок
half_way = (x2-x1)/2
wrap.action.move_to_pos(0, x1+half_way, mario_start_y-half_way)
wrap.action.move_to_pos(0, x2, mario_start_y)

#третий прыжок
half_way = (last_x-x2)/2
wrap.action.move_to_pos(0, x2+half_way, mario_start_y-half_way)
wrap.action.move_to_pos(0, last_x, mario_start_y)