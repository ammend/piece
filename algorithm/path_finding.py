# -*- coding: utf-8 -*-

"""
- Dijkstra
- Best First Search
- A*
"""

# Dijkstra
from math import dist
import queue


def dijkstra():
    """
    S -> A 6
    S -> B 2
    B -> A 3
    A -> E 1
    B -> E 5
    """
    infinity = float("inf")
    graph = {}
    graph ["S"] = {}
    graph ["A"] = {}
    graph ["B"] = {}
    graph ["E"] = {}
    graph ["S"]["A"] = 6
    graph ["S"]["B"] = 2
    graph ["B"]["A"] = 3
    graph ["A"]["E"] = 1
    graph ["B"]["E"] = 5
    start = "S"
    end = "E"
    costs = {}
    for key in graph:
        costs[key] = infinity
    costs["S"] = 0
    parents = {}
    for k in graph:
        parents[k] = None
    processed = set() 
    def extract_min(graph, processed, costs):
        lowest_cost = infinity
        lowest_cost_node = None
        for node in costs:
            if not node in processed:
                if costs[node] < lowest_cost:
                    lowest_cost = costs[node]
                    lowest_cost_node = node
        return lowest_cost_node
    node = extract_min(graph, processed, costs)
    while node != None and node != "E":
        cost = costs[node]
        neighbors = graph[node]
        for key in neighbors:
            new_cost = cost + graph[node][key]
            if new_cost < costs[key]:
                costs[key] = new_cost
                parents[key] = node
        processed.add(node)
        node = extract_min(graph, processed, costs)

    def find_shortest_path(parents, start, end):
        node = end
        shortest_path = [node]
        while parents[node] != start:
            shortest_path.append(parents[node])
            node = parents[node]
        shortest_path.append(start)
        return shortest_path
    shortest_path = find_shortest_path(parents, start, end)
    shortest_path.reverse()
    print(shortest_path)
    
def bfs():
    """
    ******
    ******
    **$$$*
    *@**$*
    **$$$&
    ******

    $ 障碍
    @ 起点
    & 终点
    * 可通过
    """
    graph = [[0 for i in range(6)] for i in range(6)]
    graph[2][1] = 1
    graph[3][1] = 1
    graph[4][1] = 1
    graph[4][2] = 1
    graph[4][3] = 1
    graph[3][3] = 1
    graph[2][3] = 1

    start = (1,2)
    end = (5,1)
    shortest_path=[]
    # 1.探测周围的节点，上下左右，返回可行的候选集合
    # 2.选择曼哈顿距离最小的点
    # 3.重复1&2，直至最小的点是终点
    def detect(graph, node):
        up = (node[0], node[1]+1)
        down = (node[0], node[1]-1)
        left = (node[0]-1, node[1])
        right = (node[0]+1, node[1])
        def conflict(graph, node):
            if node[0] < 0 or node[1] < 0:
                return False
            if graph[node[0]][node[1]] == 1:
                return False
            return True
        nodes = []
        if conflict(graph, up):
            nodes.append(up)
        if conflict(graph, down):
            nodes.append(down)
        if conflict(graph, left):
            nodes.append(left)
        if conflict(graph, right):
            nodes.append(right)
        return nodes
    def manhattan_distance(start, end):
        return abs(start[0]-end[0]) + abs(start[1]-end[1])
    infinity = float("inf")
    nearest_node = start
    while nearest_node != None:
        shortest_path.append(nearest_node)
        if nearest_node == end:
            break
        candicates = detect(graph, nearest_node)
        nearest_node = None
        nearest_node_instance = infinity  
        for key in candicates:
            distance = manhattan_distance(key, end)
            if nearest_node_instance > distance:
                nearest_node = key
    print(shortest_path)

class Graph(object):
    def __init__(self) -> None:
        super().__init__()
    
    def neighbors(self, current):
        pass

    def start(self):
        pass

    def end(self):
        pass

    def cost(self, current, next):
        pass
    
    def print_path(self, came_from):
        current = self.end()
        path = []
        while current != self.start():
            path.append(current)
            current = came_from(current)
        path.append(self.start())
        path.reverse()
        self.print(path)

    def heuristic(self, end, current):
        return abs(end[0]-current[0]) + abs(end[1]-current[1])

    def breadth_first_search(self):
        frontier = queue.Queue()
        reached = set()
        came_from = {}

        start = self.start()
        end = self.end()

        frontier.put(start)
        reached.add(start)
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()
            if current == end:
                break
            for next in self.neighbors(current):
                if next not in reached:
                    frontier.put(next)
                    reached.add(next)
                    came_from[next] = current 

        self.print_path(came_from)


    def dijkstra(self):
        frontier = queue.PriorityQueue()
        came_from = {}
        cost_so_far = {}
        start = self.start()
        end = self.end()

        frontier.put(start, 0)
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    frontier.put(next, new_cost)
                    came_from[next] = current

        self.print_path(came_from)
    


    def best_first_search(self):
        frontier = queue.PriorityQueue()
        came_from = {}
        start = self.start()
        end = self.end()

        frontier.put(start, 0)
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next in self.neighbors(current):
                if next not in came_from:
                    priority = self.heuristic(end, next)
                    frontier.put(next, priority)
                    came_from[current] = next

        self.print_path(came_from) 

    def a_start(self):
        frontier = queue.PriorityQueue()
        came_from = {}
        cost_so_far = {}
        start = self.start()
        end = self.end()

        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == end:
                break

            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(end, next)
                    frontier.put(next, priority)
                    came_from[next] = current
    def print(path):
        pass

if __name__ == "__main__":
    #dijkstra()
    bfs()
