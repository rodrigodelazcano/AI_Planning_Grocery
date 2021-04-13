from products import Products
products = Products()


class Node():

    def __init__(self, me=None, position=None):
        self.me = me
        self.position = position
        self.node_visited = []
        self.f = 0


def dist(current_node, new_node):
    return (current_node.position[0] - new_node.position[0])**2 + (current_node.position[1] - new_node.position[1])**2 

def gbfs(product_dict):

    start = (1,1) #starting point
    start_node = Node("start", start)

    open_list = []
    closed_list = []
    open_list.append(start_node)
    flag = 0

    while(len(open_list) > 0):
        current_node = open_list[0]
        current_index = 0

        open_list.pop(current_index) #take out first element from open list and add to closed list
        closed_list.append(current_node)

        for i in range(len(product_dict)):
            if(current_node.me == product_dict[i]): continue

            if(len(current_node.node_visited) != None):
                for j in range(len(current_node.node_visited)):
                    if(product_dict[i] == current_node.node_visited[j]): flag = 1
            if(flag == 1): 
                flag = 0
                continue               

            new_node = Node(product_dict[i], products.product_list[product_dict[i]])
            new_node.f = current_node.f + dist(current_node, new_node)
            new_node.node_visited = current_node.node_visited.copy()
            new_node.node_visited.append(current_node.me)
            open_list.append(new_node)


    return_index = 0
    f_value = 9999

    #return closed list element with lowest f value
    for k in range(len(closed_list)):
        print(closed_list[k].me, closed_list[k].node_visited, closed_list[k].f)
        if(len(closed_list[k].node_visited) == len(product_dict)):
            if(closed_list[k].f < f_value):
                f_value = closed_list[k].f
                return_index = k

    closed_list[return_index].node_visited.append(closed_list[return_index].me)
    closed_list[return_index].node_visited.pop(0)
    return closed_list[return_index].node_visited


def main():     
    product_dict = products.get_random_list()
    ordered_list = gbfs(product_dict) # Do not send start(1,1) position
    print(product_dict)
    print(ordered_list)


if __name__ == '__main__':
    main()