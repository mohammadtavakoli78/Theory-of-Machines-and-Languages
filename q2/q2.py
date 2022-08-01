import os.path as path

project_path = path.abspath(path.dirname(__file__))
file_path = path.join(project_path, "NFA_Input_2.txt")

# open file
file = open(file_path, "r")

numberLine = 0

alphabet = states = initialState = finalStates = currState = ""

enteghal = []
DFA_states = []
DFA_enteghal = []
DFA_finalStates = []

flag = False

# read file
for f in file:
    if numberLine == 0:
        alphabet = f.split()
    elif numberLine == 1:
        states = f.split()
    elif numberLine == 2:
        initialState = f
    elif numberLine == 3:
        finalStates = f.split()
    else:
        enteghal.append(f.strip())
    numberLine = numberLine + 1

# set initial state
currState = initialState.strip()

DFA_states.append("{"+currState+"}")

# find dfaStates and dfa_enteghals
for i in DFA_states:
    temp = i[1:-1]
    if temp[0] != "t":
        tempStates = temp.split(",")
        for a in alphabet:
            string = "{"
            l = []
            for t in tempStates:
                for s in enteghal:
                    sourceState = s.split(" ")[0]
                    alph = s.split(" ")[1]
                    destinationState = s.split(" ")[2]
                    if (sourceState == t or sourceState in l) and alph == a:
                        tempStr = string
                        tempStr = tempStr[1:]
                        tempStrs = tempStr.split(",")
                        if not (destinationState in tempStrs):
                            string += destinationState + ","

                    ll = []
                    for ss in enteghal:
                        if (ss.split(" ")[0] == destinationState or ss.split(" ")[0] in ll) and not (ss.split(" ")[1] in alphabet):
                            ll.append(ss.split(" ")[2])
                    for l2 in ll:
                        tempStr = string
                        tempStr = tempStr[1:]
                        tempStrs = tempStr.split(",")
                        if not (l2 in tempStrs):
                            string += l2 + ","

                    if sourceState == t and not (alph in alphabet):
                        l.append(destinationState)
                    if sourceState != t and not (alph in alphabet) and sourceState in l:
                        l.append(destinationState)


            if string == "{":
                counter = 0
                for s2 in DFA_states:
                    tempStr = s2[1:-1]
                    if tempStr[0] == 't':
                        counter = counter+1
                DFA_enteghal.append(i+" "+a+" "+"{t"+str(counter)+"}")
                DFA_states.append("{t"+str(counter)+"}")
                for a2 in alphabet:
                    DFA_enteghal.append("{t"+str(counter)+"}"+" "+a2+" "+"{t"+str(counter)+"}")
            else:
                string = string[:-1]
                string += "}"
                tempS = string[1:-1]
                tempSArray = tempS.split(",")
                tempSArray.sort()
                string2 = "{"
                for count in tempSArray:
                    string2 += count+","
                string2 = string2[:-1]
                string2 += "}"
                if not (string2 in DFA_states):
                    DFA_states.append(string2)
                DFA_enteghal.append(i + " " + a + " " + string2)

# for s in DFA_enteghal:
#     print(s)
# for s in DFA_states:
#     print(s)

#  find dfa_final states
for s in DFA_states:
    string = s[1:-1]
    strArray = string.split(",")
    for f in finalStates:
        if f in strArray:
            DFA_finalStates.append(s)

# check if nfa accept landa or not
firstState = currState
for i in range(0, len(enteghal)):
    for s in enteghal:
        sourceState = s.split(" ")[0]
        alph = s.split(" ")[1]
        destinationState = s.split(" ")[2]
        if firstState == sourceState and not (alph in alphabet):
            firstState = destinationState
            if destinationState in finalStates:
                flag = True
                break

string = " ".join(str(x) for x in finalStates)
check = "{"+currState+"}"
if flag:
    if not (check in string):
        DFA_finalStates.append(check)

# write file
file_path2 = path.join(project_path, "DFA_Output_2.txt")
f = open(file_path2, "w")
f.write(" ".join(str(x) for x in alphabet) + "\r")
f.write(" ".join(str(x) for x in DFA_states) + "\r")
f.write("{"+currState+"}" + "\r")
f.write(" ".join(str(x) for x in DFA_finalStates) + "\r")
for s in DFA_enteghal:
    f.write(s + "\r")
