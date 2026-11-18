# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline: Push numbers onto a stack. For each operator, pop the right and left
    # operands, apply it, and push the result back.
    stack = []
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            stack.append(int(token))
            continue

        right = stack.pop()
        left = stack.pop()
        if token == "+":
            result = left + right
        elif token == "-":
            result = left - right
        elif token == "*":
            result = left * right
        else:
            quotient = abs(left) // abs(right)
            result = -quotient if (left < 0) != (right < 0) else quotient
        stack.append(result)

    return stack[-1]


def decode_string(s):
    # Outline: Accumulate the current text and repeat count. At each opening bracket,
    # save both on a stack; at the closing bracket, repeat and append the inner text.
    stack = []
    current = []
    repeat_count = 0

    for char in s:
        if char.isdigit():
            repeat_count = repeat_count * 10 + int(char)
        elif char == "[":
            stack.append((current, repeat_count))
            current = []
            repeat_count = 0
        elif char == "]":
            previous, count = stack.pop()
            current = previous + current * count
        else:
            current.append(char)

    return "".join(current)


def daily_temperatures(temps):
    # Outline: Keep indices of days still waiting for a warmer temperature. When a
    # warmer day arrives, resolve earlier waiting days from the top of the stack.
    waits = [0] * len(temps)
    waiting_days = []

    for day, temperature in enumerate(temps):
        while waiting_days and temps[waiting_days[-1]] < temperature:
            previous_day = waiting_days.pop()
            waits[previous_day] = day - previous_day
        waiting_days.append(day)

    return waits


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline: Scan every cell. When unvisited land is found, count a new island and
    # use a stack to visit and mark all connected land cells.
    if not grid:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    island_count = 0

    for row in range(rows):
        for column in range(columns):
            start = (row, column)
            if grid[row][column] != "1" or start in visited:
                continue

            island_count += 1
            visited.add(start)
            to_visit = [start]
            while to_visit:
                current_row, current_column = to_visit.pop()
                for next_row, next_column in (
                    (current_row - 1, current_column),
                    (current_row + 1, current_column),
                    (current_row, current_column - 1),
                    (current_row, current_column + 1),
                ):
                    neighbor = (next_row, next_column)
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and grid[next_row][next_column] == "1"
                        and neighbor not in visited
                    ):
                        visited.add(neighbor)
                        to_visit.append(neighbor)

    return island_count


def main():
    print(eval_rpn(["2", "1", "+", "3", "*"]))                  # Expected: 9
    print(decode_string("3[a2[c]]"))                             # Expected: accaccacc
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]


if __name__ == "__main__":
    main()
