class AdjMatrix:

    def __init__(self, infile):
        self.paths = ['-', '|', '/', '\\']
        self.directions = [('|', (-1, 0)),
                           ('/', (-1, 1)),
                           ('-', (0, 1)),
                           ('\\', (1, 1)),
                           ('|', (1, 0)),
                           ('/', (1, -1)),
                           ('-', (0, -1)),
                           ('\\', (-1, -1))]

        self.grid = dict()
        with open(infile, 'r') as inputFile:
            self.nedges = int(inputFile.readlines(1)[0])
            col, row = 0, 0
            while True:
                c = inputFile.read(1)
                if not c:
                    break
                elif c == "\n":
                    row += 1
                    col = 0
                elif c != ' ':
                    self.grid[(row, col)] = c
                    col += 1
                else:
                    col += 1

        self.nodes = {x[1]: x[0] for x in self.grid.items() if x[1].isalpha()}
        self.nnodes = len(self.nodes)

        self.edges = []
        for node in self.nodes.keys():
            dirs = self._get_dirs(self.grid, self.nodes[node], self.directions)
            for direction in dirs:
                self.edges.append((node, self._search(self.grid, self.nodes[node],
                                                      direction, self.directions, self.paths)))

        self.adj_matrix = [[0 for i in range(0, self.nnodes)] for j in range(0, self.nnodes)]
        for pair in self.edges:
            self.adj_matrix[ord(pair[0]) - 97][ord(pair[1]) - 97] = 1

        del self.directions
        del self.paths

    def __str__(self):
        output = '\n'
        for row in self.adj_matrix:
            output += ' '.join([str(x) for x in row])
            output += '\n'
        return output

    @staticmethod
    def _get_dirs(grid, pos, directions):
        dirs = []
        r1, c1 = pos
        for symbol, direction in directions:
            try:
                if grid[(r1 + direction[0], c1 + direction[1])] == symbol:
                    dirs.append(direction)
            except KeyError:
                pass
        return dirs

    @staticmethod
    def _search(grid, pos, direction, directions, paths):
        r1, c1 = pos
        r2, c2 = direction
        next_pos = (r1 + r2, c1 + c2)
        try:
            next_char = grid[next_pos]
            if next_char.isalpha():
                return next_char
            elif next_char == '#':
                new_dirs = AdjMatrix._get_dirs(grid, next_pos, directions)
                new_dirs.remove((direction[0] * -1, direction[1] * -1))
                new_dir = new_dirs[0]
                new_next_pos = (next_pos[0] + new_dir[0], next_pos[1] + new_dir[1])
                return AdjMatrix._search(grid, new_next_pos, new_dir, directions, paths)
            elif next_char in paths:
                return AdjMatrix._search(grid, next_pos, direction, directions, paths)
        except KeyError:
            return None
