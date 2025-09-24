def is_same_stripes(matrix):
  # m= #ofrow, n= #ofcolumn
  m, n = len(matrix), len(matrix[0])
  
  #check all diagonals that start on first row
  for col in range(n): #go from comlumn 0 to n-1
    value = matrix[0][col]
    i = 0
    j = col
    while i<m and j<n:
      if matrix[i][j] != value:
        return False
      i=i+1
      j=j+1
  
  #check check all diagonals that start on first column
  for row in range(m):
    value = matrix[1][row] #already check matrix[0][0]
    i=1
    j=row
    while i<m and j<n:
      if matrix[i][j] != value:
        return False
    i=i+1
    j=j+1
  return True
