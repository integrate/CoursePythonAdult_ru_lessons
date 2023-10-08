"""
Расположить четко в углах экрана случайных персонажей.
Расположить одного персонажа в центре.
Между каждым угловым персонажем центральным должны быть еще два персонажа, чтобы они образовывали крест.
"""

import wrap

width = 300
height = 600



wrap.world.create_world(width, height)
wrap.sprite.add("pacman",0, 0, "enemy_blue_down1")
wrap.sprite.add("pacman",width, 0, "enemy_ill_blue1")
wrap.sprite.add("pacman",width, height, "enemy_ill_white1")
wrap.sprite.add("pacman",0, height, "enemy_pink_down1")

wrap.sprite.add("pacman",0, height/6, "enemy_red_down1")
wrap.sprite.add("pacman",0, 2*height/6, "enemy_red_down1")
wrap.sprite.add("pacman",0, 3*height/6, "enemy_red_down1")
wrap.sprite.add("pacman",0, 4*height/6, "enemy_red_down1")
wrap.sprite.add("pacman",0, 5*height/6, "enemy_red_down1")

wrap.sprite.add("pacman",width, height/6, "enemy_red_down1")
wrap.sprite.add("pacman",width, 2*height/6, "enemy_red_down1")
wrap.sprite.add("pacman",width, 3*height/6, "enemy_red_down1")
wrap.sprite.add("pacman",width, 4*height/6, "enemy_red_down1")
wrap.sprite.add("pacman",width, 5*height/6, "enemy_red_down1")

wrap.sprite.add("pacman",width/6, 0, "enemy_red_down1")
wrap.sprite.add("pacman",2*width/6, 0, "enemy_red_down1")
wrap.sprite.add("pacman",3*width/6, 0, "enemy_red_down1")
wrap.sprite.add("pacman",4*width/6, 0, "enemy_red_down1")
wrap.sprite.add("pacman",5*width/6, 0, "enemy_red_down1")

wrap.sprite.add("pacman",width/6, height, "enemy_red_down1")
wrap.sprite.add("pacman",2*width/6, height, "enemy_red_down1")
wrap.sprite.add("pacman",3*width/6, height, "enemy_red_down1")
wrap.sprite.add("pacman",4*width/6, height, "enemy_red_down1")
wrap.sprite.add("pacman",5*width/6, height, "enemy_red_down1")

wrap.sprite.add("pacman",width/6, height/6, "enemy_red_down1")
wrap.sprite.add("pacman",2*width/6, 2*height/6, "enemy_white_down1")
wrap.sprite.add("pacman",width/2, height/2, "enemy_yellow_down1")
wrap.sprite.add("pacman",4*width/6, 4*height/6, "enemy_blue_left1")
wrap.sprite.add("pacman",5*width/6, 5*height/6, "enemy_pink_left1")

wrap.sprite.add("pacman",4*width/6, 2*height/6, "enemy_red_left1")
wrap.sprite.add("pacman",5*width/6, height/6, "enemy_blue_right1")

wrap.sprite.add("pacman",width/6, 5*height/6, "enemy_yellow_left1")
wrap.sprite.add("pacman",2*width/6, 4*height/6, "enemy_blue_up1")

