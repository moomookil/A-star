class node:
    def __init__(self, state, estimate=0, cost=0, parent=None):
        '''Create a search tree Node, derived by exapnsion of a parent with state 'state', current cost 'cost' and
        estimate = current cost + heristic bein 'estimate', and parent expansion of which resulted in this node being a node
        '''
        self.state = state
        self.cost = cost
        if estimate:
            self.estimate = estimate
        if parent:
            self.parent = parent

    def __cmp__(self, other):
            '''_cmp_ method allows for comparions between objects of this class where comparison is done using the attribute estimate
             '''
            return cmp(self.estimate, other.estimate)


class SimpleGraph:
    ''' consists of two dictionaries:
    a. first contains directed edges that are pairs (name of target state, cost of edge expansion)
    each entry into this dictionary is a state (key): list off edges [ (state,cost), ..., (state,cost)]
    b. second contain pairs key: value where key is a state and value is value of heuristic function for this state

    Neighbors function returns the list of of edges of a state (=id) that is used as a key in dictionary
    '''
    def __init__(self):
        self.edges = {}
        self.heuristic = {}

    def neighbors(self, id):
        return self.edges[id]

import heapq

class PriorityQueue:
    '''Priority queue is just an envelope of a binary heap. see descirption at https://docs.python.org/2/library/heapq.html'''
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item):
        self.item = item
        heapq.heappush(self.elements, item)

    def get(self):
        return heapq.heappop(self.elements)


def A_star_search(graph, start, goal):
    '''create node for initial state 'start': find its heuristic by key (state) in heuristic list (grpah.heuristic)'''
    list = graph.heuristic
    est = list.get(start)
    start_n = node(start,est)
    frontier = PriorityQueue()
    frontier.put(start_n)
    visited = []


    while not frontier.empty():
        # while frontier is not empty get the first node. If it is goal print the cost of it and exit
        current = frontier.get()
        if current.state == goal:
            cost=current.cost
            print("cost of goal %s is %r" % (goal, cost))
            #printing string variable %s and %r real vaiable
            break
        #otherwise print visited state
        current_s = current.state
        print("Visiting %r" % current_s)
        visited.append(current_s)
        print visited
        for next in graph.neighbors(current_s):
            if next not in visited:
                cst = current.cost + next[1]
                est = list.get(next[0]) + cst
                print list.get(current_s), "h(n)", '<=', est, "(c,a,c') + h(n')"
                if list.get(current_s) <= est:
                    next_n = node(next[0], est, cst, current_s)
                    frontier.put(next_n)
                else:
                    print "This is an inconsistent heuristic"
                    exit()




                #if next not in visited:

            #expand neighbor states (next[0]) of the state of current node (current_s) in graph by creating for them a new node
            # - one for each neighbor state with cost = cost of current + cost of an edge (next[1])
            # and f = heuristic of this state (list.get(next[0])+ its accumulated cost (current.cost+next[1])



import ast
y = {}
z = {}
# graph is formatted so that all lines with the exception of the las line contain correct dictionary for adjacency list
# of nodes i.e. {state:[(stateid,weight of directed edge),...,(stateid,weight of directed edge)]}
#the last line contain the heuristic function given in format 'h={state:value, ..., state:value}
#note that in each line first 2 symbols and last 2 symbols are special symbols
# substring of strin s can be given as s[a:-b] where a, b position numbers from begiing and end of the line resp.
# str() forces conversion of input data type to str
#line.split() whole line until cr
#update dictionary appends values to dictionary
#as.literl_eval evaluates stting wrt to standard data types and converts if possible
with open('C:/Users/Brian/Documents/CST411-AI/graph-weighted.txt', 'r') as f:
    for line in f:
        cur = str(line.split())[2:-2]
        s=cur[0]
        if s is 'h':
            cur=cur[2:]
            d1 = ast.literal_eval(cur)
            z.update(d1)
        else:
            d = ast.literal_eval(cur)
            y.update(d)

example_graph = SimpleGraph()
example_graph.edges = y
example_graph.heuristic = z
start = raw_input('Starting point: ')
goal = raw_input('Goal: ')

A_star_search(example_graph,start,goal)
exit()