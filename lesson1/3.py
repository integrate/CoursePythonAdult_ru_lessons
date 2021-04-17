import wrap
import wrap_py
from time import sleep

wrap_py.world.create_world(400, 600, 930, 50)
wrap_py.sprite.add_sprite("mario-2big", 100, 300, True, "stand")
wrap_py.sprite.change_width_proportionally(0, 50)

wrap_py.sprite.add_sprite("mario-2big", 300, 300, True, "stand")
wrap_py.sprite.set_sprite_flipx_reverse(1, True)
wrap_py.sprite.change_width_proportionally(1, 50)

sleep(1)

wrap_py.sprite_actions.move_sprite_to_angle(0, 500, 100)
sleep(1)
wrap_py.sprite_actions.move_sprite_to_angle(1, 500, 200)
sleep(1)
wrap_py.sprite.hide_sprite(0)
sleep(1)
wrap_py.sprite.show_sprite(0)