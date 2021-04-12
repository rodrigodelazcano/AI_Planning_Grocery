from map import Map
new_map = Map()
import math
import numpy as np

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.g = 0
        self.h = 0

def astar(start, goal):
    "Return list of tuples for path"

    start_node = Node(None, start)
    goal_node = Node(None, goal)

    #initialize frontier and closed list
    Frontier = []
    closed_list = []

    Frontier.append(start_node)
    
    while(len(Frontier) > 0):
        # print(len(Frontier))
        current_node = Frontier[0]
        current_index = 0
        
        # finding the current node with lowest value 
        for index, item in enumerate(Frontier):
            if(current_node.f > item.f):
                current_node = item
                current_index = index

        Frontier.pop(current_index)
        closed_list.append(current_node)

        # reached goal node then backtrack and return the path
        distance_to_goal = np.linalg.norm(np.array(current_node.position) - np.array(goal_node.position))
        if(distance_to_goal <= 0.1): 
            print("goal reached")
            path = []
            current = current_node

            while(current != None):
                
                path.append(current.position)
                current = current.parent

            return path[::-1]

        children = []
        delta = 0.25

        for new_pos in [(0,-delta), (0,delta), (-delta,0), (delta,0), (-delta*math.sqrt(1/2),-delta*math.sqrt(1/2)),
                            (-delta*math.sqrt(1/2),delta*math.sqrt(1/2)), (delta*math.sqrt(1/2),-delta*math.sqrt(1/2)),
                            (delta*math.sqrt(1/2),delta*math.sqrt(1/2))]:

            child_node = Node(current_node, (current_node.position[0]+new_pos[0], current_node.position[1]+new_pos[1]))
            
            # child position out of maze
            if( child_node.position[0] > 15 or child_node.position[0] < 0 or child_node.position[1] < 0 or child_node.position[1] >  13):
                continue

            # child position is not same as obstacle position
            if(new_map.check_collision(child_node.position[0], child_node.position[1]) == True):
                # if(maze[child_node.position[0]][child_node.position[1]] != 0):
                continue

            children.append(child_node)

        for child in children:

            #remove child if in closed list
            for closed_child in closed_list:
                if(child == closed_child):
                    continue

            child.g = current_node.g+delta
            child.h = ((child.position[0]-goal_node.position[0])**2) + ((child.position[1]-goal_node.position[1])**2)
            child.f = child.g + child.h

            for frontier_child in Frontier:
                if((child == frontier_child) and (child.g > frontier_child.g)):
                    continue
            
            Frontier.append(child)



def main():
    
    start = (1,1)
    goal = (5,2)
    # new_map = map.Map()
    print(new_map.check_collision(goal[0], goal[1]))
    print(new_map.check_collision(start[0], start[1]))
    

    path = astar(start,goal)
    print(path)
    # print(maze)

if __name__ == '__main__':
    main()