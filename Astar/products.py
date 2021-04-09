import random

class Products():
    def __init__(self):
        self.product_list = {
            "coliflower": (1.54, 5.4),
            "brocoli": (1.54, 5.4),
            "lettuce": (1.54, 6.48),
            "asparagus": (1.54, 6.48),
            "tomato": (1.54, 7.91),
            "cucumber": (1.54, 7.91),
            "red_pepper": (1.54, 8.85),
            "green_pepper": (1.54, 8.85),
            "chicken": (2.06, 10.73),
            "chicken_drums": (2.9, 11.38),
            "chicken_wings": (3.92, 11.94),
            "sausage": (5.08, 12.22),
            "bacon": (6.36, 12.59),
            "hamburger": (7.4, 12.85),
            "beef": (8.79, 12.98),
            "ribs": (9.82, 12.98),
            "tuna": (11.86, 12.239976),
            "salmon": (12.61, 11.32),
            "cod": (13.46, 10.64),
            "crab": (14.35, 9.63),
            "milk": (14.85, 8.17),
            "orange_juice": (14.85, 8.17),
            "eggs": (14.85, 8.17),
            "yogurt": (14.85, 8.17),
            "ice_cream": (14.85, 8.17),
            "coca_cola": (14.85, 5.03),
            "red_bull": (14.85, 14.86),
            "water_bottle": (14.85, 6.86),
            "cake": (13.53, 6.8),
            "bread": (12.65, 4.82),
            "cereals": (7.12, 4.79),
            "sugar": (7.71, 4.79),
            "salt": (8.39, 4.79),
            "ketchup": (8.92, 4.79),
            "cocoa": (10, 5.37),
            "tea": (10, 5.93),
            "tomato_soup": (8.63, 6.66),
            "pasta": (8.22, 6.66),
            "olive_oil": (7.66, 6.66),
            "chips": (6.99, 6.66),
            "banana": (3.42, 4.63),
            "pear": (2.39, 5.24),
            "orange": (4.37, 5.34),
            "apple": (4.44, 6.35),
            "lemon": (2.31, 6.36),
            "lime": (3.37, 6.97),
            "pineapple": (3.42, 4.63),
            "mango": (4.44, 6.35),
            "strawberry": (2.31, 6.36),
            "potato": (3.58, 7.44),
            "sweet_potato": (3.03, 7.45),
            "watermelon": (5.1, 8.44),
            "carrot": (2.85, 9.33),
            "onion": (3.58, 9.33)
            }
        
        self.all_prod_list = self.product_list.keys()
    def get_random_list(self):
        number_prod = random.randint(4,9) # number of products to be generated in the list
        return random.sample(self.all_prod_list, number_prod)
    def seed(self, seed):
        random.seed(seed)


