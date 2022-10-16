src = not False and True or False and not True

src1 = True and True or False and False
src1 = True or False
src1 = True # TODO расписать упрощение выражения

result = src1  # TODO подставить результат выражения

print(src == result)
