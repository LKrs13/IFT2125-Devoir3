from copy import deepcopy
from ford_fulkerson import ford_fulkerson
import sys

def get_file_name():
    if len(sys.argv) != 2:
        print("Usage: python3 controle.py instance.txt")
        return
    file_name = f'data/{sys.argv[1]}'
    return file_name

def print_output(file_name, answer):
    output = [f'{x} {y}' for x, y in answer]
    output = '\n'.join(output)
    with open(f"resultat_{file_name[5:-4]}.txt", 'w') as file:
        file.write(output)

def parse_input_file(file_name):
    with open(file_name) as f:
        line = f.readline().strip().split(';')

        num_vertices = int(line[0])
        k = int(line[1])
        graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

        # Parse each vertex and its outgoing arcs
        for i in range(num_vertices):
            line = f.readline().strip().split(';')
            vertex_id = int(line[0])

            if len(line) == 1:
                continue

            # Parse each outgoing arc and its capacity
            for j in range(1, len(line)):
                arc = line[j].strip(')').split('(')
                if len(arc) != 2:
                    continue
                dest_id, capacity = map(int, arc)
                graph[vertex_id][dest_id] = capacity

        return graph, k

def solution(graph, k):
    res = set()
    max_flow = min_max_flow = ford_fulkerson(deepcopy(graph), 0, len(graph) - 1)

    def backtrack(k, max_flow, arcs):
        nonlocal res, min_max_flow

        if max_flow == 0:
            res = arcs.copy()
            return
        
        if k == 0:
            if max_flow < min_max_flow:
                min_max_flow = max_flow
                res = arcs.copy()
            return
        
        for r in range(len(graph)):
            for c in range(len(graph)):
                arc = graph[r][c]

                # Avoid duplicates
                if arc == 0 or (r, c) in arcs or (c, r) in arcs:
                    continue

                graph[r][c] = 0
                max_flow = ford_fulkerson(deepcopy(graph), 0, len(graph) - 1)
                arcs.add((r, c))

                backtrack(k - 1, max_flow, arcs)

                arcs.remove((r, c))
                graph[r][c] = arc

    backtrack(k, max_flow, set())
    return res

def main():
    file_name = get_file_name()
    graph, k = parse_input_file(file_name)
    res = solution(graph, k)
    print_output(file_name, res)

if __name__ == "__main__":
    main()