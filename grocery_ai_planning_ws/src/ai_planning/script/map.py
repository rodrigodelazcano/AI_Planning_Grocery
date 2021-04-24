import numpy as np
import math

class Line():
    def __init__(self, x1, x2, y1, y2, distance, side):
        self.coeff = np.polyfit([x1, x2],[y1, y2], 1)
        self.side = side ## side 0 left, side 1 right

        if distance > 0:
            if (self.coeff[0] > 0 and side == 0):
                self.coeff[1] = self.coeff[1] - distance * math.sin(1.57 - math.atan(self.coeff[0])) + self.coeff[0]*distance * math.cos(1.57 - math.atan(self.coeff[0]))
            elif (self.coeff[0] > 0 and side == 1):
                self.coeff[1] = self.coeff[1] - distance * math.sin(1.57 - math.atan(self.coeff[0]))
            elif (self.coeff[0] < 0 and side == 0):
                self.coeff[1] = self.coeff[1] + distance * (self.coeff[0]*math.cos(1.57 - math.atan(abs(self.coeff[0]))) + math.cos(1.57 - math.atan(abs(self.coeff[0]))))
            elif (self.coeff[0] < 0 and side == 1):
                self.coeff[1] = self.coeff[1] + distance * (self.coeff[0]*math.cos(1.57 - math.atan(abs(self.coeff[0]))) + math.cos(1.57 - math.atan(abs(self.coeff[0]))))

    def check_boundary(self, x, y):
        boundary = round(y - self.coeff[0] * x - self.coeff[1])
        if (self.coeff[0] > 0 and self.side == 0):
            if boundary >= 0:
                return True ##out of boundary
        if (self.coeff[0] > 0 and self.side == 1):
            if boundary <= 0:
                return True
        if (self.coeff[0] < 0 and self.side == 0):
            if boundary <= 0:
                return True
        if (self.coeff[0] < 0 and self.side == 1):
            if boundary >= 0:
                return True

        return False ##inside boundary
    
      
    
class Map():
    def __init__(self, clearance = 0.177, radius = 0.15):

        self.clearance = clearance
        self.radius = radius
        self.distance = clearance + radius
        self.goal = None

        self.line1 = Line(1.199979, 1.130248, 9.748759, 10.939484, self.distance, 0)
        self.line2 = Line(1.130248, 3.263999, 10.939484, 12.155476, self.distance, 0)
        self.line3 = Line(3.263999, 8.037341, 12.155476, 13.453712, self.distance, 0)
        self.line4 = Line(10.528966, 11.612505, 13.453485, 13.011247, self.distance, 1)
        self.line5 = Line(11.612505, 15.053117, 13.011247, 9.539164, self.distance, 1)
        self.line6 = Line(15.053117, 15.448179, 9.539164, 8.912024, self.distance, 1)

    def check_collision(self, x, y):
        def check_contour(x, y):
            c1 = x <= 0 + self.distance
            c2 = y >= 4.765123 - self.distance and x <= 1.199979 + self.distance and self.line1.check_boundary(x, y)
            c3 = x >= 15.448179 - self.distance
            c4 = y <= 0 + self.distance
            c5 = y >= 13.453485 - self.distance
            total_c = c1 or c2 or c3 or c4 or c5
            c_line2 = self.line2.check_boundary(x, y)
            c_line3 = self.line3.check_boundary(x, y)
            c_line4 = self.line4.check_boundary(x, y)
            c_line5 = self.line5.check_boundary(x, y)
            c_line6 = self.line6.check_boundary(x, y)

            if (total_c or c_line2 or c_line3 or c_line4 or c_line5 or c_line6):
                return True ##out of boundary
            
            return False ##inside boundary
        
        def check_cashiers(x ,y):
            cs_y = (y >= 2.246674 - self.distance) and (y <= 3.693339 + self.distance)
            cs1 = ((x >= 5.251926 - self.distance) and (x <= 6.035216 + self.distance) and cs_y)
            cs2 = ((x >= 7.172170 - self.distance) and (x <= 7.975383 + self.distance) and cs_y)
            cs3 = ((x >= 9.040226 - self.distance) and (x <= 9.832662 + self.distance) and cs_y)
            cs4 = ((x >= 10.931436 - self.distance) and (x <= 11.755313 + self.distance) and cs_y)
            cs5 = ((x >= 12.833400 - self.distance) and (x <= 13.646369 + self.distance) and cs_y)

            if (cs1 or cs2 or cs3 or cs4 or cs5):
                return True
            
            return False
        
        def check_shelves(x, y):
            s_x = (x >= 6.253904 - self.distance) and (x <= 9.605268 + self.distance)
            s_y = (y <= 8.432007 + self.distance) and (y >= 7.505381 - self.distance)
            s1 = (s_x and (y <= 10.764730 + self.distance) and (y >= 9.775013 - self.distance))
            s2 = (s_x and (y <= 6.209282 + self.distance) and (y >= 5.266344 - self.distance))
            s3 = (x >= 6.253904 - self.distance) and (x <= 7.227457 + self.distance) and s_y
            s4 = (x >= 8.622844 - self.distance) and (x <= 9.610721 + self.distance) and s_y
            s5 = ((x >= 10.978244 - self.distance) and (x <= 11.974152 + self.distance) and (y <= 9.687450 + self.distance)
                and (y >= 6.32 - self.distance))
            s6 = ((x >= 13.160530 - self.distance) and (x <= 13.939310 + self.distance) and (y <= 6.165968 + self.distance)
                and (y >= 4.687012 - self.distance))
            
            s7 = ((x >= 2.702442 - self.distance) and (x <= 3.926082 + self.distance) and (y <= 8.827066 + self.distance)
                and (y >= 7.846692 - self.distance))
            
            if (s1 or s2 or s3 or s4 or s5 or s6 or s7):
                return True
            
            return False
        
        def check_circles(x, y):
            dist_small = np.sqrt((x - 3.926082)**2 + (y - 8.350689)**2)
            small_c = dist_small <= 0.7 + self.distance
            
            dist_big = np.sqrt((x - 3.409916)**2 + (y - 5.777571)**2)
            big_c = dist_big <= 0.7775 + self.distance

            if (small_c or big_c):
                return True
            
            return False
        
        check1 = check_contour(x, y)
        check2 = check_cashiers(x, y)
        check3 = check_shelves(x, y)
        check4 = check_circles(x, y)

        if (check1 or check2 or check3 or check4):
            return True  # if location is outside of boundaries

        return False  # if location is inside boundaries

    def update_goal(self, x, y):
        self.goal = np.array([x, y])
    
    def check_goal(self, x, y, threshold):
        euc_dist = np.linalg.norm(self.goal - np.array([x, y]))

        if (euc_dist <= threshold):
            return True
        
        return False
