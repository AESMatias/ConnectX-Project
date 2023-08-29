values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

positions = [(val, i, j) for i in range(4)
             for j in range(3) for val in values if i % 2 == 0]

print(positions)
