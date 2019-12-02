import os, sys, math

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##loop through input row, or "ints"
with open(os.path.join(dirname, "input.txt")) as ints_list:
    ints = [int(x) for x in [ints.split(",") for ints in ints_list][0]]

def freshInput():
    return ints.copy()

curr_ints = freshInput()
correct_output = 19690720

def prepInput(noun, verb):
    curr_ints[1] = noun
    curr_ints[2] = verb

def calcAnswer(noun, verb):
    return noun * 100 + verb

def performAction(pos):
    print(pos)
    if curr_ints[pos] == 1:
        curr_ints[curr_ints[pos + 3]] = curr_ints[curr_ints[pos + 1]] + curr_ints[curr_ints[pos + 2]]
    elif curr_ints[pos] == 2:
        curr_ints[curr_ints[pos + 3]] = curr_ints[curr_ints[pos + 1]] * curr_ints[curr_ints[pos + 2]]

def run():
    pos = 0
    while (curr_ints[pos] != 99):
        performAction(pos)
        pos += 4

def findNounAndVerb():
    for noun in range(99):
        for verb in range(99):
            print(noun, verb)
            curr_ints = freshInput()
            prepInput(noun, verb)
            run()
            if (curr_ints[0] == correct_output):
                return calcAnswer(noun, verb)

print(findNounAndVerb())
