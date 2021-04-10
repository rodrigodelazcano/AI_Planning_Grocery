import numpy as np
from map import Map
from products import Products

map = Map(radius=0.177)

collision = map.check_collision(15, 15)

prod = Products()
prod.seed(100)

new_list = prod.get_random_list()

print(new_list)
new_list1 = prod.get_random_list()
print(new_list1)
print(collision)

for product, coord in prod.product_list.items():

    collision = map.check_collision(coord[0],coord[1])
    if (collision == True):
        print(product, " collides")
