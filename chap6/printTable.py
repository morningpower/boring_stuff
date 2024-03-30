def print_table(table_data):
    col = len(table_data)
    row = len(table_data[0])

    col_width = [0] * col
    for index in range(col):
        for data in table_data[index]:
            col_width[index] = max(col_width[index], len(data))
    
    for r in range(row):
        for c in range(col):
            print(table_data[c][r].rjust(col_width[c]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)