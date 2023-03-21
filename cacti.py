def cacti_number(plot):
    cacti = 0
    numRows = len(plot)
    numCols = len(plot[0])
    list0 = [0]

    #Increase dimensions of array by 2 and pad 0s all around.
    zeroRow = [0] * (numCols + 2)
    newPlot = [zeroRow]

    #For every row append a 0 in front and a 0 at the end
    for row in plot:
        row = list0 + row
        row = row + list0
        newPlot = newPlot + [row]

    #Append 0s as first row and 0s as last row
    newPlot = newPlot + [zeroRow]

    #Cacti logic
    numRows = len(newPlot) #Redefine row col vals
    numCols = len(newPlot[0])
    for i in range(1,numRows-1):
        for j in range(1,numCols-1):
            if (newPlot[i][j] == 0): #If a 0 is observed
                if (newPlot[i][j-1] == 0 and newPlot[i][j+1] == 0 and newPlot[i-1][j] == 0 and newPlot[i+1][j] == 0): #Compare its neighbors and check if they are 0s
                    cacti = cacti + 1
                    newPlot[i][j] = 1
    return cacti