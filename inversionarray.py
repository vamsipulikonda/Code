# Python3 program to count 
# For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 

def getInvCount(arr, n): 

	inv_count = 0
	for i in range(n): 
		for j in range(i + 1, n): 
			if (arr[i] > arr[j]): 
				inv_count += 1

	return inv_count 

# Driver Code 
arr = [2,4,1,3,5] 
n = len(arr) 
print("Number of inversions are", 
			getInvCount(arr, n)) 

# This code is contributed by Smitha Dinesh Semwal 
