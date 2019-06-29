import math
area = int(input())
while area != 0:
    side = int(math.sqrt(area))
    if area%side == 0:
        side2 = int(area/side)
    else:
        for i in range(side, 0, -1):
            if area%i == 0:
                side = i
                side2 = int(area/side)
                break
    perimeter = int(2*side + 2*side2)
    print("Minimum perimeter is " + str(perimeter)+ " with dimensions " + str(side) + " x " + str(side2))
    area = int(input())
                
    
