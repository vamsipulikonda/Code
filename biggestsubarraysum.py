#Given an array arr of N integers. Find the contiguous sub-array with maximum sum
def max_subarray(arr):
    max_ending = max_current = arr[0]

    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)

    return max_current

print(max_subarray([1,2,3,-2,5]))
#Given an array arr of N integers. Find the contiguous sub-array with maximum sum