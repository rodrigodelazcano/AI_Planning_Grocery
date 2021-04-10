import numpy as np
import math

class Line():
    def __init__(self, x1, x2, y1, y2, distance, side):
        self.coeff = np.polyfit([x1, x2],[y1, y2], 1)
        self.side = side ## side 0 left, side 1 right

        if distance > 0:
            if (self.coeff[0] > 0 and side == 0):
                self.coeff[1] = self.coeff[1] + distance * math.sin(1.57 - math.atan(self.coeff[0]))
            elif (self.coeff[0] > 0 and side == 1):
                self.coeff[1] = self.coeff[1] - distance * math.sin(1.57 - math.atan(self.coeff[0]))
            elif (self.coeff[0] < 0 and side == 0):
                self.coeff[1] = self.coeff[1] - distance * math.sin(1.57 - math.atan(self.coeff[0]))
            elif (self.coeff[0] < 0 and side == 1):
                self.coeff[1] = self.coeff[1] + distance * math.sin(1.57 - math.atan(self.coeff[0]))

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
    def __init__(self, clearance = 0, radius = 0):

        self.clearance = clearance
        self.radius = radius
        self.distance = clearance + radius
        self.goal = None

        self.line1 = Line(1.15, 1.04, 9.79, 10.93, self.distance, 0)
        self.line2 = Line(1.04, 3.25, 10.93, 12.17, self.distance, 0)
        self.line3 = Line(3.25, 8.03, 12.17, 13.45, self.distance, 0)
        self.line4 = Line(11.56, 15.07, 13, 9.53, self.distance, 1)
        self.line5 = Line(15.07, 15.38, 9.53, 8.92, self.distance, 1)

    def check_collision(self, x, y):
        def check_contour(x, y):
            c1 = x <= 0 + self.distance
            c2 = y >= 4.85 - self.distance and x <= 1.15 + self.distance and self.line1.check_boundary(x, y)
            c3 = x >= 15.38 - self.distance
            c4 = y <= 0 + self.distance
            c5 = y >= 13.46 - self.distance
            total_c = c1 or c2 or c3 or c4 or c5
            c_line2 = self.line2.check_boundary(x, y)
            c_line3 = self.line3.check_boundary(x, y)
            c_line4 = self.line4.check_boundary(x, y)
            c_line5 = self.line5.check_boundary(x, y)

            if (total_c or c_line2 or c_line3 or c_line4 or c_line5):
                return True ##out of boundary
            
            return False ##inside boundary
        
        def check_cashiers(x ,y):
            cs_y = (y >= 2.27 - self.distance) and (y <= 3.77 + self.distance)
            cs1 = ((x >= 5.21 - self.distance) and (x <= 6 + self.distance) and cs_y)
            cs2 = ((x >= 7.07 - self.distance) and (x <= 7.91 + self.distance) and cs_y)
            cs3 = ((x >= 8.99 - self.distance) and (x <= 9.84 + self.distance) and cs_y)
            cs4 = ((x >= 10.89 - self.distance) and (x <= 11.7 + self.distance) and cs_y)
            cs5 = ((x >= 12.8 - self.distance) and (x <= 13.58 + self.distance) and cs_y)

            if (cs1 or cs2 or cs3 or cs4 or cs5):
                return True
            
            return False
        
        def check_shelves(x, y):
            s_x = (x >= 6.2 - self.distance) and (x <= 9.6 + self.distance)
            s_y = (y <= 8.51 + self.distance) and (y >= 7.47 - self.distance)
            s1 = (s_x and (y <= 10.83 + self.distance) and (y >= 9.79 - self.distance))
            s2 = (s_x and (y <= 6.3 + self.distance) and (y >= 5.25 - self.distance))
            s3 = (x >= 6.2 - self.distance) and (x <= 7.22 + self.distance) and s_y
            s4 = (x >= 8.6 - self.distance) and (x <= 9.6 + self.distance) and s_y
            s5 = ((x >= 10.9 - self.distance) and (x <= 11.97 + self.distance) and (y <= 9.75 + self.distance)
                and (y >= 6.32 - self.distance))
            s6 = ((x >= 12.98 - self.distance) and (x <= 14.03 + self.distance) and (y <= 6.32 + self.distance)
                and (y >= 4.55 - self.distance))
            
            s7 = ((x >= 2.65 - self.distance) and (x <= 3.9 + self.distance) and (y <= 9 + self.distance)
                and (y >= 7.73 - self.distance))
            
            if (s1 or s2 or s3 or s4 or s5 or s6 or s7):
                return True
            
            return False
        
        def check_circles(x, y):
            dist_small = np.sqrt((x - 3.9)**2 + (y - 8.37)**2)
            small_c = dist_small <= 0.73 + self.distance
            
            dist_big = np.sqrt((x - 3.37)**2 + (y - 5.77)**2)
            big_c = dist_big <= 0.75 + self.distance

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
