# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input
 # 模板自带的输入

sequence = [0]
visited = {0}

for k in range(1, L):
    candidate = sequence[-1] - k
    if candidate > 0 and candidate not in visited:
        next_num = candidate
    else:
        next_num = sequence[-1] + k
    sequence.append(next_num)
    visited.add(next_num)

for item in sequence:
    print(item)

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence