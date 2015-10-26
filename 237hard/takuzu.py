import sys
import Numberjack


def main(arg):

    # read in data, get dimension
    with open(arg, "r") as infile:
        input_grid = [list(line.strip()) for line in infile.readlines()]
    dim = len(input_grid)
    target_sum = dim / 2

    # create model and a matrix of variables
    model = Numberjack.Model()
    grid = Numberjack.Matrix(dim, dim)

    # set known variables
    for r in range(dim):
        for c in range(dim):
            if input_grid[r][c] is not '.':
                model.add(grid[r][c] == int(input_grid[r][c]))

    # set sum and three-in-a-row constraints
    for row in grid.row:
        model.add(Numberjack.Sum(row) == target_sum)
        for i in range(dim - 2):
            model.add(Numberjack.Sum(row[i:i + 3]) > 0)
            model.add(Numberjack.Sum(row[i:i + 3]) < 3)
    for col in grid.col:
        model.add(Numberjack.Sum(col) == target_sum)
        for i in range(dim - 2):
            model.add(Numberjack.Sum(col[i:i + 3]) > 0)
            model.add(Numberjack.Sum(col[i:i + 3]) < 3)

    # treat each row and column as a binary number and impose the constraint that they must all be different
    model.add(Numberjack.AllDiff([Numberjack.Sum([grid[r][c] * 2**(dim-c-1) for c in range(dim)]) for r in range(dim)]))
    model.add(Numberjack.AllDiff([Numberjack.Sum([grid[r][c] * 2**(dim-r-1) for r in range(dim)]) for c in range(dim)]))

    # create solutions object
    solver = model.load("Mistral", grid)
    solver.solve()
    solution = solver.get_solution()

    # print solution
    solution = [str(x) for x in solution]
    solution = [solution[i:i+dim] for i in range(0, len(solution), dim)]
    for row in solution:
        print ' '.join(row)

if __name__ == "__main__":
    main(sys.argv[1])
