import sys

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

if __name__ == "__main__":
    routers, topology = read_input()
    print("Routers:", routers)
    print("Topology:", topology)
