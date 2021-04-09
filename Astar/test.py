import numpy as np
from map import Map
from products import Products

map = Map()

collision = map.check_collision(15, 15)

prod = Products()
prod.seed(100)

new_list = prod.get_random_list()

print(new_list)
new_list1 = prod.get_random_list()
print(new_list1)
print(collision)
