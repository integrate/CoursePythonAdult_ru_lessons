"""
Вынесли в отдельную функцию команду say(). Она рисует слова персонажей.
"""

import time

from wrap import world, sprite, sprite_text, actions


def say(player_id, text):
    text = sprite.add_text(text, sprite.get_x(player_id), sprite.get_top(player_id) - 20, font_size=10, underline=True)
    actions.set_size_percent(text, 200, 200, 500)
    actions.set_size_percent(text, 100, 100, 500)
    sprite.remove(text)


def run(angle):
    # побег
    say(victim, "Бежим!")

    actions.set_size_percent(victim, 30, 30, 500)
    actions.set_angle(victim, angle, 500)
    actions.move_at_angle_dir(victim, 100, 600)
    actions.set_size_percent(victim, 100, 100, 500)


def run_after_him():

    # погоня
    say(hunter, "За ним!")
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), 70, 500)



world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")

run(180)
run_after_him()
run(200)
run_after_him()
run(90)
run_after_him()

