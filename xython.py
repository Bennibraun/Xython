

def xylophuck(notes):
    brktmap = {}
    rbrktmap = {}
    stack = []
    tape = [0]
    ptr = 0
    inloop = False
    i = 0
    for x in range(len(notes)):
        if notes[x] == 'B':
            stack.append(x)
        if notes[x] == 'K':
            brktmap[x] = stack[len(stack)-1]
            rbrktmap[stack[len(stack)-1]] = x
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
            # print(tape[ptr], sep="")
            print(chr(tape[ptr]), sep="",end='')
        if k == 'B':
            if tape[ptr] == 0:
                i = rbrktmap[i]
        if k == 'K':
            if tape[ptr] > 0:
                i = brktmap[i]
        i = i+1

# C <
# d >
# e +
# f -
# g ,
# a .
# b [
# k ]

def translate_brainfuck(notes):
    notes = notes.replace('\n','')
    notes = notes.replace(' ','')
    notes = [c for c in notes]
    print(notes)
    bf_list = ['<','>','+','-',',','.','[',']']
    note_list = ['C','D','E','F','G','A','B','K']
    translation = ''
    for i in range(len(notes)):
        translation += note_list[bf_list.index(notes[i])]
    
    return translation

# xylophuck(translate_brainfuck('++>+++++[<+>-]++++++++[<++++++>-]<.'))
xylophuck(translate_brainfuck('-->+++>+>+>+>+++++>++>++>->+++>++>+>>>>>>>>>>>>>>>>->++++>>>>->+++>+++>+++>+++>+++>+++>+>+>>>->->>++++>+>>>>->>++++>+>+>>->->++>++>++>++++>+>++>->++>++++>+>+>++>++>->->++>++>++++>+>+>>>>>->>->>++++>++>++>++++>>>>>->>>>>+++>->++++>->->->+++>>>+>+>+++>+>++++>>+++>->>>>>->>>++++>++>++>+>+++>->++++>>->->+++>+>+++>+>++++>>>+++>->++++>>->->++>++++>++>++++>>++[-[->>+[>]++[<]<]>>+[>]<--[++>++++>]+[<]<<++]>>>[>]++++>++++[--[+>+>++++<<[-->>--<<[->-<[--->>+<<[+>+++<[+>>++<<]]]]]]>+++[>+++++++++++++++<-]>--.<<<]'))

