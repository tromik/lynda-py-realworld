""" A 3-Dimensional Valet Service """

# 2D list of lists
#  - index cars by row, spot
lot_2d = [['Toyota','Audi','BMW'], # 0th row
          ['Lexus','Jeep'],        # 1st row
          ['Honda','Kia','Mazda']] # 2nd row

# 3D list of lists of lists
#  - index cars by floor, row, spot
lot_3d = [[['Telsa','Fiat','BMW'], # 0th floor
           ['Honda','Jeep'],
           ['Saab','Kia','Ford']],
          [['Subaru','Nissan'],    # 1st floor
           ['Volvo']],
          [['Mazda','Chevy'],      # 2nd floor
           [],
           ['Volkswagen']]]

# lists are mutable
print(lot_2d)
print(lot_2d[2])
print(lot_2d[2][1])

print(lot_3d)
print(lot_3d[0])
print(lot_3d[0][2])
print(lot_3d[0][2][1])

for floor in lot_3d:
    for lot in floor:
        for car in lot:
            print(car)
