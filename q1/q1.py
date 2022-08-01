import os.path as path

project_path = path.abspath(path.dirname(__file__))
file_path = path.join(project_path, "DFA_Input_1.txt")
# open file
file = open(file_path, "r")

numberLine = 0

alphabet = states = initialState = finalStates = inputString = currState = ""

flag = False

enteghal = []
# read file
for f in file:
    if numberLine == 0:
        alphabet = f
    elif numberLine == 1:
        states = f
    elif numberLine == 2:
        initialState = f
    elif numberLine == 3:
        finalStates = f
    else:
        enteghal.append(f)
    numberLine = numberLine + 1

# set initial state
currState = initialState.strip()

# set alphabets , initialStates and finalStates
arr_alphabet = alphabet.split(" ")
arr_states = states.split(" ")
arr_finalStates = finalStates.split(" ")

# take input from user
inputString = input()

# check input string with dfa
for s in inputString:
    for e in enteghal:
        currEnteghal = e.split(" ")
        if currEnteghal[0] == currState and currEnteghal[1] == s:
            currState = currEnteghal[2].strip()
            break

# check if the string is accepted or not
for f in arr_finalStates:
    if currState == f.strip():
        flag = True

if flag:
    print("yes", end=" ")
else:
    print("no", end=" ")
