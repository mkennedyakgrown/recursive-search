def recursive_search(arr, target):

    if len(arr) == 0:
        return False
    
    if arr[0] == target:
        return True
    
    return recursive_search(arr[1:], target)

print(recursive_search([7,12,5,23,8], 1))
print(recursive_search([3,4,5,6,7,8], 5))