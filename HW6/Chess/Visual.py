def visual(coordinates):
    matrix = [[' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8, [' '] * 8]
    columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    for i in coordinates:
        matrix[columns.index(i[0])][int(i[1]) - 1] = '♕'
    print(
        f"| {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} | {matrix[0][3]} |"
        f" {matrix[0][4]} | {matrix[0][5]} | {matrix[0][6]} | {matrix[0][7]} |")
    print(
        f"| {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} | {matrix[1][3]} |"
        f" {matrix[1][4]} | {matrix[1][5]} | {matrix[1][6]} | {matrix[1][7]} |")
    print(
        f"| {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} | {matrix[2][3]} |"
        f" {matrix[2][4]} | {matrix[2][5]} | {matrix[2][6]} | {matrix[2][7]} |")
    print(
        f"| {matrix[3][0]} | {matrix[3][1]} | {matrix[3][2]} | {matrix[3][3]} |"
        f" {matrix[3][4]} | {matrix[3][5]} | {matrix[3][6]} | {matrix[3][7]} |")
    print(
        f"| {matrix[4][0]} | {matrix[4][1]} | {matrix[4][2]} | {matrix[4][3]} |"
        f" {matrix[4][4]} | {matrix[4][5]} | {matrix[4][6]} | {matrix[4][7]} |")
    print(
        f"| {matrix[5][0]} | {matrix[5][1]} | {matrix[5][2]} | {matrix[5][3]} |"
        f" {matrix[5][4]} | {matrix[5][5]} | {matrix[5][6]} | {matrix[5][7]} |")
    print(
        f"| {matrix[6][0]} | {matrix[6][1]} | {matrix[6][2]} | {matrix[6][3]} |"
        f" {matrix[6][4]} | {matrix[6][5]} | {matrix[6][6]} | {matrix[6][7]} |")
    print(
        f"| {matrix[7][0]} | {matrix[7][1]} | {matrix[7][2]} | {matrix[7][3]} |"
        f" {matrix[7][4]} | {matrix[7][5]} | {matrix[7][6]} | {matrix[7][7]} |")
