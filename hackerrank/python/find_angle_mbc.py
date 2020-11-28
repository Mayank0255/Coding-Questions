from math import degrees,atan2

AB = int(input())
BC = int(input())

print(str(int(round(degrees(atan2(AB,BC)),0))) + '°')
