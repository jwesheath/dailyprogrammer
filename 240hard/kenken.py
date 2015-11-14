import Numberjack
import operator

# read in dimesion and data
with open('input1.txt', 'r') as f:
    dim = int(f.readline().strip())
    lines = f.read().splitlines()

# create model and a matrix of variables, name them for convenience
model = Numberjack.Model()
grid = [[Numberjack.Variable(1, dim, chr(j+65)+str(i+1)) for j in range(dim)]
                                                         for i in range(dim)]

# read each line of input and add constraints to model
for line in lines:
    data = line.split()
    result = int(data[0])
    op = data[1]
    cells = data[2:]
    cell_tuples = [(int(cell[1]) - 1, ord(cell[0]) - 65) for cell in cells]
    variables = [grid[ct[0]][ct[1]] for ct in cell_tuples]
    if op == '+':
        model.add(Numberjack.Sum(variables) == result)
    elif op == '*':
        model.add(reduce(operator.mul, variables) == result)
    elif op == '-':
        model.add((variables[0] - variables[1] == result) |
                  (variables[1] - variables[0] == result))
    elif op == '/':
        model.add((variables[0] / variables[1] == result) |
                  (variables[1] / variables[0] == result))
    elif op == '=':
        model.add(variables[0] == result)

# ensure rows and columns don't have duplicates
for row in grid:
    model.add(Numberjack.AllDiff(row))
col_wise = map(list, zip(*grid))
for col in col_wise:
    model.add(Numberjack.AllDiff(col))

# solve and print
solver = model.load("MiniSat", grid)
solver.solve()
solution = solver.get_solution()
solution = [str(x) for x in solution]
solution = [solution[i:i+dim] for i in range(0, len(solution), dim)]
for row in solution:
    print ' '.join(row)
