x = 0
y = 0
current_move = -1

#открытие файлов
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

#работа с входным файлом

#считывание размера поля
s = fin.read(1)
t = fin.read(1)
while (t.isalnum()):
    s += t
    t = fin.read(1)
N = int(s)

#создание поля
field = [[0] * N for i in range(N)]
#считывание поля
for i in range(N):
    for j in range(N):
        s = fin.read(1)
        while(s.isalnum() == False):
            s = fin.read(1)
        long_num = fin.read(1)
        while(long_num.isalnum()):
            s += long_num
            long_num = fin.read(1)
        field[i][j] = int(s)
        #нахождение позиции коня
        if (field[i][j] > current_move):
            current_move = field[i][j]
            x = i
            y = j

#особый случай, если дали пустое поле
if (current_move == 0):
    field[x][y] = 1
    current_move+= 1

current_move+= 1

#закрытие входного файла
fin.close()

maxk = 0
next_x = 0
next_y = 0
min_possible_moves = 9
move1 = [2, 1, -1, -2, -2, -1, 1, 2] # всевозможные ходы из любой клетки ТИПО ЭТО х
move2 = [1, 2, 2, 1, -1, -2, -2, -1] # смещением координаты на [move1[x], move2[x]] ТИПО ЭТО y

#количество возможных ходов из клетки [i][j]
def possible_moves(i: int, j: int) -> int:
    k = 0
    for now in range(8):
        #проверка, что ход - возможный и что поле не было посещено! 
        if (i + move1[now] < N and i + move1[now] >= 0 and j + move2[now] < N and j + move2[now] >= 0 and field[i + move1[now]][j + move2[now]] == 0):
            k+= 1
    return k
        
while (current_move != (N*N+1)):

    for i in range(8): #проверка каждого поля
        if (x + move1[i] < N and x + move1[i] >= 0 and y + move2[i] < N and y + move2[i] >= 0 and field[x + move1[i]][y + move2[i]] == 0):
        
            # количество возможных ходов из поля, куда можно пойти прямо сейчас
            temp = possible_moves(x + move1[i], y + move2[i])
            
            # если возможных ходов меньше, чем в ранее найденных клетках
            if(temp < min_possible_moves):
                min_possible_moves = temp

                # запоминаем поле
                next_x = move1[i] 
                next_y = move2[i]

    #пишем в поле номер хода
    field[x+next_x][y+next_y] = current_move
    current_move+= 1
    #обнуление для следующего хода
    min_possible_moves = 9
    x = x+next_x
    y = y+next_y


#запись поля в выходной файл
for i in range(N):
    for j in range(N):
        fout.write(str(field[i][j]) + "\t")
    fout.write("\n\n")

#закрытие выходного файла
fout.close()
