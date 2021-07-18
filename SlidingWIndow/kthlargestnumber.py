from heapq import *
def findKthLargest(nums , k):
    minheap = []
    heapify(minheap)
    for i in range(k):
        heappush(minheap, nums[i])
    for j in range(k, len(nums)):
        print("Before",minheap)
        print(nums[j])
        if nums[j] > minheap[0]:
            heappush(minheap, nums[j])
            print(minheap)
            heappop(minheap)
    return minheap[0]


print(findKthLargest([-1,2,0],1))