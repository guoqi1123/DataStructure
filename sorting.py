# all sorts of sorting in ascending order using Python List
# insertion sort
# checkout this big O cheat sheet for complexity analysis: http://bigocheatsheet.com/
# the style follows the PEP 8: https://www.python.org/dev/peps/pep-0008/

def swap(a,b):
	# helper function for swap
	# we assume deep copy			
	c = a
	a = b
	b = c
	return a,b
	
def insertion_sort(arr):
	# we follow: https://en.wikipedia.org/wiki/Insertion_sort
	n_of_cmp = 0 # number of compare
	for i in range(len(arr)-1):
		j = i+1
		n_of_cmp += 1
		while(j >= 1 and arr[j-1] > arr[j]):
			arr[j-1], arr[j] = swap(arr[j-1], arr[j])
			j -= 1
			n_of_cmp += 1

	return arr, n_of_cmp

def bubble_sort(arr):
	# we follow: https://en.wikipedia.org/wiki/Bubble_sort
	n_of_cmp = 0 # number of compare
	swapped = True # the flag for whether a swap has occured, for early stopping
	n = len(arr) 
	while(swapped):
		swapped = False
		for i in range(n-1):
			n_of_cmp += 1
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = swap(arr[i], arr[i+1])
				swapped = True
		n -= 1
	
	return arr, n_of_cmp

def selection_sort(arr):
	# we follow: https://en.wikipedia.org/wiki/Selection_sort
	n_of_cmp = 0 # number of Compare
	n = len(arr)
	for i in range(n):
		# find the minimum in [i,n-1]
		i_min = i
		for j in range(i+1, n):
			n_of_cmp += 1
			# change the index of min when finding a smaller number
			if arr[j] < arr[i_min]:
				i_min = j
		# if we find someone smaller than arr[i], swap		
		if i_min != i:
			arr[i_min], arr[i] = swap(arr[i_min], arr[i])
	return arr, n_of_cmp


def quick_sort(arr):
	n_of_cmp = recursive_quick_sort(arr, 0, len(arr)-1, 0)
	return arr, n_of_cmp

def recursive_quick_sort(arr, lo, hi, n_of_cmp=0):
	# we follow: https://en.wikipedia.org/wiki/quick_sort
	if lo < hi:		
		p, n_of_cmp = partition(arr, lo, hi, n_of_cmp)
		n_of_cmp = recursive_quick_sort(arr, lo, p-1, n_of_cmp)
		n_of_cmp = recursive_quick_sort(arr, p+1, hi, n_of_cmp)
	return n_of_cmp

def partition(arr, lo, hi, n_of_cmp=0):
	# partition of quick_sort
	pivot = arr[hi]
	i = lo
	for j in range(lo, hi):
		n_of_cmp += 1
		if arr[j] < pivot:
			arr[i], arr[j] = swap(arr[i], arr[j])
			i += 1			
	# put the pivot in place
	arr[hi], arr[i] = swap(arr[hi], arr[i])
	return i, n_of_cmp

# top down approach of merge sort
# we follow: https://en.wikipedia.org/wiki/Merge_sort
def top_down_merge_sort(arr):
	# deep copy an extra array for sorting
	# this is why the space complexity is O(n)
	arr_s = [arr[i] for i in range(len(arr))]
	n_of_cmp = 0
	n_of_cmp = top_down_split_merge(arr, 0, len(arr)-1, arr_s, n_of_cmp)
	return arr_s, n_of_cmp

def top_down_split_merge(arr, lo, hi, arr_s, n_of_cmp):
	# first check if [lo,hi] contains only <= one element,
	# if so, consider sorted
	if hi <= lo:
		return n_of_cmp
	
	# otherwise split
	mid = int((hi + lo)/2) # auto conversion to integer
	### NOTICE THE CHANGE OF SEQUENCE OF arr_s AND arr
	n_of_cmp = top_down_split_merge(arr_s, lo, mid, arr, n_of_cmp)
	n_of_cmp = top_down_split_merge(arr_s, mid+1, hi, arr, n_of_cmp)

	# merge
	i = lo
	j = mid + 1
	for k in range(lo, hi+1):
		n_of_cmp += 1
		if i <= mid and (j > hi or arr[i] <= arr[j]):
			arr_s[k] = arr[i]
			i += 1
		else:
			arr_s[k] = arr[j]
			j += 1
	return n_of_cmp

# bottom up approach of merge sort
def bottom_up_merge_sort(arr):
	arr_s = [arr[i] for i in range(len(arr))]
	n_of_cmp = 0
	n = len(arr)
	width = 2
	while(width < 2*n):
		for i in range(int(n/width)+1):
			n_of_cmp = bottom_up_merge(
				arr, 
				i*width, 
				min(int(i*width + width/2-1), n-1), 
				min((i+1)*width-1, n-1), 
				arr_s, 
				n_of_cmp
			)
		# swap the arr and arr_s so that it always sort arr into arr_s,
		# we could also switch the roles of arr and arr_s each time
		tmp_arr = [arr[i] for i in range(len(arr))]
		arr = [arr_s[i] for i in range(len(arr_s))]
		arr_s = [tmp_arr[i] for i in range(len(tmp_arr))]
		width *= 2
	return arr, n_of_cmp

def bottom_up_merge(arr, lo, mid, hi, arr_s, n_of_cmp):
	# merge two sorted array ranging [lo,mid] and [mid+1,hi]
	if lo >= hi:
		return n_of_cmp
	i = lo
	j = mid + 1
	for k in range(lo, hi+1):
		n_of_cmp += 1
		if i <= mid and (j > hi or arr[i] <= arr[j]):
			arr_s[k] = arr[i]
			i += 1
		else:
			arr_s[k] = arr[j]
			j += 1
	return n_of_cmp

# prepare a random instance for testing
import random
a = [i for i in range(10)]
random.shuffle(a)
	
	
