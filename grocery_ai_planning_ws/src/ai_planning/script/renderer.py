import cv2
from map import Map
import numpy as np
from products import Products

class Renderer(Map):
    def __init__(self, radius=0.177, clearance=0.15):
        super().__init__(radius, clearance)
        
        self.blank_image = np.ones(shape=[1400, 1600, 3], dtype=np.uint8)

        self.font = cv2.FONT_ITALIC

        self.products = Products()

        self.cashier_coord = (1465.5536, 1400 - 304.2128)
        
        distance = (radius + clearance)*100

        boundrec1 =  np.array([[[0, 1400],[0, 1400 - 476.5123],[119.9979, 1400 - 476.5123],[119.9979,1400 - 974.8759],
                                [113.0248, 1400 - 1093.9484], [326.3999, 1400 - 1215.5476], [803.7341, 1400 - 1345.3712], [1052.8966, 1400 - 1345.3712],
                                [1161.2505, 1400 - 1301.1247], [1505.3117, 1400 - 953.9164], [1544.8179, 1400 - 891.2024], [1544.8179, 1400]]], np.int32)

        cv2.fillConvexPoly(self.blank_image, boundrec1, (255, 255, 255))

        x1 = ((self.line2.coeff[1]-self.line1.coeff[1])/(self.line1.coeff[0]-self.line2.coeff[0]))
        y1 = (x1 * self.line1.coeff[0] + self.line1.coeff[1])

        x2 = ((self.line3.coeff[1]-self.line2.coeff[1])/(self.line2.coeff[0]-self.line3.coeff[0]))
        y2 = (x2 * self.line2.coeff[0] + self.line2.coeff[1])

        x2 = ((self.line3.coeff[1]-self.line2.coeff[1])/(self.line2.coeff[0]-self.line3.coeff[0]))*100
        y2 = (x2/100 * self.line2.coeff[0] + self.line2.coeff[1])*100

        boundrec2 =  np.array([[[0 + distance, 1400 - distance],[0 + distance, 1400 - 476.5123 + distance],[119.9979 + distance, 1400 - 476.5123 + distance],[119.9979 + distance, 1400 - 974.8759],
                                [x1*100 , 1400 - y1*100], [x2*100 , 1400 - y2*100], [803.7341, 1400 - 1345.3712 + distance], [1052.8966, 1400 - 1345.3712 + distance],
                                [1161.2505, 1400 - 1301.1247], [1505.3117, 1400 - 953.9164], [1544.8179 - distance, 1400 - 891.2024], [1544.8179 - distance, 1400 - distance]]], np.int32)

        cv2.fillConvexPoly(self.blank_image, boundrec2, (211,211,211))

        # Cashiers
        cashier1_d = np.array([[[525.1926 - distance, 1400 - 224.6674 + distance], [525.1926 - distance, 1400 - 369.3339 - distance],
                            [603.5216 + distance, 1400 - 369.3339 - distance], [603.5216 + distance, 1400 - 224.6674 + distance]]], np.int32)
        cashier2_d = np.array([[[717.2170 - distance, 1400 - 224.6674 + distance], [717.2170 - distance, 1400 - 369.3339 - distance],
                            [797.5383 + distance, 1400 - 369.3339 - distance], [797.5383 + distance, 1400 - 224.6674 + distance]]], np.int32)
        cashier3_d = np.array([[[904.0226 - distance, 1400 - 224.6674 + distance], [904.0226 - distance, 1400 - 369.3339 - distance],
                            [983.2662 + distance, 1400 - 369.3339 - distance], [983.2662 + distance, 1400 - 224.6674 + distance]]], np.int32)
        cashier4_d = np.array([[[1093.1436 - distance, 1400 - 224.6674 + distance], [1093.1436 - distance, 1400 - 369.3339 - distance],
                            [1175.5313 + distance, 1400 - 369.3339 - distance], [1175.5313 + distance, 1400 - 224.6674 + distance]]], np.int32)
        cashier5_d = np.array([[[1283.3400 - distance, 1400 - 224.6674 + distance], [1283.3400 - distance, 1400 - 369.3339 - distance],
                            [1364.6369 + distance, 1400 - 369.3339 - distance], [1364.6369 + distance, 1400 - 224.6674 + distance]]], np.int32)
        cv2.fillPoly(self.blank_image, cashier1_d, (255,255,255))
        cv2.fillPoly(self.blank_image, cashier2_d, (255,255,255))
        cv2.fillPoly(self.blank_image, cashier3_d, (255,255,255))
        cv2.fillPoly(self.blank_image, cashier4_d, (255,255,255))
        cv2.fillPoly(self.blank_image, cashier5_d, (255,255,255))


        cashier1 = np.array([[[525.1926, 1400 - 224.6674], [525.1926, 1400 - 369.3339],
                            [603.5216, 1400 - 369.3339], [603.5216, 1400 - 224.6674]]], np.int32)
        cashier2 = np.array([[[717.2170, 1400 - 224.6674], [717.2170 , 1400 - 369.3339],
                            [797.5383, 1400 - 369.3339], [797.5383 , 1400 - 224.6674]]], np.int32)
        cashier3 = np.array([[[904.0226, 1400 - 224.6674 ], [904.0226 , 1400 - 369.3339 ],
                            [983.2662, 1400 - 369.3339 ], [983.2662 , 1400 - 224.6674 ]]], np.int32)
        cashier4 = np.array([[[1093.1436, 1400 - 224.6674], [1093.1436 , 1400 - 369.3339 ],
                            [1175.5313, 1400 - 369.3339 ], [1175.5313 , 1400 - 224.6674]]], np.int32)
        cashier5 = np.array([[[1283.3400, 1400 - 224.6674], [1283.3400 , 1400 - 369.3339],
                            [1364.6369, 1400 - 369.3339], [1364.6369 , 1400 - 224.6674 ]]], np.int32)
        cv2.fillPoly(self.blank_image, cashier1, (0,0,0))
        cv2.fillPoly(self.blank_image, cashier2, (0,0,0))
        cv2.fillPoly(self.blank_image, cashier3, (0,0,0))
        cv2.fillPoly(self.blank_image, cashier4, (0,0,0))
        cv2.fillPoly(self.blank_image, cashier5, (0,0,0))

        #Circles

        cv2.circle(self.blank_image, (341, 1400 - 578), 78 + int(distance), (255, 255, 255), -1)
        cv2.circle(self.blank_image, (341, 1400 - 578), 78, (0, 0, 0), -1)

        # Shelves

        shelf1_d = np.array([[[625.3904 - distance, 1400 - 1076.4730 - distance], [625.3904 - distance, 1400 - 977.5013 + distance], 
                            [960.5268 + distance, 1400 - 977.5013 + distance], [960.5268 + distance, 1400 - 1076.4730 - distance]]], np.int32)
        shelf1 = np.array([[[625.3904, 1400 - 1076.4730], [625.3904, 1400 - 977.5013], 
                            [960.5268, 1400 - 977.5013], [960.5268, 1400 - 1076.4730]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf1_d, (255,255,255))
        cv2.fillPoly(self.blank_image, shelf1, (0,0,0))

        shelf2_d = np.array([[[625.3904 - distance, 1400 - 620.9282 - distance], [625.3904 - distance, 1400 - 526.6344 + distance], 
                            [960.5268 + distance, 1400 - 526.6344 + distance], [960.5268 + distance, 1400 - 620.9282 - distance]]], np.int32)
        shelf2 = np.array([[[625.3904, 1400 - 620.9282], [625.3904, 1400 - 526.6344], 
                            [960.5268, 1400 - 526.6344], [960.5268, 1400 - 620.9282]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf2_d, (255,255,255))
        cv2.fillPoly(self.blank_image, shelf2, (0,0,0))

        shelf3_d = np.array([[[625.3904  - distance, 1400 - 843.2007 - distance], [625.3904  - distance, 1400 - 750.5381 + distance], 
                            [722.7457 + distance, 1400 - 750.5381 + distance], [722.7457 + distance, 1400 - 843.2007 - distance]]], np.int32)
        shelf3 = np.array([[[625.3904 , 1400 - 843.2007], [625.3904 , 1400 - 750.5381], 
                            [722.7457, 1400 - 750.5381], [722.7457, 1400 - 843.2007]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf3_d, (255,255,255))
        cv2.fillPoly(self.blank_image, shelf3, (0,0,0))

        shelf4_d = np.array([[[862.2844  - distance, 1400 - 843.2007 - distance], [862.2844  - distance, 1400 - 750.5381 + distance], 
                            [961.0721+ distance, 1400 - 750.5381 + distance], [961.0721 + distance, 1400 - 843.2007 - distance]]], np.int32)
        shelf4 = np.array([[[862.2844 , 1400 - 843.2007], [862.2844 , 1400 - 750.5381], 
                            [961.0721, 1400 - 750.5381], [961.0721, 1400 - 843.2007]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf4_d, (255,255,255))
        cv2.fillPoly(self.blank_image, shelf4, (0,0,0))

        shelf5_d = np.array([[[270.2442 - distance, 1400 - 882.7066 - distance], [270.2442  - distance, 1400 - 784.6692 + distance], 
                            [392.6082+ distance, 1400 - 784.6692 + distance], [392.6082 + distance, 1400 - 882.7066 - distance]]], np.int32)
        shelf5 = np.array([[[270.2442 , 1400 - 882.7066], [270.2442 , 1400 - 784.6692], 
                            [392.6082, 1400 - 784.6692], [392.6082, 1400 - 882.7066]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf5_d, (255,255,255))
        cv2.circle(self.blank_image, (393, 1400 - 835), 70 + int(distance), (255, 255, 255), -1)
        cv2.fillPoly(self.blank_image, shelf5, (0,0,0))
        cv2.circle(self.blank_image, (393, 1400 - 835), 70, (0, 0, 0), -1)

        shelf6_d = np.array([[[1316.0530  - distance, 1400 - 616.5968 - distance], [1316.0530  - distance, 1400 - 468.7012 + distance], 
                            [1393.9310+ distance, 1400 - 468.7012 + distance], [1393.9310 + distance, 1400 - 616.5968 - distance]]], np.int32)
        shelf6 = np.array([[[1316.0530 , 1400 - 616.5968], [1316.0530 , 1400 - 468.7012], 
                            [1393.9310, 1400 - 468.7012], [1393.9310, 1400 - 616.5968]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf6_d, (255,255,255))
        cv2.fillPoly(self.blank_image, shelf6, (0,0,0))

        shelf6_d = np.array([[[1097.8244  - distance, 1400 - 968.7450 - distance], [1097.8244  - distance, 1400 - 632 + distance], 
                            [1197.4152 + distance, 1400 - 632 + distance], [1197.4152 + distance, 1400 - 968.7450 - distance]]], np.int32)
        shelf6 = np.array([[[1097.8244 , 1400 - 968.7450], [1097.8244 , 1400 - 632], 
                            [1197.4152, 1400 - 632], [1197.4152, 1400 - 968.7450]]], np.int32)
        cv2.fillPoly(self.blank_image, shelf6_d, (255,255,255))
        cv2.fillPoly(self.blank_image, shelf6, (0,0,0))

    
    def draw_product_location(self, list):
        for product in list:
            x = round(self.products.product_list[product][0]*100)
            y = round(self.products.product_list[product][1]*100)
            cv2.circle(self.blank_image, (x,1400 - y), 50, (0,0,255), 2)
            cv2.putText(self.blank_image,product, (x - 40,1400 - y - 50), self.font, 1, (0,0,255), 3, cv2.LINE_AA)
    

    def draw_random_list(self, list):

        prod_list_to_draw = [np.array([100, 1400 - 100])]
        for product in list:
            x = round(self.products.product_list[product][0]*100)
            y = round(self.products.product_list[product][1]*100)          
            prod_coord = np.asarray((x, 1400 - y), np.int32)
            prod_list_to_draw.append(prod_coord)

        cashier_coord = np.asarray(self.cashier_coord, np.int32)
        prod_list_to_draw.append(cashier_coord)
        pts = np.array(prod_list_to_draw)
        cv2.polylines(self.blank_image, [pts], False, (255,0,0), 3, lineType=8)
    
    def draw_GBFS_list(self, list):
        prod_list_to_draw = [np.array([100, 1400 - 100])]
        for product in list:
            x = round(self.products.product_list[product][0]*100)
            y = round(self.products.product_list[product][1]*100)          
            prod_coord = np.asarray((x, 1400 - y), np.int32)
            prod_list_to_draw.append(prod_coord)

        cashier_coord = np.asarray(self.cashier_coord, np.int32)
        prod_list_to_draw.append(cashier_coord)
        pts = np.array(prod_list_to_draw)
        cv2.polylines(self.blank_image, [pts], False, (0,255,0), 6, lineType=8)
    
    def draw_Astar_path(self, path):
        wayp_list = []
        for wayp in path:
            wayp_coord = np.asarray((wayp[0]*100, 1400 - wayp[1]*100), np.int32)
            wayp_list.append(wayp_coord)
        
        pts = np.array(wayp_list)
        cv2.polylines(self.blank_image, [pts], False, (0,0,255), 3, lineType=8)


    def draw_duration_cost(self, seconds, cost):
        cv2.putText(self.blank_image,"Time: " + str(round(seconds,2)) + " s", (1350,1400 - 1300), self.font, 1, (255,255,255), 3, cv2.LINE_AA)
        cv2.putText(self.blank_image,"Cost: " + str(round(cost,2)), (1350,1400 - 1250), self.font, 1, (255,255,255), 3, cv2.LINE_AA)


    def render(self):
        self.blank_image = cv2.resize(self.blank_image, (700,800), fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

        cv2.imshow("Grocery Map", self.blank_image)
        cv2.waitKey()


        
