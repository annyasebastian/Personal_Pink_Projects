import math
from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


# please ignore this
def get_solver_mapping():
    return dict(
        astar_ec=ASTAR_Euclidean,
        astar_mh=ASTAR_Manhattan
    )


class ASTAR(object):
    # TODO, Exercise 2:
    # implement A* search (ASTAR)
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - use a 'set()' to store nodes that were already visited
    def solve(self, problem: Problem):
        visited = set()  # set of visited nodes
        f = PriorityQueue()
        start_node = problem.get_start_node()  # getting node with start state
        f.put(self.heuristic(start_node,start_node)+start_node.cost, start_node)  # putting start node and its cost in the queue

        visited.add(start_node)  # marking the start node as visited

        while f:
            node = f.get()  # get the node from the queue
            visited.add(node)  # mark as visited

            if problem.is_end(node):  # check if it is the goal node
                return node

            successor = problem.successors(node)  # getting a list of nodes containing successor states

            for i in successor:
                if i not in visited:
                    # if it hasn't been visited, put it in the queue and then also mark it as visited
                    f.put(self.heuristic(i,node)+i.cost, i)
                    visited.add(i)
        return None


# please note that in an ideal world, the heuristics should actually be part
# of the problem definition, as it assumes domain knowledge about the structure
# of the problem, and defines a distance to the goal state


# this is the ASTAR variant with the euclidean distance as a heuristic
# it is registered as a solver with the name 'astar_ec'
class ASTAR_Euclidean(ASTAR):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.sqrt((cy - gy) ** 2 + (cx - gx) ** 2)


# this is the ASTAR variant with the manhattan distance as a heuristic
# it is registered as a solver with the name 'astar_mh'
class ASTAR_Manhattan(ASTAR):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.fabs((cy - gy)) + math.fabs(cx - gx)
