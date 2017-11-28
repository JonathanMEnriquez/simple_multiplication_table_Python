
print "x , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12"
for rows in range(1,13):
    row = "  "
    for cols in range(0,13):
        if cols == 0:
            row = str(rows) + " "
        else:
            row = row + " " + str(rows * cols)
    print row

