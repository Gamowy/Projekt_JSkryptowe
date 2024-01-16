def loadBoard(filename: str) -> list:
    loaded_board = []
    try:
        with open(filename) as file:
            lines = file.readlines()
            lines = [l.strip() for l in lines]
            for line in lines:
                loaded_board.append(line.split(' '))
    except IOError:
        print("Nie udało się załadować pliku game.txt z planszą!")
        return None
    return loaded_board


def addPoints(count: int, points: list):
    match count:
        # 1 punkt
        case 2:
            points[0] += 1
        # 3 punkty
        case 3:
            points[1] += 1
        # 7 punktow
        case 4:
            points[2] += 1
        # 15 punktow
        case 5:
            points[3] += 1


if __name__ == "__main__":
    board = loadBoard('game.txt')
    usedPatterns = [[[False for _ in range(4)] for _ in range(5)] for _ in range(5)]
    kacperPoints = [0 for _ in range(4)]
    olekPoints = [0 for _ in range(4)]

    if board is not None:
        for i in range(5):
            for j in range(5):
                symbol = board[i][j]

                # Wiersze
                n = 0
                while (j + n < 5) and (board[i][j + n] == symbol) and (usedPatterns[i][j + n][0] == False):
                    usedPatterns[i][j + n][0] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacperPoints)
                else:
                    addPoints(n, olekPoints)

                # Kolumny
                n = 0
                while (i + n < 5) and (board[i + n][j] == symbol) and (usedPatterns[i + n][j][1] == False):
                    usedPatterns[i+n][j][1] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacperPoints)
                else:
                    addPoints(n, olekPoints)

                # Diagonale lewe
                n = 0
                while (i + n < 5) and (j - n >= 0) and (board[i + n][j - n] == symbol) and (usedPatterns[i + n][j - n][2] == False):
                    usedPatterns[i+n][j-n][2] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacperPoints)
                else:
                    addPoints(n, olekPoints)

                # Diagonale prawe
                n = 0
                while (i + n < 5) and (j + n < 5) and (board[i + n][j + n] == symbol) and (usedPatterns[i + n][j + n][3] == False):
                    usedPatterns[i+n][j+n][3] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacperPoints)
                else:
                    addPoints(n, olekPoints)

        # Sumowanie punktów
        sumKacper = kacperPoints[3] * 15 + kacperPoints[2] * 7 + kacperPoints[1] * 3 + kacperPoints[0] * 1
        sumOlek = olekPoints[3] * 15 + olekPoints[2] * 7 + olekPoints[1] * 3 + olekPoints[0] * 1

        # Wypisanie wyników
        print(f"Punkty dla gracza umieszczającego \"x\": {kacperPoints[3]}*15 + {kacperPoints[2]}*7 + {kacperPoints[1]}*3 + {kacperPoints[0]}*1 = {sumKacper}")
        print(f"Punkty dla gracza umieszczającego \"o\": {olekPoints[3]}*15 + {olekPoints[2]}*7 + {olekPoints[1]}*3 + {olekPoints[0]}*1 = {sumOlek}")

        if sumKacper > sumOlek:
            print("Wygrał kacper")
        elif sumOlek > sumKacper:
            print("Wygrał Olek")
        else:
            print("Jest remis")
