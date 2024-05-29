def maxArea(list):
    r = len(list) - 1
    l = 0
    currentVolume = 0
    maxVolume = 0
    while r-l > 0:
        # Get current volume based on the lower height
        if list[l] >= list[r]:
            currentVolume = (r-l) * list[r]
        else:
            currentVolume = (r-l) * list[l]
        # Check if this is a winning solution
        if currentVolume > maxVolume:
            maxVolume = currentVolume
        # Move the pointer of the smaller height
        if list[l] >= list[r]:
            r -= 1
        else:
            l += 1
    return maxVolume

# Testing Suite
list_1 = [1,2,1,1,2] # Solution = 6
list_2 = [0,0,0,1,0,2,0,0,0,2] # Solution = 8
list_3 = [0,0,0,1,0,2,10,10,0,2] # Solution = 10
list_4 = [0,0] # Solution = 0
list_5 = [0,100] # Solution = 0
list_6 = [1,1] # Solution = 1
list_7 = [1,1,1,1,1,1] # Solution = 5

print(maxArea(list_1))