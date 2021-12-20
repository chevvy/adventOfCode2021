from Window import Window

input1_file_name = 'inputP1.txt'
input2_file_name = 'inputP2.txt'


def q1_part_one(list_nb):
    total_increases = 0
    for i in range(len(list_nb)):
        if i == 0:
            continue
        previous_measure = int(list_nb[i - 1])
        current_measure = int(list_nb[i])
        if current_measure > previous_measure:
            total_increases += 1

    print("q1 answer" + str(total_increases))


def getLines(file_name):
    with(open(file_name)) as file:
        lines = file.readlines()
    return lines


def q1_part_two(list_nb):
    sum_list = []
    window = Window()
    for i in range(len(list_nb)):
        # if theres not enough data to get a full new window, we break
        if i + 2 >= len(list_nb):
            break
        for index in range(i, i+3):
            window.addNb(int(list_nb[index]))
        sum_list.append(window.getSum())
        window = Window()

    q1_part_one(sum_list)


q1_part_one(getLines(input1_file_name))
q1_part_two(getLines(input2_file_name))
