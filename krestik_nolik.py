pole=[['1','2','3'],['4','5','6'],['7','8','9']]
for i in pole:
    print(*i, sep='|')
print('Вводите номер ячейки, сначала игрок №1, затем игрок №2 ')
def igra():
        x = int(input('Ход игрока №1 '))
        if x in [1, 2, 3]:
            pole[0][x - 1] = 'x'
        elif x in [4, 5, 6]:
            pole[1][x - 4] = 'x'
        elif x in [7, 8, 9]:
            pole[2][x - 7] = 'x'
        o = int(input('Ход игрока №2 '))
        if o in [1, 2, 3]:
            pole[0][o - 1] = 'o'
        elif o in [4, 5, 6]:
            pole[1][o - 4] = 'o'
        elif o in [7, 8, 9]:
            pole[2][o - 7] = 'o'
        for i in pole:
            print(*i, sep='|')
        if pole[0] == ['x', 'x', 'x'] or pole[1] == ['x', 'x', 'x'] or pole[2] == ['x', 'x', 'x'] or (
                pole[0][0] == 'x' and pole[1][0] == 'x' and pole[2][0] == 'x') or (
                pole[0][1] == 'x' and pole[1][1] == 'x' and pole[2][1] == 'x') or (
                pole[0][2] == 'x' and pole[1][2] == 'x' and pole[2][2] == 'x') or (
                pole[0][0] == 'x' and pole[1][1] == 'x' and pole[2][2] == 'x') or (
                pole[2][0] == 'x' and pole[1][1] == 'x' and pole[0][2] == 'x'):
            print('выйграл игрок №1')
            break
        if pole[0] == ['o', 'o', 'o'] or pole[1] == ['o', 'o', 'o'] or pole[2] == ['o', 'o', 'o'] or (
                pole[0][0] == 'o' and pole[1][0] == 'o' and pole[2][0] == 'o') or (
                pole[0][1] == 'o' and pole[1][1] == 'o' and pole[2][1] == 'o') or (
                pole[0][2] == 'o' and pole[1][2] == 'o' and pole[2][2] == 'o') or (
                pole[0][0] == 'o' and pole[1][1] == 'o' and pole[2][2] == 'o') or (
                pole[2][0] == 'o' and pole[1][1] == 'o' and pole[0][2] == 'o'):
            print('выйграл игрок №1')
            break
igra()

