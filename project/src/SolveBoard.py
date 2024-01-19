import sys


# Ładuje planszę
def loadBoard(filename: str) -> list:
    loaded_board = []
    try:
        with open(filename, encoding='utf=8') as board_file:
            lines = board_file.readlines()
            lines = [l.strip() for l in lines]
            for line in lines:
                loaded_board.append(line.split(' '))

        # Sprawdzanie poprawności wczytania danych
        if len(loaded_board) != 5:
            raise IOError
        for l in range(5):
            if len(loaded_board[l]) != 5 or not all(s == 'x' or s == 'o' for s in loaded_board[l]):
                raise IOError
    except IOError:
        print(f"Plik {filename} jest niepoprawny!")

    print(f"Pomyślnie załadowano plik {filename} z planszą")
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


if __name__ == '__main__':
    board = None
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    except IndexError:
        raise SystemExit("Nie podano scieżki do plików!")

    board = loadBoard(input_file)
    if board is not None:
        used_patterns = [[[False for _ in range(4)] for _ in range(5)] for _ in range(5)]
        kacper_points = [0 for _ in range(4)]
        olek_points = [0 for _ in range(4)]
        for i in range(5):
            for j in range(5):
                symbol = board[i][j]

                # Wiersze
                n = 0
                while (j + n < 5) and (board[i][j + n] == symbol) and (used_patterns[i][j + n][0] == False):
                    used_patterns[i][j + n][0] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacper_points)
                else:
                    addPoints(n, olek_points)

                # Kolumny
                n = 0
                while (i + n < 5) and (board[i + n][j] == symbol) and (used_patterns[i + n][j][1] == False):
                    used_patterns[i+n][j][1] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacper_points)
                else:
                    addPoints(n, olek_points)

                # Diagonale lewe
                n = 0
                while (i + n < 5) and (j - n >= 0) and (board[i + n][j - n] == symbol) and (used_patterns[i + n][j - n][2] == False):
                    used_patterns[i+n][j-n][2] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacper_points)
                else:
                    addPoints(n, olek_points)

                # Diagonale prawe
                n = 0
                while (i + n < 5) and (j + n < 5) and (board[i + n][j + n] == symbol) and (used_patterns[i + n][j + n][3] == False):
                    used_patterns[i+n][j+n][3] = True
                    n += 1
                if symbol == 'x':
                    addPoints(n, kacper_points)
                else:
                    addPoints(n, olek_points)

        # Sumowanie punktów
        sumKacper = kacper_points[3] * 15 + kacper_points[2] * 7 + kacper_points[1] * 3 + kacper_points[0] * 1
        sumOlek = olek_points[3] * 15 + olek_points[2] * 7 + olek_points[1] * 3 + olek_points[0] * 1

        # Wypisanie wyników
        try:
            with open(output_file, "w", encoding='utf-8') as out_file:
                for row in board:
                    print(*row, end=' ', file=out_file)
                print(f"\n{kacper_points[3]}*15 + {kacper_points[2]}*7 + {kacper_points[1]}*3 + {kacper_points[0]}*1 = {sumKacper}", file=out_file)
                print(f"{olek_points[3]}*15 + {olek_points[2]}*7 + {olek_points[1]}*3 + {olek_points[0]}*1 = {sumOlek}", file=out_file)
                if sumKacper > sumOlek:
                    print("Wygrał Kacper", file=out_file)
                elif sumOlek > sumKacper:
                    print("Wygrał Olek", file=out_file)
                else:
                    print("Jest remis", file=out_file)
            print(f"Zapisano wynik do pliku {output_file}")
        except IOError:
            print(f"Nie udało się zapisać do pliku {output_file}!")