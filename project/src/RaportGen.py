import sys
import os


# Tworzy tablice z planszą
def create_table(symbols: str) -> str:
    table = '''<table class="board"><tr>'''
    for j, symbol in enumerate(symbols):
        if j % 5 == 0 and j != 0:
            table += "</tr><tr>"
        if symbol == 'x':
            player = "kacper"
        else:
            player = "olek"
        table += f'''<td class="{player}">{symbol}</td>'''
    table += "</table>"
    return table


if __name__ == '__main__':
    try:
        input_dir = sys.argv[1]
        output_file = sys.argv[2]
    except IndexError:
        raise SystemExit("Nie podano scieżki do plików!")

    # Odcztywanie plików wejściowych i tworzenie raportów
    raport_sections = []
    try:
        for i, filename in enumerate(os.listdir(input_dir)):
            if filename.endswith(".txt"):
                file = os.path.join(input_dir, filename)
                with open(file, encoding="utf8") as raport:
                    lines = raport.read().split('\n')
                    board = lines[0].split()
                    score_kacper = lines[1]
                    score_olek = lines[2]
                    result = lines[3]

                    section_header = f'''
<hr><section><div class="left">
<h3>Raport nr.{i+1} <span style="font-weight: normal">(Plik {filename})</span></h3>'''
                    section_table = create_table(board)
                    section_text = f'''
</div><div class="right">
<div class="score"><span class="kacper">Punkty dla gracza umieszczającego "x"</span>:<br>{score_kacper}</div>
<div class="score"><span class="olek">Punkty dla gracza umieszczającego "o"</span>:<br>{score_olek}</div>
<div class="result">{result}</div></div>
</section>'''
                    raport_sections.append(section_header + section_table + section_text)
    except IOError:
        raise SystemExit("Błąd podczas odczytywania plików z raportami!")

    # Zapisywanie raportów do pliku .html
    try:
        with open(output_file, "w", encoding="utf=8") as html:
            html.write('''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Zadanie 2 2014 - Kółko i Krzyżyk</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body {
background-color: #ffffcc;
text-align: center;
font-size: 1.1em
}
header h1 {
font-weight: bold;
color: red
}
h3 {
font-size: 1.5em
}
hr { 
border: none;
height: 2px;
background-color: black
} 
section {
display: flex;
align-items: center;
justify-content: space-around
}
.right {
text-align: left
}
table {
font-size: 2em
}
th ,td {
text-align: center;
font-size: 2em;
border: 3px solid black;
width: 2em
}
.kacper {
color: blue
}
.olek {
color: green
}
.score {
text-align: center;
font-size: 1.5em
}
.score span {
font-weight: bold
}
.result {
text-align: center;
font-size: 1.5em;
font-weight: bold
}
</style>
</head>
<body>
<header>
<h1>Algorytmion 2014 Zadanie 2 - "Kółko i Krzyżyk"</h1>
<h2>Raport wykonanych obliczeń</h2>
</header>''')
            for section in raport_sections:
                html.write(section)
            html.write('''
</body>
</html>''')
        print(f"Utworzono raport w pliku {output_file}")
    except IOError:
        raise SystemExit("Błąd podczas tworzenia raportu .html!")
