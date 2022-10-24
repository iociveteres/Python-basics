n, m = map(int, input().split())
mines_count = int(input())
mines = []
field = [[0 for j in range(m)] for i in range(n)]
for i in range(mines_count):
    x, y = map(int, input().split())
    mines.append((x - 1, y - 1))

neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= (n - 1) and
                                   -1 < y <= (m - 1) and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= (n - 1)) and
                                   (0 <= y2 <= (m - 1)))]

for i in range(n):
    for j in range(m):
        if (i, j) in mines:
            field[i][j] = '*'
            a = neighbors(i, j)
            for x, y in a:
                try:
                    int_value = int(field[x][y])
                except ValueError:
                    pass
                else:
                    field[x][y] += 1
            
for i in field:
    print(*i)
