def convolution(array1: list, array2: list):
    array2 = array2[::-1]
    start = 1
    end = len(array1)+len(array2)
    
    result = []

    for i in range(start, end):

        if i <= len(array1):
            arr1_comb, arr2_comb = array1[:i], array2[-i:]
        else:
            arr1_comb, arr2_comb = array1[i-len(array1):], array2[:len(array2)-i] 

        element_sum = sum([el1*el2 for el1, el2 in zip(arr1_comb, arr2_comb)])
        result.append(element_sum)
    
    return result


x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(convolution(x, y))