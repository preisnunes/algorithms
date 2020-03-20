# Algorithm to solve recursively and interactively the pascal triangle 
# Return the pascal triangle entry given the line and position.
# Two implementation were done: a recursive and a iteractive one
def pascal_recursive(line :int, pos :int) ->int:
    if pos not in range(0,line + 1):
        return -1

    if line == 0:
        return 1

    if pos == 0 or pos == line:
        return 1

    return pascal_recursive(line-1, pos-1) + pascal_recursive(line-1, pos)

def pascal_iterative(line :int, pos :int) -> int:
    if pos not in range(0,line + 1):
        return -1

    if line == 0:
        return 1

    if pos == 0 or pos == line:
        return 1

    previous_line = []
    for i in range(0, line):
        line = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                line.append(1)
                continue
            line.append(previous_line[j] + previous_line[j-1])
        previous_line = line
    

    return previous_line[pos] + previous_line[pos-1]

print(pascal_iterative(6, 3))
print(pascal_recursive(6, 3))
            

            





