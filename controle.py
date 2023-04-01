def parse_input_file(file_name):
    with open(file_name) as f:
        line = f.readline().strip().split(';')

        num_vertices = int(line[0])
        num_arcs_to_remove = int(line[1])
        adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

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
                adj_matrix[vertex_id][dest_id] = capacity

        return adj_matrix, num_arcs_to_remove



x = parse_input_file('data/ex1.csv')
print(x)
