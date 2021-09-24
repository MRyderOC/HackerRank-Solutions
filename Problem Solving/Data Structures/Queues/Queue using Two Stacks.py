s_in = []
s_out = []

for q in range(int(input())):
    operation = input()
    if operation[0] == '1':
        s_in.append(int(operation.split()[1]))
    elif operation[0] == '2':
        if not s_out:
            s_out = s_in[::-1]
            s_in = []
        s_out.pop()
    elif operation[0] == '3':
        if not s_out:
            s_out = s_in[::-1]
            s_in = []
        print(s_out[-1])

