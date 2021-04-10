from pyhop import hop
import a_star

# declaration of actions
def move_robot(state, r, goal_point):
	print(a_star.astar(state.loc[r], goal_point))
	state.loc[r] = goal_point	
	return state

def pay(state, r):
	state.cash[r] -= state.owe[r]
	state.owe[r] = 0
	return state

hop.declare_operators(move_robot, pay)
print('')
hop.print_operators(hop.get_operators())


# declaration of methods
def normal_shopping(state, r):
	return [('move_robot', r, (5,2))]

def optimal_shopping(state, r):
	pass

hop.declare_methods('buy_groceries', normal_shopping, optimal_shopping)
print('')
hop.print_methods(hop.get_methods())


state = hop.State('state')
state.loc = {'robot':(0,0)}
state.cash = {'robot': 10}
state.owe = {'robot':0}
state.cart = []
state.list = []
state.path = []


print('- If verbose=3, Pyhop also prints the intermediate states:')
hop.plan(state,
         [('buy_groceries','robot')],
         hop.get_operators(),
         hop.get_methods(),
         verbose=3)

print(state.path)
