def convert_number(x, b, moves):
    b += 1
    s1 = []
    s2 = []
    while x > 0:
        t = (x % b)
        if t == 0:
            return False
        s1.append(t)
        s2.append(t)
        x = int(x / b)

    for i in range(0, len(s1)):
        s2[len(s1) - 1 - i] = s1[i]

    if len(s2) == moves:
        return s2
    return False


def generate(lines, moves):
    x = []
    for i in range(1, (lines + 1) ** moves):
        if convert_number(i, lines, moves):
            x.append(convert_number(i, lines, moves))

    return x


def save_csv(var_to_save, filename):
    file_to_save = open(filename, 'w')
    i = 0
    while i < len(var_to_save):
        j = 0
        while j < len(var_to_save[i]):
            file_to_save.write(str(var_to_save[i][j]))
            j += 1
        file_to_save.write('\n')
        i += 1

    print('> saved file')


def load_csv(filename):
    var = []
    temp = []
    file_to_load = open(filename, 'r')
    file_to_load = file_to_load.read()
    for char in file_to_load:
        if '0' <= char <= '5':
            temp.append(int(char))
        else:
            var.append(temp)
            temp = []

    return var


def delete(variants, x):
    i = 0
    while len(x) > len(variants[i]):
        i += 1

    while i < len(variants):
        temp = []
        for j in range(0, len(x)):
            temp.append(variants[i][j])
        if temp == x:
            print('Delete', variants[i])
            variants.pop(i)
            i -= 1
        i += 1

    return variants



run = True
while run:
    function = input('''
> 1. generate new variations
> 2. edit variations
> 3. view file
> 4. quit
> ''')

    if function == '1':
        lines = int(input('> lines: '))
        moves = int(input('> moves: '))
        filename = input('> filename: ')
        var = generate(lines, moves)
        print('')
        print('> variations generated')
        print('> var size', len(var))
        save_csv(var, filename + '.txt')

    elif function == '2':
        filename = input('> filename: ')
        var = load_csv(filename + '.txt')
        x = []
        y = []
        temp = int(input('> (do not separate values) x: '))
        while temp != 0:
            y.append(temp % 10)
            temp = int(temp / 10)

        for i in range(0, len(y)):
            x.append(y[len(y) - 1 - i])
        print(x)

        var = delete(var, x)
        print('> var size', len(var))
        save_csv(var, filename + '.txt')

    elif function == '3':
        filename = input('> filename: ')
        var = load_csv(filename + '.txt')
        print(var)

    elif function == '4':
        run = False