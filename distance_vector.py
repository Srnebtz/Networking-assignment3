import sys

INF = float('inf')

def read_input():
    routers = []
    topology = []

    for line in sys.stdin:
        line = line.strip()
        if line == "START":
            break
        if line:
            routers.append(line)

    for line in sys.stdin:
        line = line.strip()
        if line == "UPDATE":
            break
        if line:
            parts = line.split()
            if len(parts) == 3:
                topology.append((parts[0], parts[1], int(parts[2])))

    return routers, topology

def build_graph(routers, topology):
    graph = {router: {} for router in routers}
    for src, dst, cost in topology:
        graph[src][dst] = cost
        graph[dst][src] = cost 
    return graph

def initialize_distance_tables(routers, graph):
    distance_tables = {}
    for router in routers:
        table = {}
        for target in routers:
            if router == target:
                table[target] = (0, router)
            elif target in graph[router]:
                table[target] = (graph[router][target], target)
            else:
                table[target] = (INF, None)
        distance_tables[router] = table
    return distance_tables

if __name__ == "__main__":
    routers, topology = read_input()
    graph = build_graph(routers, topology)
    distance_tables = initialize_distance_tables(routers, graph)

    for router in routers:
        print(f"Initial Distance Table for {router}:")
        for dest in sorted(distance_tables[router]):
            dist, via = distance_tables[router][dest]
            dist_str = "INF" if dist == INF else str(dist)
            print(f"{dest}: {dist_str} via {via}")
        print()

