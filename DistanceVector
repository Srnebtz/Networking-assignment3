#!/usr/bin/env python3
import sys
import math
import copy

INF = float("inf")

def parse_input():
    routers = []
    edges = []
    updates = []

    # Read until START
    for line in sys.stdin:
        line = line.strip()
        if line == "START":
            break
        if line:
            routers.append(line)

    # Read until UPDATE
    for line in sys.stdin:
        line = line.strip()
        if line == "UPDATE":
            break
        if line:
            parts = line.split()
            if len(parts) == 3:
                edges.append((parts[0], parts[1], int(parts[2])))

    # Read until END
    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        if line:
            parts = line.split()
            if len(parts) == 3:
                updates.append((parts[0], parts[1], int(parts[2])))

    return routers, edges, updates

def initialize_tables(routers, edges):
    neighbors = {r: {} for r in routers}
    dist = {r: {d: INF for d in routers} for r in routers}
    next_hop = {r: {d: None for d in routers} for r in routers}

    for r in routers:
        dist[r][r] = 0
        next_hop[r][r] = r

    for u, v, w in edges:
        neighbors[u][v] = w
        neighbors[v][u] = w
        dist[u][v] = w
        dist[v][u] = w
        next_hop[u][v] = v
        next_hop[v][u] = u

    return neighbors, dist, next_hop

def print_distance_tables(dist, next_hop, routers, t):
    for r in sorted(routers):
        print(f"Distance Table of router {r} at t={t}:")
        for d in sorted(routers):
            if d == r:
                continue
            cost = dist[r][d]
            nh = next_hop[r][d]
            cost_str = "INF" if cost == INF else str(cost)
            nh_str = nh if nh else "?"
            print(f"{d} {nh_str} {cost_str}")
        print()

def print_routing_tables(dist, next_hop, routers):
    for r in sorted(routers):
        print(f"Routing Table of router {r}:")
        for d in sorted(routers):
            if d == r:
                continue
            cost = dist[r][d]
            nh = next_hop[r][d]
            if cost == INF or nh is None:
                print(f"{d},INF,INF")
            else:
                print(f"{d},{nh},{cost}")
        print()

def distance_vector(routers, neighbors, dist, next_hop):
    t = 0
    while True:
        updated = False
        prev_dist = copy.deepcopy(dist)
        for r in routers:
            for d in routers:
                if d == r:
                    continue
                min_cost = dist[r][d]
                min_next = next_hop[r][d]
                for n in neighbors[r]:
                    cost = neighbors[r][n] + dist[n][d]
                    if cost < min_cost:
                        min_cost = cost
                        min_next = n
                dist[r][d] = min_cost
                next_hop[r][d] = min_next

        print_distance_tables(dist, next_hop, routers, t)
        t += 1

        if dist == prev_dist:
            break

    print_routing_tables(dist, next_hop, routers)

def apply_updates(routers, neighbors, dist, next_hop, updates):
    for u, v, w in updates:
        if u not in routers:
            routers.append(u)
            neighbors[u] = {}
            dist[u] = {d: INF for d in routers}
            next_hop[u] = {d: None for d in routers}
            dist[u][u] = 0
            next_hop[u][u] = u
            for r in routers:
                dist[r][u] = INF
                next_hop[r][u] = None

        if v not in routers:
            routers.append(v)
            neighbors[v] = {}
            dist[v] = {d: INF for d in routers}
            next_hop[v] = {d: None for d in routers}
            dist[v][v] = 0
            next_hop[v][v] = v
            for r in routers:
                dist[r][v] = INF
                next_hop[r][v] = None

        if w == -1:
            if v in neighbors[u]:
                del neighbors[u][v]
            if u in neighbors[v]:
                del neighbors[v][u]
        else:
            neighbors[u][v] = w
            neighbors[v][u] = w
            dist[u][v] = w
            dist[v][u] = w
            next_hop[u][v] = v
            next_hop[v][u] = u

def main():
    routers, edges, updates = parse_input()
    neighbors, dist, next_hop = initialize_tables(routers, edges)
    distance_vector(routers, neighbors, dist, next_hop)
    if updates:
        apply_updates(routers, neighbors, dist, next_hop, updates)
        distance_vector(routers, neighbors, dist, next_hop)

if __name__ == "__main__":
    main()
