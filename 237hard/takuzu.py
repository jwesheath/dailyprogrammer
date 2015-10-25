import sys
import Numberjack


def check(solution, dim):
    solution_rows = [tuple(solution[i:i + dim]) for i in range(0, len(solution), dim)]
    solution_cols = zip(*solution_rows)
    if len(set(solution_rows)) == dim and len(set(solution_cols)) == dim:
        return True
    return False


def print_solution(solution, dim):
    solution = [str(x) for x in solution]
    solution = [solution[i:i+dim] for i in range(0, len(solution), dim)]
    for row in solution:
        print ' '.join(row)


def main(arg):

    with open(arg, "r") as infile:
        input_grid = [list(line.strip()) for line in infile.readlines()]
    dim = len(input_grid)
    target_sum = dim / 2
    model = Numberjack.Model()

    # matrix of variables
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

    # create solutions object
    solver = model.load("Mistral", grid)
    solver.solve()
    solution = solver.get_solution()

    # if first solution is good, print it and quit, else cycle through the rest
    if check(solution, dim):
        print_solution(solution, dim)
    else:
        try:
            while solver.getNextSolution():
                solution = solver.get_solution()
                if check(solution, dim):
                    print_solution(solution, dim)
                    break
        except StopIteration:
            pass


if __name__ == "__main__":
    main(sys.argv[1])
