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

def distance_vector_step(routers, graph, distance_tables):
    updated = False
    new_tables = {}

    for router in routers:
        current_table = distance_tables[router]
        new_table = current_table.copy()

        for neighbor in graph[router]:
            neighbor_table = distance_tables[neighbor]
            cost_to_neighbor = graph[router][neighbor]

            for dest in routers:
                if dest == router:
                    continue
                neighbor_cost_to_dest, _ = neighbor_table[dest]
                new_cost = cost_to_neighbor + neighbor_cost_to_dest

                if new_cost < new_table[dest][0]:
                    new_table[dest] = (new_cost, neighbor)
                    updated = True

        new_tables[router] = new_table

    return new_tables, updated


if __name__ == "__main__":
    routers, topology = read_input()
    graph = build_graph(routers, topology)
    distance_tables = initialize_distance_tables(routers, graph)

    round_num = 0
    converged = False

    while not converged:
        print(f"Distance Tables at t={round_num}")
        for router in sorted(routers):
            print(f"Distance Table of router {router} at t={round_num}:")
            for dest in sorted(routers):
                if dest == router:
                    continue
                cost, via = distance_tables[router][dest]
                cost_str = "INF" if cost == INF else str(cost)
                print(f"{dest} {cost_str} {via if via else 'INF'}")
            print()

        distance_tables, updated = distance_vector_step(routers, graph, distance_tables)
        if not updated:
            converged = True
        round_num += 1
