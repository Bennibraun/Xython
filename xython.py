

def xylophuck(notes):
    brktmap = {}
    stack = []
    tape = [0]
    ptr = 0
    inloop = False
    i = 0
    for x in range(len(notes)):
        if notes[x] == 'B':
            stack.append(x)
        if notes[x] == 'K':
            brktmap[stack[len(stack)-1]] = x
            stack.pop()
    while( i < len(notes)):
        k = notes[i]
        if k == 'C':
            if ptr > 0:
                ptr = ptr - 1
        if k == 'D':
            if ptr == len(tape) - 1:
                tape.append(0)
            ptr += 1
        if k == 'E':
            tape[ptr] += 1
        if k == 'F':
            tape[ptr] += -1
        if k == 'G':
            tape[ptr] = int(input())
        if k == 'A':
            print(tape[ptr], sep="")
        if k == 'K':        
            if tape[ptr] > 0:
                i = brktmap[i]
        i = i+1
