import time
from wrap import world, sprite

"""
Делаем трех марио, которые играют в футбол спящей уткой.
"""

world.create_world(400, 600, 900, 50)

#создаем игроков
player1 = sprite.add("mario-1-big", 50, 300, "stand")
player2 = sprite.add("mario-2-big", 350, 100, "stand")
player3 = sprite.add("mario-3-big", 150, 50, "stand")
sprite.set_reverse_x(player2, True)

#создаем мяч
ball = sprite.add("mario-enemies", 200, 220, "duck_red_dead")

#полет мяча
dx = sprite.get_left(player2) - sprite.get_right(ball)
dy = sprite.get_bottom(player2) - sprite.get_bottom(ball)

stepx = dx/30
stepy = dy/30

count = 0
while count<30:
    time.sleep(1/30)
    sprite.move(ball, stepx, stepy)
    count+=1

time.sleep(1)

#полет мяча
dx = sprite.get_right(player1) - sprite.get_left(ball)
dy = sprite.get_bottom(player1) - sprite.get_bottom(ball)

stepx = dx/30
stepy = dy/30
count = 0
while count<30:
    time.sleep(1/30)
    sprite.move(ball, stepx, stepy)
    count+=1


#полет мяча
dx = sprite.get_right(player3) - sprite.get_left(ball)
dy = sprite.get_bottom(player3) - sprite.get_bottom(ball)

stepx = dx/30
stepy = dy/30
count = 0
while count<30:
    time.sleep(1/30)
    sprite.move(ball, stepx, stepy)
    count+=1