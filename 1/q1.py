with(open('input.txt')) as file:
    lines = file.readlines()

total_increases = 0
for i in range(len(lines)):
    if i == 0:
        continue
    previous_measure = int(lines[i - 1])
    current_measure = int(lines[i])
    if current_measure > previous_measure:
        total_increases += 1

print(total_increases)
