def binary_search(l, target):
    left,right = 0, len(l) - 1  #left = 0 , right len(l) - 1

    while (left <= right):
        midpoint = (left + right) // 2 

        if l[midpoint] == target:
            return midpoint
        elif l[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1

    return "Target not found"

if __name__=='__main__':

    l = [1, 3, 5, 10, 12]
    target = 10
    print(binary_search(l, target))