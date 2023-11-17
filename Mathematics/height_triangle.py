from math import ceil

def lowestTriangle(trianglebase, area):
  return ceil((area*2)/trianglebase)


print(lowestTriangle(575954,646422))
