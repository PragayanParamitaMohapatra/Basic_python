import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:",nums_list)
# Find three smallest values
smallest_nums = hq.nsmallest(3, nums_list)
print("\nThree smallest numbers are:", smallest_nums)
