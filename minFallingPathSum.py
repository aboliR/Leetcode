def minFallingPathSum(matrix):
    '''
    Logic - keep first row as it is, start changing from second row, replace every element in the cell with min of above row's [col-1],col,[col+1] and add that element with the existing value of cell
    Time complexity - (n-1)*(n) = n^2 - n = O(n)
    Space complexity - O(1) as we are updating same matrix
    '''
    
    n = len(matrix)
    for row in range(1,n): # start from second row as u gonna check previous row for each value, for 0th there is no prev row
        for col in range(n):
            if col==0: # for 1st column, col-1 doesn't exist
                matrix[row][col] = min(matrix[row-1][col],matrix[row-1][col+1]) + matrix[row][col]
            if col>0 and col<n-1:
                matrix[row][col] = min(matrix[row-1][col-1],matrix[row-1][col],matrix[row-1][col+1]) + matrix[row][col]
            else: # for last col, col+1 doesn't exist
                matrix[row][col] = min(matrix[row-1][col-1],matrix[row-1][col]) + matrix[row][col]

    return(min(matrix[-1]))

matrix =  [[2,1,5,3],[6, -5, 4, 2],[7,8,9,-2],[5,2,1,-3]]
result = minFallingPathSum(matrix)
print(result)