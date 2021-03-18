import numpy as np
from map import Line, Map

map = Map()

collision = map.check_collision(15, 15)

print(collision)
