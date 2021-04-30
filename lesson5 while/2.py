"""
Марио и черепашка.

Черепашка двигается вверх-вниз вдоль левой границы экрана.
Марио двигается вверх-вниз вдоль правой границы экрана.
Они двигаются с разными скоростями.

В игре есть таймер, который показывает количество секунд, прошедшее с момента запуска игры.

При запуске игры, черепашка запускает молоточек в направлении Марио.
Молоточек летит и вращается.

Каждые 5 секунд черепашка запускает новый молоточек в том направлении, где в этот момент находится Марио.

Как только молоточек касается Марио, движение Черепашки и молоточка прекращается.
Марио падает вниз вращаясь.
"""

import time
from wrap import world, sprite, sprite_text

#создаем мир
world.create_world(400, 600, 900, 40)
world.set_back_color(100, 200, 200)

#создаем черпашку
turtle = sprite.add("mario-enemies", 30, 300, "turtle_stand")
sprite.set_reverse_x(turtle, True)

#создаем марио
mario = sprite.add("mario-1-big", 370, 300, "stand")
sprite.set_reverse_x(mario, True)

#создаем молоточек. устанавливаем точку, к которой он будет лететь
hammer = sprite.add("mario-enemies", 30, 300, "turtle_hammer")
hammer_goal_x = 370
hammer_goal_y = 300

#запоминаем время начала игры. и время запуска первого молоточка
timer = sprite.add_text("--", 70, 30)
start_time = time.time()
hammer_time = time.time()

#начальные скорости движения марио и черепашки
turtle_speed_y = 5
mario_speed_y = 3

#движение продолжается, пока молоточек не коснется марио
while not sprite.is_collide_sprite(hammer, mario):

    # движение и отбивка черепашки от верха и низа экрана
    sprite.move(turtle, 0, turtle_speed_y)
    if sprite.get_bottom(turtle)>600:
        turtle_speed_y = -5
    if sprite.get_top(turtle)<0:
        turtle_speed_y = 5

    # движение и отбивка марио от верха и низа экрана
    sprite.move(mario, 0, mario_speed_y)
    if sprite.get_bottom(mario)>600:
        mario_speed_y=-3
    if sprite.get_top(mario)<0:
        mario_speed_y=3

    # движение и поворот молоточка
    sprite.move_at_angle_point(hammer, hammer_goal_x, hammer_goal_y, 30)
    angle = sprite.get_angle(hammer)
    sprite.set_angle(hammer, angle+10)

    # обновление таймера
    end_time = time.time()
    sprite_text.set_text(timer, str(int(end_time-start_time)))

    # запускаем новый молоточек, если с момента запуска прошлого прошло 5 секунд
    if end_time-hammer_time>=5:
        hammer_time=end_time
        hammer = sprite.add("mario-enemies", sprite.get_x(turtle), sprite.get_y(turtle), "turtle_hammer")
        hammer_goal_x = sprite.get_x(mario)
        hammer_goal_y = sprite.get_y(mario)


# падение и вращение марио
while True:
    sprite.move(mario, 0, 8)

    angle = sprite.get_angle(mario)
    sprite.set_angle(mario, angle+8)