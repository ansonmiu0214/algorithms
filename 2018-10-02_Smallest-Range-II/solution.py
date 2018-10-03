#!/bin/python3

"""
Make the list sorted first, so A[0] <= ... <= A[n-1].
Recognise that A[i] += K is equivalent to A[i] += {0, 2*K}.
Iterate through the list and attempt to add 2*K to A[i] to reduce the range.
"""
def smallestRange(A, K):
	A.sort()

	head, tail = A[0], A[-1]
	offset = 2*K
	higherHead = A[0] + offset
	
	minRange = tail - head
	end = len(A)
	
	for idx in range(end - 1):
		# no need to consider A[-1] + 2*K since A[-1] is largest by default
		localMax = max(tail, A[idx] + offset)
	
		# no need to consider A[0] + 0 since it is smallest by default
		localMin = min(higherHead, A[idx+1])

		minRange = min(minRange, localMax - localMin)

	return minRange


if __name__ == "__main__":
	print("Enter space-separated integers for A: ", end="")
	A = list(map(int, input().strip().split(' ')))

	print("Enter K: ", end="")
	K = int(input().strip())

	minRange = smallestRange(A, K)
	print(minRange)
