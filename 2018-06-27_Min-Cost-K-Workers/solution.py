#!/bin/python3

from datetime import datetime
import queue as Q

"""
Want K workers with the lowest wage per quality 'rate'. Everyone has a minimum rate they work for, so iterate through a sorted list of ascending rates to guarantee that, for worker[i], workers[:i] will accept the rate of worker[i] and the wage sum is calculated based on worker[i]'s rate.

Also want to minimise total wage, so evict workers with highest quality as tie-breaker (use maxheap to keep track). 

Sorting runs with O(nlog(n)) and subsequent for loop runs O(n) with heap operations running at O(log(n)) for total running time of O(nlog(n)).
"""
def minCostToHireWorkers_fast(quality, wage, K):
	count = len(quality)

	# compose list of workers with their quality, wage and 'rate'
	workers = list(map(lambda x: (x[1] / x[0], x[0], x[1]), zip(quality, wage)))
	
	# sort in ascending order of rates
	workers.sort()

	# init to 'infinity'
	res = 99999999
	quality_sum = 0
	quality_pq = Q.PriorityQueue()
	pq_count = 0

	for rate, q, w in workers:
		# negated insert since standard PQ is minheap
		quality_pq.put(-q)
		quality_sum += q
		pq_count += 1
	
		if pq_count > K:
			# evict worker with highest quality (use addition as PQ stores negations)
			quality_sum += quality_pq.get()
			pq_count -= 1
	
		if pq_count == K:
			# update smallest running total if necessary
			total = rate * quality_sum
			if total < res:
				res = total

	return res


"""
Naive approach. Every worker takes turns being the 'leader' where other workers' wages are adjusted relative to the leader's quality.

Outer for-loop runs for O(n) with an inner O(n) for-loop and sorting that takes O(nlog(n)), resulting in overall O(n^2 log(n))
"""
def minCostToHireWorkers_slow(quality, wage, K):
	count = len(quality)
	res = Q.PriorityQueue()

	for leader in range(count):
		q, w = quality[leader], wage[leader]

		worker_wages = Q.PriorityQueue()
		num_workers = 0

		for other in range(count):
			# normalise
			norm_quality = quality[other] / q
			min_pay = wage[other]
			required = norm_quality * w

			if required >= min_pay:
				# add to list
				worker_wages.put(required)
				num_workers += 1

		# ignore if not enough compatible workers
		if num_workers < K:
			continue

		# compute wage total for this set of workers
		total = 0
		for _ in range(K):
			total += worker_wages.get()

		res.put(total)

	# return minimum observed total from minheap
	return res.get()		


if __name__ == "__main__":
	print("Enter space-separated qualities: ", end="")
	quality = list(map(int, input().strip().split(' ')))

	print("Enter space-separated wages: ", end="")
	wage = list(map(int, input().strip().split(' ')))

	print("Enter number of workers to hire: ", end="")
	K = int(input().strip())

	# slow algo
	slow_start = datetime.now()
	res = minCostToHireWorkers_slow(quality, wage, K)
	slow_end = datetime.now()
	slow_duration = (slow_end - slow_start).total_seconds() * 1000
	print("Naive approach = ${} in {}ms.".format(res, slow_duration))

	# fast algo
	fast_start = datetime.now()
	res = minCostToHireWorkers_fast(quality, wage, K)
	fast_end = datetime.now()
	fast_duration = (fast_end - fast_start).total_seconds() * 1000
	print("Heap approach = ${} in {}ms.".format(res, fast_duration))
