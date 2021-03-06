"""
На изготовление одного инструмента уходит X1 кг железа.
На изготовление одного гвоздя уходит X2.
У нас есть X0 килограмм.

Сколько инструментов мы сможем изготовить.
Сколько гвоздей получится из остатков.
Сколько килограмм останется не использованными.
Программа должна вывести решение с объяснением.
"""

#исходные данные
all_iron = 1000 #x0
one_tool_need = 17 #x1
one_nail_need = 2 #x2

#расчет инструментов и остатка
tools = all_iron//one_tool_need
iron_after_tools = all_iron % one_tool_need

#расчет гвоздей и остатка
nails = iron_after_tools//one_nail_need
iron_after_nails = iron_after_tools % one_nail_need

print("У нас есть", all_iron, "кг железа.")
print("На один инструмент требуется", one_tool_need, "кг железа.")
print("Из железа можно сделать", tools, "инструментов. После чего останется", iron_after_tools,"кг железа.")
print("На один гвоздь требуется", one_nail_need, "кг железа")
print("Из остатков можно сделать", nails, "гвоздей. После чего останется", iron_after_nails,"кг железа.")
