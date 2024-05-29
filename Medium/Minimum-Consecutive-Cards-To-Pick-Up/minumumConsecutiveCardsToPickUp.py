def minimumCardPickup(list):
    lastOccurance = {str(list[0]): 0}
    min = 100001
    for j in range(len(list)-1):
        i = j+1
        if str(list[i]) in lastOccurance:
            dist = i - lastOccurance[str(list[i])] + 1
            if dist < min:
                min = dist
                # Smallest case. Found solution.
                if dist == 2:
                    return 2
            lastOccurance[str(list[i])] = i
        else:
            lastOccurance[str(list[i])] = i
    # No found matching cards.
    if min == 100001:
        return -1
    # Found a minimum case.
    else:
        return min


list_1 = [3,4,2,3,4,7] # Solution = 4
list_2 = [1,0,5,3] # Solution = -1
list_3 = [3,4,2,4,3,7] # Solution = 3
list_4 = [1] # Solution = -1
list_5 = [1,1] # Solution = 2
list_6 = [1,2,3,4,5,6,7,7,8,9,10,1] # Solution = 2, stops search at the pair of 7's.

print(minimumCardPickup(list_6))